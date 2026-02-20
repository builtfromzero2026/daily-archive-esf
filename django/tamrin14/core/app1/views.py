from django.shortcuts import render

def blog(request):
    return render(request, 'app1/blog.html', {})

def test(request):
    return render(request, 'app1/test.html', {})