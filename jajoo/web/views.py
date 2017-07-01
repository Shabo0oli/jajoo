from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import UserInfo, Place

# Create your views here.


def index(request):
    allplace = Place.objects.all()
    context = {}
    context['places'] = allplace
    return render(request, 'index.html', context)


@csrf_exempt
def login_view(request):
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            usrInfo = UserInfo.objects.filter(Username=user)

            context = {}
            context['avatar'] = usrInfo[0].Avatar.url[4:]
            allplace = Place.objects.all()
            context['places'] = allplace
            return render(request, 'index.html', context)
        else:
            context = {}
            context['message'] ='نام کاربری یا پسورد وارد شده اشتباه میباشد'
            return render(request, 'login.html', context)
    else:
        context = {}
        return render(request, 'login.html', context)



def register(request):
    if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
        if User.objects.filter(email=request.POST['email']).exists() or User.objects.filter(username=request.POST['username']).exists():
            context = {}
            context['message']='مشخصات وارد شده تکراری میباشد'
            return render(request, 'register.html', context)
        else:
            username = request.POST['username']
            password = request.POST['password']
            phone = request.POST['phone']
            email = request.POST['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            info = UserInfo(Username=user, Phone=phone)
            info.save()
            context = {}
            return redirect('/')
    else:
        context = {}
        return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def place(request , placeid):
    thisplace = Place.objects.get(id=placeid)
    context = {}
    context['place'] = thisplace
    return render(request, 'place.html', context)
