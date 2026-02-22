from django.shortcuts import render

# Create your views here.
taf = {
    'irantafrihan': 'https://irantafrih.com/',
    'tafrihi2': 'https://tafrihnet.com/',
}
def tafrih(request):
    return render(request,'tafrih/tafrih.html',{'glt': taf})