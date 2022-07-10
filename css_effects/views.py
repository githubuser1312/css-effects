from django.shortcuts import render

def index(request):
    return render(request, 'product/index.html')


def buttonseffects(request):
    return render(request, 'product/buttonseffects.html')


def menuseffects(request):
    return render(request, 'product/menuseffects.html')


def specialeffects(request):
    return render(request, 'product/specialeffects.html')
