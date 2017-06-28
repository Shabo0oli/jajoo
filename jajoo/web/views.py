from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout

# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


@csrf_exempt
def login(request):
    context = {}
    return render(request, 'index.html', context)


def register(request):
    context = {}
    return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    context = {}
    return render(request, 'index.html', context)
