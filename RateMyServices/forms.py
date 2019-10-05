from django import forms

from .models import GeneralUser

class GeneralUserCreationForm(forms.Form):
    '''
    Assuming users behave, it works. Need to work on validations stuffs.
    '''
    
    first_name  = forms.CharField()
    last_name   = forms.CharField()
    email       = forms.EmailField(label='Email Address (you\'ll be using email to login)')
    #email2      = forms.EmailField(label='Confirm email')
    password    = forms.CharField(widget=forms.PasswordInput)
    #password2   = forms.CharField(widget=forms.PasswordInput)
    state       = forms.CharField(
                            widget=forms.TextInput(
                                attrs={"placeholder": "State"}
                                )
                            )
    city        = forms.CharField(
                            widget=forms.TextInput(
                                attrs={"placeholder": "City"}
                                )
                            )
    street      = forms.CharField(
                            widget=forms.TextInput(
                                attrs={"placeholder": "Street"}
                                )
                            )
    zips        = forms.CharField(
                            widget=forms.TextInput(
                                attrs={"placeholder": "Zip code"}
                                )
                            )
    phone       = forms.CharField()
    
    class Meta:
        model = GeneralUser
        fields = [
            'first_name',
            'last_name',
            'email',
            #'email2',
            'password',
            #'password2',
            'street',
            'city',
            'state',
            'zips',
            'phone'
        ]
    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("email must match")
    #     email_qs = GeneralUser.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError(
    #             "This email has been used"
    #         )
    #     return email