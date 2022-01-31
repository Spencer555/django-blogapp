from django import forms
from django.contrib.auth.models import User
from profiles.models import Profile

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email']


        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control rounded-4'}),

            'email': forms.EmailInput(attrs={'class':'form-control rounded-4'})
        }



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


        widgets ={
            'image':forms.FileInput(attrs={'class':'form-control rounded-4'}),

        }
        





