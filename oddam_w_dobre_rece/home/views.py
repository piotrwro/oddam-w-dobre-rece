from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from home.models import Institution, Category, Donation

from home.form import DonationForm



class Index(View):
    def get(self, request):



        inst1 = Institution.objects.filter(type=1)
        inst2 = Institution.objects.filter(type=2)
        inst3 = Institution.objects.filter(type=3)


        donations = Donation.objects.all()
        inst_don = len(donations)
        don_quantity=[]
        for donation in donations:
            don_quantity.append(int(donation.quantity))
            sum_quantity = sum(don_quantity)
        return render(request, 'index.html', context={"inst1": inst1, 'inst2': inst2, 'inst3': inst3,
                                                      'inst_don': inst_don, 'sum_quantity': sum_quantity })


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

            return render(request, 'register.html')
        else:
            User.objects.create_user(username=username, password=password, first_name=first_name,
                                     last_name=last_name)
        return render(request, 'register.html', context={'email': username, 'password': password})







class Userprofile(View):
    def get(self, request, ):
        donations = Donation.objects.all()

        return render(request, "userprofile.html", context={'donations': donations})


class Form(View):

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, "form.html", context={'categories': categories, 'institutions': institutions})

    def post(self, request):
        donation_form = DonationForm(request.POST)
        if donation_form.is_valid():
            donation_form.save()
            return redirect('form-confirmation')
        else:
            return redirect('form')



