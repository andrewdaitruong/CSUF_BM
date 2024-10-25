from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from django.contrib import messages #added 10/22
from .forms import ProductSortForm, CategoryForm, ProductForm # Added 10/22 CategoryForm and ProductForm
# Create your views here.
#modified 10/18
def store(request, category_slug=None):
    categories = None
    products = None
    sort_form = ProductSortForm(request.GET)

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    if sort_form.is_valid():
        sort_by = sort_form.cleaned_data['sort_by']
        if sort_by:
            products = products.order_by(sort_by)

    context = {
        'products': products,
        'sort_form': sort_form,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)

#added 10/18

def categories_processor(request):
    return {
        'categories': Category.objects.all()
    }

@login_required
def manage_category(request, category_id=None):
    category = None
    if category_id:
        category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 
                           f'Category {"updated" if category else "added"} successfully!')
            return redirect('manage_items')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'title': 'Edit Category' if category else 'Add New Category',
        'category': category,
        'is_edit': bool(category)
    }
    return render(request, 'admin/category_form.html', context)

@login_required
def manage_product(request, product_id=None):
    product = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 
                           f'Product {"updated" if product_id else "added"} successfully!')
            return redirect('manage_items')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'title': 'Edit Product' if product else 'Add New Product',
        'product': product,
        'is_edit': bool(product)
    }
    return render(request, 'admin/product_form.html', context)

@login_required
def manage_items(request):
    categories = Category.objects.all()
    products = Product.objects.all().select_related('category')  # Optimize query
    
    context = {
        'categories': categories,
        'products': products,
        'title': 'Manage Items'
    }
    return render(request, 'admin/manage_items.html', context)