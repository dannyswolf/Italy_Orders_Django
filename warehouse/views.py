# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import (BROTHER, CANON, EPSON, KONICA, KYOCERA, LEXMARK, OKI, RICOH, SAMSUNG, SHARP)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

import os
import shutil
from django.http import HttpResponseRedirect, JsonResponse


# Create your views here.
class BROTHERListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = BROTHER.objects.using('SparePartsDb').all()


class CANONListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = CANON.objects.using('SparePartsDb').all()


class EPSONListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = EPSON.objects.using('SparePartsDb').all()


class KONICAListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = KONICA.objects.using('SparePartsDb').all()


class KYOCERAListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = KYOCERA.objects.using('SparePartsDb').all()


class LEXMARKListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = LEXMARK.objects.using('SparePartsDb').all()


class OKIListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = OKI.objects.using('SparePartsDb').all()


class RICOHListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = RICOH.objects.using('SparePartsDb').all()


class SAMSUNGListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = SAMSUNG.objects.using('SparePartsDb').all()


class SHARPListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = SHARP.objects.using('SparePartsDb').all()

