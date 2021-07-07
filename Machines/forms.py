from django import forms
from datetime import datetime
from .models import Machines


class AddMachineForm(forms.ModelForm):
    class Meta:
        model = Machines
        fields = '__all__'

    model = forms.CharField(max_length=50, label="Εταιρία και Μοντέλο")


class EditMachineForm(forms.ModelForm):
    class Meta:
        model = Machines
        fields = '__all__'

    model = forms.CharField(required=True, label='Μοντέλο')
    prices_date = forms.CharField(help_text='Τελευταία ενημέρωση τιμών', required=False, label='Ημερομηνία Τιμών')
