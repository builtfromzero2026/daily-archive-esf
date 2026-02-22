from django.shortcuts import render

connectionn = {
    'jabama': 'https://www.jabama.com/',
    'jajiga': 'https://www.jajiga.com/',
}
def ertebat(request):
    return render(request,'ertebat/ertebat.html',{'ertt': connectionn})