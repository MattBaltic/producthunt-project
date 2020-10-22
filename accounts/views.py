from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        #user nas info and want accounts
        if request.POST['password1'] == request.POST['password2']: #check if password equals Confirm password1
            try:
                user =  User.object.get(username=request.POST['username']) #checks if password is assign to already created username
                return render(request, 'accounts/signup.html', {'error': 'Username already exist'})
            except User.DoesNotExist: #craeting new user after skipping first bit of code
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')

            else:
                #user wants to enter info
                return render(request, 'accounts/signup.html')


    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #TODO need to route to home page
    #don't forget to logout
    return render(request, 'accounts/signup.html')
