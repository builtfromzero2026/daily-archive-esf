from django.shortcuts import render
from django.http import HttpResponseNotFound

products = {
    'iphone 13 pro max' :{
        'slug':'iphone-13-pro-max' ,
        'image':'iphone-13-pro-max.jpg' ,
        'price' :'500', 
        'discription':'The only iphone that you can register in Iran',
        'des' : 'smart phone ',
    },
    'samsung s24 ultra':{
        'slug':'samsung-s24-ultra' ,
        'image':'samsung-s24-ultra.jpg' ,
        'price' :'400', 
        'discription':'lastest samsung smart phone',
        'des' : 'beautiful phone',
    },
    'xiaomi poco x6':{
        'slug': 'xiaomi-poco-x6',
        'image':'xiaomi-poco-x6.jpg' ,
        'price' :'300', 
        'discription':'latest xiaomi phone',
        'des' : 'blue 256G',
    },
    'huawei nova 12i':{
        'slug': 'huawei-nova-12i',
        'image':'huawei-nova-12i.jpg',
        'price':'200',
        'discription':'latest huawei smart phone',
        'des':'green 512G',
    },
    'nokia 1100':{
        'slug':'nokia-1100',
        'image':'nokia-1100.jpg',
        'price':'100',
        'discription':'strong as a rock',
        'des':'small phone',
    },
}


def index(request):
    return render(request, 'shop/index.html', {'products': products.items(), 'caller':'home'})

def prod_det(request, x):  
    item = x.replace("-", " ")
    if item in products:
        return render(request, 'shop/prod-det.html', {'product': item, 'details': products[item], 'caller': 'details'})
    return HttpResponseNotFound("Item does not exists")