from .models import Basket
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EditBasketForm, AddSparePartFromHomeForm
from django.contrib.auth.decorators import login_required
from Spareparts.models import SpareParts
from django.http import HttpResponseRedirect, JsonResponse, Http404
from Orders.models import Orders
from datetime import datetime


# Create your views here.
class BasketListView(LoginRequiredMixin, ListView):
    model = Basket
    template_name = 'Basket/basket.html'
    success_url = reverse_lazy("Basket")

    def get_context_data(self, **kwargs):
        context = super(BasketListView, self).get_context_data(**kwargs)
        all_objs = Basket.objects.all()
        sum_total = 0
        for obj in all_objs:
            sum_total += float(obj.total)
        context['sum_total'] = "{:.2f}".format(float(sum_total))
        return context


class EditBasket(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # services = forms.ModelChoiceField(queryset=Services.objects.all())
    model = Basket
    form_class = EditBasketForm
    template_name = 'Basket/detail.html'
    success_url = reverse_lazy('Basket:basket')

    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, ):
        id_ = self.kwargs.get("basket_id")  # apo to urls.py -->> path('<int:machine_id>'....
        return get_object_or_404(Basket, pk=id_, )


class BasketDelete(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = Basket
    template_name = 'Basket/confirm_delete.html'
    success_url = reverse_lazy('Basket:basket')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("basket_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Basket, pk=id_)


@login_required()
def create_basket(request, spare_part_id, **kwargs):
    spare_part = SpareParts.objects.all().filter(pk=spare_part_id)
    machine = spare_part[0].Μηχάνημα
    initial_data = {
        'spare_part': spare_part[0],
        'machine': machine,
        'ml_code': spare_part[0].ml_code,
        'price': str(spare_part[0].ital_price).replace(" €", "")
    }

    success_url = reverse_lazy('Basket')
    form = AddSparePartFromHomeForm(request.POST or None, initial=initial_data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('../', )
    context = {
        'form': form,
    }
    return render(request, 'Basket/create.html', context)


@login_required()
def make_order(request, **kwargs):
    if request.method == 'POST':
        today = datetime.today().strftime("%d.%m.%Y")
        basket_items = Basket.objects.all()
        for item in basket_items:
            order_item = Orders(machine=item.machine, date=today, spare_part=item.spare_part,
                                price=item.price, pieces=item.pieces, total=item.total)
            order_item.save()
            item.delete()
        return HttpResponseRedirect('../Orders/', )
    return HttpResponseRedirect('/Basket/', )


@login_required()
def java_script_add_to_basket(request, *args, **kwargs):
    # Javascript
    if request.is_ajax():
        spare_part_id = int(request.POST.get('somedata[spare_part_id]'))
        pieces = request.POST.get('somedata[pieces]')
        spare_part_objs = SpareParts.objects.all().filter(pk=spare_part_id)
        spare_part = spare_part_objs[0]
        price = spare_part.ital_price.replace(" €", "")

        sum_total = "{:.2f}".format(float(price) * float(pieces))

        # Αν  υπάρχει στο καλάθι
        if Basket.objects.filter(spare_part=spare_part).exists():
            json_response = {
                'status': 302  # 302 Found https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302
            }
            return JsonResponse(json_response)
        else:
            new_obj = Basket(machine=spare_part.Μηχάνημα, spare_part=spare_part_objs[0], price=price, pieces=pieces,
                                                            total=sum_total, ml_code=spare_part.ml_code)
            new_obj.save()
            json_response = {
                'status': 201
            }
            return JsonResponse(json_response)

    if request.method == "GET":
        raise Http404()
