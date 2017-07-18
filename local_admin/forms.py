from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from loads.models import KeyOwner, Cistern


class AddSystemUserForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'required': True, 'maxlength': 30}),
                                 max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'required': True, 'maxlength': 30}),
                                max_length=30)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True}))


class EditDjangoUserForm(ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email'}
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'})}


class EditKeyOwnerForm(ModelForm):
    class Meta:
        model = KeyOwner
        fields = {'name', 'car', 'keys', 'comment'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 40}),
                   'car': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 40}),
                   'keys': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 16}),
                   'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50})}


class CisternForm(ModelForm):
    class Meta:
        model = Cistern
        fields = {'start_volume', 'max_volume', 'cistern_type'}
        widgets = {'start_volume': forms.NumberInput(attrs={'class': 'form-control'}),
                   'max_volume': forms.NumberInput(attrs={'class': 'form-control'}),
                   'cistern_type': forms.Select(attrs={'class': 'form-control'})}


class AddUpDosedForm(forms.Form):
    volume = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
                                max_digits=7, decimal_places=2, min_value=0.0)
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
