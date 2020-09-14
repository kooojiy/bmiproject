from django import forms

class BmiForm(forms.Form):
    height = forms.IntegerField(label = '身長')
    weight = forms.IntegerField(label='体重')
    