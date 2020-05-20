from django.shortcuts import render


def myhandler404(request):
    return render(request, '404.html', status=404)

def myhandler500(request):
    return render(request, '500.html', status=500)