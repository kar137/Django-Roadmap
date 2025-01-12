from django import forms

class ProfileForm(forms.Form):      #inherits from forms class
    user_image = forms.FileField()        #setup form control for accepting files