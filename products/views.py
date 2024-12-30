from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Genre, Format

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting & search queries """

    products = Product.objects.all()
    query = None
    categories = None
    genres = None
    formats = None
    sort = None
    direction = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'format' in request.GET:
            formats = request.GET['format'].split(',')
            products = products.filter(format__format__in=formats)
            formats = Format.objects.filter(format__in=formats)

        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            products = products.filter(genre__genre__in=genres)
            genres = Genre.objects.filter(genre__in=genres)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products')) 

            queries = Q(title__icontains=query) | Q(artist__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_genres': genres,
        'current_formats': formats,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'search_term': query,
    }

    return render(request, 'products/product_detail.html', context)
