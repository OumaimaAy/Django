# memberships/forms.py
from django import forms
from .models import Membership

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['membership_type', 'start_date', 'end_date']  # Include the correct fields here
