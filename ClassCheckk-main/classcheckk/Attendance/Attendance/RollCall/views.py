from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')  # Ana sayfa şablonunu render et

def userlogin(request):
    # Giriş işlemleri burada yapılacak (örneğin, form işleme)
    return render(request, 'login.html')  # Giriş sayfası şablonunu render et

def empty(request):
    return render(request, 'empty.html')  # Empty şablonunu render et

def home(request):
    return render(request, 'home.html')  # Empty şablonunu render et

def userlogout(request):
    logout(request)  # Kullanıcıyı çıkış yaptır
    return redirect('index') 


