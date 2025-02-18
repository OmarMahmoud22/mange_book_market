from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserResitrationForm(forms.ModelForm):
    password = forms.CharField(label= 'password' , widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repete password' , widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'email']

    def clean_password2(self):
            cd  = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('passwords dont match.')
            return cd['password2']
                
    def clean_email(self):
         data = self.cleaned_data['email']
        
         if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already exists.')
         return data
        
            

class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        
        if qs.exists():
            raise forms.ValidationError('This email address is already in use.')
        
        return data
    





class ProfielEditForm(forms.ModelForm)        :
    class Meta:
        model = Profile
        fields = ['date_of_birth' , 'image']


    
