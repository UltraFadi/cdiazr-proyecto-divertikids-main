from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"core/index.html")



def productos(request):
    return render(request, "core/productos.html")

@login_required
def carrito(request):
    return render(request, "core/carrito.html")
