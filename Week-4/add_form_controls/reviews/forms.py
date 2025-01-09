from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField()      #creates a input field but will not impact the database
    