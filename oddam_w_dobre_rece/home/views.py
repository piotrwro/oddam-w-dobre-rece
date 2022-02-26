from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class Index(View):
    def get(self, request):
        return render(request, "index.html")


class Form(View):
    def get(self, request):
        return render(request, "form.html")


class FormConf (View):
    def get(self, request):
        return render(request, "form-confirmation.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect('register')




class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get('email')
        first_name = request.POST.get('name')
        last_name = request.POST.get('surname')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if not username or not password or password != password2:
            ctx = {"text": "Uzupełnij pola"}
            return render(request, 'create_user.html', ctx)
        else:
            User.objects.create_user(username=username, email=None, password=password, first_name=first_name,
                                     last_name=last_name)
            return render(request, 'register.html', context={'email': username, 'password': password})

