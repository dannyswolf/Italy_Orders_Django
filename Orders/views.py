from .models import Orders
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import EditOrderForm

# Create your views here.
class OrdersListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    # model = Orders
    template_name = 'Orders/orders.html'
    queryset = Orders.objects.all()

    fields = '__all__'


class OrdersEdit(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # services = forms.ModelChoiceField(queryset=Services.objects.all())
    model = Orders
    form_class = EditOrderForm
    template_name = 'Orders/detail.html'
    success_url = reverse_lazy('Orders:orders')

    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, ):
        id_ = self.kwargs.get("order_id")  # apo to urls.py -->> path('<int:machine_id>'....
        return get_object_or_404(Orders, pk=id_, )


class OrderDelete(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = Orders
    template_name = 'Orders/confirm_delete.html'
    success_url = reverse_lazy('Orders:orders')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("order_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Orders, pk=id_)