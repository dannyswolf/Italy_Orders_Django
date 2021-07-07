from django import forms
from .models import Orders


class EditOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditOrderForm, self).__init__(*args, **kwargs)
        self.fields['spare_part'].widget.attrs['disabled'] = False

    class Meta:
        model = Orders
        # fields = '__all__'
        fields = ("spare_part", "price", "pieces", "total")

    # machine = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    # spare_part = forms.CharField(label='Ανταλλακτικό', required=True, disabled=True)
    price = forms.FloatField(label='Τιμή', required=False)
    pieces = forms.IntegerField(label='Τεμάχια', required=False)
    total = forms.FloatField(label='Σύνολο', required=False, disabled=True)

    def clean_total(self):
        total = self.cleaned_data.get('total')
        price = self.cleaned_data.get('price')
        pieces = self.cleaned_data.get('pieces')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        new_total = float(price * float(pieces))
        return str(new_total)



