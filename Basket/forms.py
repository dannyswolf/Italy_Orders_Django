from django import forms
from .models import Basket


class EditBasketForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditBasketForm, self).__init__(*args, **kwargs)
        self.fields['spare_part'].widget.attrs['disabled'] = False

    class Meta:
        model = Basket
        # fields = '__all__'
        fields = ("spare_part", 'ml_code', "price", "pieces", "total")

    # machine = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    ml_code = forms.CharField(label='Κωδικός', required=False, disabled=True)
    # spare_part = forms.CharField(label='Ανταλλακτικό', required=True, disabled=True)
    price = forms.FloatField(label='Τιμή', required=False, disabled=True)
    pieces = forms.IntegerField(label='Τεμάχια', required=False)
    total = forms.FloatField(label='Σύνολο', required=False, disabled=True)

    def clean_total(self):
        total = self.cleaned_data.get('total')
        price = self.cleaned_data.get('price')
        pieces = self.cleaned_data.get('pieces')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        new_total = float(price * float(pieces))
        return str(new_total)


class AddSparePartFromHomeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddSparePartFromHomeForm, self).__init__(*args, **kwargs)
        self.fields['spare_part'].widget.attrs['disabled'] = False

    class Meta:
        model = Basket
        fields = '__all__'
        # fields = ("spare_part", 'ml_code', "price", "pieces", "total")

    # machine = forms.CharField(label='Μηχάνημα', required=True, disabled=True)
    ml_code = forms.CharField(label='Κωδικός', required=True, disabled=True)
    # spare_part = forms.CharField(label='Ανταλλακτικό', required=True, disabled=True)
    price = forms.FloatField(label='Τιμή', required=True, disabled=True)
    pieces = forms.IntegerField(label='Τεμάχια', required=True)
    total = forms.FloatField(label='Σύνολο', required=False, disabled=True)

    def clean_total(self):
        total = self.cleaned_data.get('total')
        price = self.cleaned_data.get('price')
        pieces = self.cleaned_data.get('pieces')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        new_total = float(price * float(pieces))
        return str(new_total)


