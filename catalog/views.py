from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import ProductForm

"""
    Display the product dashboard.

    Fetches all products and filters them based on a search query if provided.
    @login_required: Accessible only to authenticated users.

    Argument:
        request: The HTTP request object.

    Returns:
        response: Rendered HTML for the dashboard page.
"""
@login_required
def dashboard(request):
    products = Product.objects.all()
    query = request.GET.get('search', '')
    if query:
        products = products.filter(name__icontains=query) | products.filter(category__name__icontains=query)
    return render(request, 'catalog/dashboard.html', {'products': products})


"""
    Handle adding a new product.

    Displays a form for creating a product and processes the form submission.
    @login_required: Accessible only to authenticated users.

    Argument:
        request: The HTTP request object.

    Returns:
        response: Redirect to the dashboard after successful product creation.
"""
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})


"""
    Handle editing an existing product.

    Displays a form pre-filled with the product's current data and helps updating the product details.
    @login_required: Accessible only to authenticated users.

    Argument:
        request: The HTTP request object.

    Returns:
        response: Redirect to the dashboard after successful product update.
"""
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_form.html', {'form': form})


"""
    Handle deleting an existing product.

    Deletes the product and then refreshes the product list.
    @login_required: Accessible only to authenticated users.
"""
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(request,  {'product': product})
