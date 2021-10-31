from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password=forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')
        

    '''def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )'''

    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        # gender = forms.ChoiceField(,widget=forms.RadioSelect)
        fields = ('nic','gender','rel_stats','address','phone_number','about')
        widgets = {
               'gender': forms.RadioSelect(),
               'rel_stats': forms.RadioSelect(),
        }
        labels = {
            'rel_stats': 'Relationship Status',
        }
    # def __init__(self, *args, **kwargs):
    #     super(UserProfileForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
