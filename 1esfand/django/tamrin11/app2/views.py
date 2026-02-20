from django.shortcuts import render

def support(request):
    return render(request, 'app2/support.html', {})

def profile(request):
    return render(request, 'app2/profile.html', {})
