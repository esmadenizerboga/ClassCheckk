from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')  

def userlogin(request):
    username = '' 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('empty')
        else:
            messages.error(request, ' Incorrect Entry, Please Try Again..')

    return render(request, 'userlogin.html', {'username': username})

def empty(request):
    return render(request, 'empty.html') 

def home(request):
    return render(request, 'home.html')  
def userlogout(request):
    logout(request)  
    return redirect('index') 


