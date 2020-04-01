from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


# Create your views here.
def index_goods(request):
    """
    Main page.
    Shows only 3 highest-price products
    """
    categories = Category.objects.all()

    products = Product.objects.order_by('-price')[:3]
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'goods/index.html', context)


def product_detail(request, id, slug):
    """
    Product page
    """
    categories = Category.objects.all()

    product = get_object_or_404(Product, id=id, slug__iexact=slug, available=True)
    cart_product_form = CartAddProductForm()
    # product = Product.objects.get(slug__iexact=slug)
    context = {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form
    }
    return render(request, 'goods/product_detail.html', context)


def category_detail(request, slug):
    """
    Categories page
    """
    categories = Category.objects.all()

    category = Category.objects.get(slug__iexact=slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories
    }
    return render(request, 'goods/category_detail.html', context)


def delivery_detail(request):
    """
    Deliveries page
    """
    categories = Category.objects.all()

    context = {'categories': categories}
    return render(request, 'goods/delivery.html', context)


def contacts_detail(request):
    """
    Contacts page
    """
    categories = Category.objects.all()

    context = {'categories': categories}
    return render(request, 'goods/contacts.html', context)
