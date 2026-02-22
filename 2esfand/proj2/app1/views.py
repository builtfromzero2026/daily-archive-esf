from django.shortcuts import render

def index(request):
    return render(request, 'app1/index.html', {})


esm = "Delaram"
def var1(request):
    return render(request, 'app1/var1.html', {'name': esm})


matn = "salam in matn baraye test hast"
def var2(request):
    return render(request, 'app1/var2.html',{'text':matn})


khali = ''
def var3(request):
    return render(request, 'app1/var3.html', {'nothing': khali})


lst = ['one', 'two', 'three']
def var4(request):
    return render(request, 'app1/var4.html',{'list':lst})


num = 5
def var5(request):
    return render(request, 'app1/var5.html', {'number': num})