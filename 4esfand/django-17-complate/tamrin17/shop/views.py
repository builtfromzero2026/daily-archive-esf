from django.shortcuts import render
from django.http import HttpResponseNotFound

products = {
    'iphone 13 pro max':{
        'slug':'iphone-13-pro-max',
        'image':'iphone-13-pro-max.jpg',
        'description':'The only iphone that you can register in Iran.',
        'details':'256G Blue',
        'price':'500.0',
    },
    'samsung s24 ultra':{
        'slug':'samsung-s24-ultra',
        'image':'samsung-s24-ultra.jpg',
        'description':'lastest samsung smartphone. That uses AI to fake photos of the moon.',
        'details':'512G Gray',
        'price':'245.0',
    },
    'huawei nova 12i':{
        'slug':'huawei-nova-12i',
        'image':'huawei-nova-12i.jpg',
        'description':'latest huawei smartphone. An exclusive product.',
        'details':'128G Persian Green',
        'price':'200',
    },
    'nokia 1100':{
        'slug':'nokia-1100',
        'image':'nokia-1100.jpg',
        'description':'Strong as a rock',
        'details':'unlimited storage and butteries',
        'price':'15',
    },
    'xiaomi poco x6':{
        'slug':'xiaomi-poco-x6',
        'image':'xiaomi-poco-x6.jpg',
        'description':'Latest xiaomi smartphone.',
        'details':'256G Yellow',
        'price':'300.0',
    },

}

def index(request):
    return render(request, 'shop/index.html', {'products': products.items(), 'caller': 'home'})


def product_details_view(request, x):
    item = x.replace('-', ' ')
    if item in products:
        return render(request, 'shop/product-details.html', { 'product':item, 'details': products[item], 'caller': 'details' })
    return HttpResponseNotFound("Item does not exists")
