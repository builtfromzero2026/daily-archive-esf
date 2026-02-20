from django.shortcuts import render


def profile(request):
    return render(request,'app2/profile.html', {})

def support(request):
    return render(request, 'app2/support.html', {})