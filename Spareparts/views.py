from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import SpareParts
from .forms import EditSparePartsForm, CreateSparePartForm


class SparepartsView(LoginRequiredMixin, ListView):
    model = SpareParts
    template_name = 'Spareparts/list_view.html'
    success_url = reverse_lazy("Spareparts")


class EditSpareParts(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # services = forms.ModelChoiceField(queryset=Services.objects.all())
    model = SpareParts
    form_class = EditSparePartsForm
    template_name = 'Spareparts/detail.html'
    success_url = reverse_lazy('Spareparts:list_spare_parts')

    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, ):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:machine_id>'....
        return get_object_or_404(SpareParts, pk=id_, )


class CreateSparepart(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    form_class = CreateSparePartForm
    model = SpareParts
    # fields = '__all__'
    template_name = 'Spareparts/create.html'

    def get_success_url(self):
        return reverse_lazy('Spareparts:edit_sparepart', args=(self.object.pk,))


class DeleteSparePart(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = SpareParts
    template_name = 'Spareparts/confirm_delete.html'
    success_url = reverse_lazy('Spareparts:list_spare_parts')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(SpareParts, pk=id_)


