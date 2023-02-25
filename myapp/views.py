from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import SignUpForm, EditUser
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash

# Create your views here.
class SignUp(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = SignUpForm()
            return render (request, 'myapp/signup.html', {'form':form})
        else:
            return redirect ('/profile/')
    def post(self, request):
        if not request.user.is_authenticated:
            form = SignUpForm(data=request.POST)
            if form.is_valid:
                form.save()
                form = SignUpForm()
                messages.success(request, 'User Created')
                return render (request, 'myapp/signup.html', {'form':form})
            else:
                form = SignUpForm()
                return render (request, 'myapp/signup.html', {'form':form})
        else:
            return redirect ('/profile/')


class UserLogin(View):
        def get(self, request):
            if not request.user.is_authenticated:
                form = AuthenticationForm()
                return render(request, 'myapp/login.html', {'form':form})
            else:
                return redirect ('/profile/')
        def post(self, request):
            if not request.user.is_authenticated:
                form = AuthenticationForm(request=request, data=request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/profile/')
                    else:
                        form = AuthenticationForm()
                        return render(request, 'myapp/login.html', {'form':form})
                else:
                    return redirect('/login/')

            else:
                return redirect ('/profile/')


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')

  
class MyProfile(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = EditUser(instance=request.user)
            return render(request, 'myapp/profile.html', {'name':request.user.first_name, 'form':form})
        else:
            return redirect ('/login/')
    def post(self, request):
        if request.user.is_authenticated:
            form = EditUser(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'User Profile Updated')
                return render(request, 'myapp/profile.html', {'name':request.user.first_name, 'form':form})
        else:
            return redirect ('/login/')


class ChangePass(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = PasswordChangeForm(user=request.user)
            return render(request, 'myapp/changepass.html', {'form':form})
        else:
            return redirect ('/login/')
    def post(self, request):
        if request.user.is_authenticated:
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Has Changed Successfully')
                update_session_auth_hash(request, form.user)
                return redirect ('/profile/')
        else:
            return redirect ('/login/')

