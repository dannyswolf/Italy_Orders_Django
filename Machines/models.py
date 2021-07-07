# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


# Create your models here.
class Machines(models.Model):
    class Meta:
        db_table = 'machines'
        ordering = ['model']
        verbose_name_plural = 'Φωτοτυπικά'
        verbose_name = 'Φωτοτυπικό'

    Copier_ID = models.AutoField(primary_key=True, db_column='ID', blank=False, null=False)  # Field name made lowercase.
    model = models.CharField(max_length=30, unique=True, blank=False, null=False)
    prices_date = models.CharField(max_length=10, blank=True, null=True)

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('Machine:list_machines', kwargs={'Copier_ID': self.pk})

    def __str__(self):
        return f'{self.model}'

    def serialize(self):
        return {

            'ID': self.pk,
            'Copier_ID': self.Copier_ID,
            'model': self.model,
            'prices_date': self.prices_date
        }

