from django import forms

class ProfileForm(forms.Form):      #inherits from forms class
    user_image = forms.ImageField()        #setup form control for accepting files---imagefield for retrieving only images and not