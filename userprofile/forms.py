from django import forms
from django.contrib.auth.models import User
from .models import UserBio,PatnertBio

class UserBioForm(forms.ModelForm):

    class Meta():
        model = UserBio
        fields = '__all__'
        exclude = ('user',)
        widgets = {
               'education': forms.RadioSelect(),
               'nationality': forms.RadioSelect(),
               'religion': forms.RadioSelect(),
               'skin_complexity': forms.RadioSelect(),
               'eye_color': forms.RadioSelect(),
               'occupation': forms.RadioSelect(),
        }


class PatnertBioForm(forms.ModelForm):
    class Meta():
        model = PatnertBio
        fields = '__all__'
        exclude = ('user',)
        widgets = {
               'education': forms.RadioSelect(),
               'nationality': forms.RadioSelect(),
               'religion': forms.RadioSelect(),
               'skin_complexity': forms.RadioSelect(),
               'eye_color': forms.RadioSelect(),
               'occupation': forms.RadioSelect(),
        }

