from django import forms


class DateFilter(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker form-control',
                                                               'placeholder': 'с даты'}),
                                 input_formats=('%d.%m.%Y', '%Y-%m-%d'), required=False)
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker form-control',
                                                             'placeholder': 'по дату'}),
                               input_formats=('%d.%m.%Y', '%Y-%m-%d'), required=False)

class AddKeysForm(forms.Form):
    key_file = forms.FileField(label='', widget=forms.ClearableFileInput(attrs={'required': True}))