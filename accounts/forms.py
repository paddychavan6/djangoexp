from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from accounts.models import Account,logimage
from django.contrib.auth import authenticate

class registrationform(UserCreationForm):
    email=forms.EmailField(max_length=60,help_text="req")


    class Meta:
        model=Account
        fields=("email","username","firstname","lastname","mobno","voterID","address","zipcode","age","password1","password2","image")
        
    def __init__(self, *args, **kwargs):
        super(registrationform, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-textbox'
        self.fields['username'].widget.attrs['class'] = 'form-textbox'
        self.fields['firstname'].widget.attrs['class'] = 'form-textbox'
        self.fields['lastname'].widget.attrs['class'] = 'form-textbox'
        self.fields['mobno'].widget.attrs['class'] = 'form-textbox'
        self.fields['voterID'].widget.attrs['class'] = 'form-textbox'
        self.fields['address'].widget.attrs['class'] = 'form-textbox'
        self.fields['zipcode'].widget.attrs['class'] = 'form-textbox'
        self.fields['age'].widget.attrs['class'] = 'form-textbox'
        self.fields['password1'].widget.attrs['class'] = 'form-textbox'
        self.fields['password2'].widget.attrs['class'] = 'form-textbox'

        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['firstname'].widget.attrs['id'] = 'firstname'
        self.fields['lastname'].widget.attrs['id'] = 'lastname'
        self.fields['mobno'].widget.attrs['id'] = 'mobno'
        self.fields['voterID'].widget.attrs['id'] = 'voterid'
        self.fields['address'].widget.attrs['id'] = 'address'
        self.fields['zipcode'].widget.attrs['id'] = 'zipcode'
        self.fields['age'].widget.attrs['id'] = 'age'
        self.fields['password1'].widget.attrs['id'] = 'password1'
        self.fields['password2'].widget.attrs['id'] = 'password2'


class AccountAuthenticationForm(forms.ModelForm):
    password=forms.CharField(label="password",widget=forms.PasswordInput)

    class Meta:
        model=Account
        fields=('email','password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid Login")

class accountupdateform(forms.ModelForm):
    class Meta:
        model=Account
        fields=("email","username","firstname","lastname","mobno","voterID","address","zipcode","age","image")

    def clean_email(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            try:
                account=Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is Already in use.' %account.email)

    def clean_username(self):
        if self.is_valid():
            username=self.cleaned_data['username']
            try:
                account=Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is Already in use.' %account.username)


class logfor(forms.ModelForm):
    class Meta:
        model=logimage
        fields=['vid','limage']

    def __init__(self, *args, **kwargs):
        super(logfor, self).__init__(*args, **kwargs)
        self.fields['vid'].widget.attrs['id'] = 'vid'
        self.fields['vid'].widget.attrs['name'] = 'vidname'    



NUMS= [
    ('bjp', 'bjp'),
    ('mns', 'mns'),
    ('congress', 'congress'),
    ]
class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))

