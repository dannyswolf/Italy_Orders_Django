from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Machines
from .forms import AddMachineForm, EditMachineForm
from Spareparts.models import SpareParts

""" ------------------------ GET PRICES ----------------------"""
from .tasks import get_ital_price, get_info_price
from django.contrib.auth.decorators import login_required
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from django.conf import settings
import yaml
from yaml import CLoader as Loader


class MachinesListView(LoginRequiredMixin, ListView):
    model = Machines
    template_name = 'Machines/list_view.html'
    success_url = reverse_lazy("Spareparts")


class CreateMachine(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    form_class = AddMachineForm
    # model = Machines
    # fields = '__all__'
    template_name = 'Machines/create.html'

    def get_success_url(self):
        return reverse_lazy('Machines:edit_machine', args=(self.object.pk,))


class EditMachine(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # services = forms.ModelChoiceField(queryset=Services.objects.all())
    model = Machines
    form_class = EditMachineForm
    template_name = 'Machines/detail.html'
    success_url = reverse_lazy('Machines:machines')

    def get_object(self, ):
        id_ = self.kwargs.get("machine_id")  # apo to urls.py -->> path('<int:machine_id>'....
        return get_object_or_404(Machines, Copier_ID=id_, )

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("machine_id")
        context = super(EditMachine, self).get_context_data(**kwargs)
        context['spare_parts'] = SpareParts.objects.filter(Μηχάνημα=id_).order_by(
            "description")  # whatever you would like
        context['machine_id'] = id_
        return context


class MachineDelete(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = Machines
    template_name = 'Machines/confirm_delete.html'
    success_url = reverse_lazy('Machines:machines')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("machine_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Machines, pk=id_)


""" ------------------------ GET ITALY PRICES ----------------------"""

with open(settings.CREDENTIALS, "r", encoding='utf8') as cred:
    cred_obj = yaml.load(cred, Loader=Loader)

ital_login_url = cred_obj["ital_login_url"]["url"]
ital_payload = cred_obj['ital_payload']

ital_session = requests.Session()
# headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) "
#                          "Chrome/81.0.4044.141 Safari/537.36"}
retry = Retry(connect=3)
adapter = HTTPAdapter(max_retries=retry)
ital_session.mount('http://', adapter)
ital_session.mount('https://', adapter)


@login_required()
def get_ital_price_view(request, machine_id):
    if request.method == "GET":
        machine = Machines.objects.get(pk=machine_id)
        # print("machine_id", machine_id)
        spare_parts = SpareParts.objects.filter(Μηχάνημα=machine)
        form = EditMachineForm(instance=machine)
        result = get_ital_price.delay(machine_id)
        context = {'task_id': result.task_id,
                   'form': form,
                   'spare_parts': spare_parts}
        return render(request, 'Machines/detail.html', context)


@login_required()
def get_info_price_view(request, machine_id):
    if request.method == "GET":
        machine = Machines.objects.get(pk=machine_id)
        # print("machine_id", machine_id)
        spare_parts = SpareParts.objects.filter(Μηχάνημα=machine)
        form = EditMachineForm(instance=machine)
        result = get_info_price.delay(machine_id)
        context = {'task_id': result.task_id,
                   'form': form,
                   'spare_parts': spare_parts}
        return render(request, 'Machines/detail.html', context)