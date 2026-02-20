from django.shortcuts import render


_dict = {
    'Google':'https://google.com',
    'Apple':'https://apple.com',
    'Yahoo':'https://yahoo.com',
}


def blog(request):
    return render(request, 'app1/blog.html', {'links': _dict })

def test(request):
    return render(request, 'app1/test.html', {})