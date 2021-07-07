from django import forms
from .models import SpareParts


class EditSparePartsForm(forms.ModelForm):
    class Meta:
        model = SpareParts
        fields = '__all__'
        #fields = ('ml_code', "spare_part", "price", "pieces", "total")

    # machine = forms.CharField(label="Μηχάνημα", disabled=True)
    part_nr = forms.CharField(label="Part No:", required=False)
    description = forms.CharField(label="Περιγραφή")
    ml_code = forms.CharField(label='<font color="orange"><b>Κωδικός</b></font>', required=False)
    ital_code = forms.CharField(label='<font color="blue"><b>Ιταλία Κωδικός</b></font>', required=False)
    ital_price = forms.CharField(label='<font color="blue"><b>Ιταλία Τιμή</b></font>', required=False)
    info_code = forms.CharField(label='<font color="#d3ea4f"><b>Info Κωδικός</b></font>', required=False)
    info_price = forms.CharField(label='<font color="#d3ea4f"><b>Info Τιμή</b></font>', required=False)
    info_site_code = forms.CharField(label='<font color="#d3ea4f"><b>Info-Site Κωδικός</b></font>', required=False)

    def clean_info_price(self):
        try:
            price = float(self.cleaned_data.get('info_price').replace(",", ".").replace("€", ""))
            new_price = f"{price:.2f}"
            final_price = new_price + " €"
            return str(final_price)
        except ValueError:  # Όταν ειναι κενό
            return self.cleaned_data.get('info_price')

    def clean_ital_price(self):
        try:
            price = float(self.cleaned_data.get('ital_price').replace(",", ".").replace("€", ""))
            new_price = f"{price:.2f}"
            final_price = new_price + " €"
            return str(final_price)
        except ValueError:  # # Όταν ειναι κενό
            return self.cleaned_data.get('ital_price')


class CreateSparePartForm(forms.ModelForm):
    class Meta:
        model = SpareParts
        fields = '__all__'

    part_nr = forms.CharField(label="Part No:", required=False)
    description = forms.CharField(label="Περιγραφή")
    ml_code = forms.CharField(label='<font color="orange"><b>Κωδικός</b></font>', required=False)
    ital_code = forms.CharField(label='<font color="blue"><b>Ιταλία Κωδικός</b></font>', required=False)
    ital_price = forms.CharField(label='<font color="blue"><b>Ιταλία Τιμή</b></font>', required=False)
    info_code = forms.CharField(label='<font color="#d3ea4f"><b>Info Κωδικός</b></font>', required=False)
    info_price = forms.CharField(label='<font color="#d3ea4f"><b>Info Τιμή</b></font>', required=False)
    info_site_code = forms.CharField(label='<font color="#d3ea4f"><b>Info-Site Κωδικός</b></font>', required=False)

