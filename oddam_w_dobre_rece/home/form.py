from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from home.models import Donation

class RegistrationUser(UserCreationForm):
    class Meta:
        model = User
        fields =('username', 'password', 'password2', 'first_name', 'last_name')


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'