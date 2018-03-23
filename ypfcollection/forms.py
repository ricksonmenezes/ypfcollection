from django import forms

class Team(forms.Form):
    playing =  forms.BooleanField(required=False)