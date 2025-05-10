from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='userlogin')
def empty(request):
   
    return render(request, 'empty.html') 

@login_required(login_url='userlogin')
def home(request):
    return render(request, 'home.html')  

def userlogout(request):
    logout(request)  
    return redirect('index') 

def password_reset_form(request):
    return render(request,'password_reset_form.html')

def password_reset_done(request):
    return render(request,'password_reset_done.html')

def password_reset_confirm(request):
     return render(request,' password_reset_confirm.html')

def password_reset_complete(request):
     return render(request,' password_reset_complete.html')





