
from django.forms import ModelForm

from home.models import Donation




class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ('quantity', 'categories', 'institution', 'phone_number', 'city','zip_code',
                  'pick_up_date', 'pick_up_time', 'pick_up_comment', 'user')