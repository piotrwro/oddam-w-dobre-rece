
from django.forms import ModelForm

from home.models import Donation




class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'