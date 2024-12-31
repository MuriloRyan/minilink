from django import forms

class UserSignInForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email must be from the domain @example.com')
        return email

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')

        if name and password:
            if name.lower() == password.lower():
                raise forms.ValidationError('Name and password cannot be the same.')

        return cleaned_data


class UserLogInForm(forms.Form):
    #password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(max_length=128)
    #email = forms.EmailField()
    email = forms.CharField(max_length=128)


