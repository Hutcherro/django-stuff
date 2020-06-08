from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('wrong password')
            if not user.is_active:
                raise forms.ValidationError('is not active')
        return super(UserLogin, self).clean(*args, **kwargs)

class UserRegister(forms.ModelForm):
    email = forms.CharField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = [
            'username',
            'password'
        ]

    #password = self.cleaned_data('password')
    
    def clean_email(self):
        email = self.cleaned_data('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('is being used')                
                
                
