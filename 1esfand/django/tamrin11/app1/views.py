from django.shortcuts import render

name = 'ehsan'

def blog(request):
    return render(request, 'app1/blog.html', {'name': name})

def test(request):
    return render(request, 'app1/test.html', {})