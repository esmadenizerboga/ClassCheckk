from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')  # Ana sayfa şablonunu render et

def userlogin(request):
    username = ''  # username değişkenini baştan tanımlıyoruz

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('empty')
        else:
            messages.error(request, 'Username or Password are incorrect')

    return render(request, 'userlogin.html', {'username': username})
         # Giriş sayfası şablonunu render et


def empty(request):
    return render(request, 'empty.html')  # Empty şablonunu render et

def home(request):
    return render(request, 'home.html')  # Empty şablonunu render et

def userlogout(request):
    logout(request)  # Kullanıcıyı çıkış yaptır
    return redirect('index') 


