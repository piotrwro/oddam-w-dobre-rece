from django.shortcuts import render
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


class Register(View):
    def get(self, request):
        return render(request, "register.html")
