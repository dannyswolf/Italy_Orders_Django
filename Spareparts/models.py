from django.db import models
from django.urls import reverse
from Machines.models import Machines


# Create your models here.
class SpareParts(models.Model):
    spare_part_id = models.AutoField(primary_key=True, db_column='ID', blank=False, null=False)  # Field name made lowercase.
    Μηχάνημα = models.ForeignKey(Machines, db_column='machine', blank=False, null=False, on_delete=models.PROTECT)
    part_nr = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=50, blank=False, null=False)
    ml_code = models.CharField(max_length=30, blank=True, null=True)
    ital_code = models.CharField(max_length=30, blank=True, null=True)
    ital_price = models.CharField(max_length=30, blank=True, null=True)
    info_code = models.CharField(max_length=30, blank=True, null=True)
    info_site_code = models.CharField(max_length=30, blank=True, null=True)
    info_price = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'spare_parts'
        ordering = ['Μηχάνημα']
        verbose_name_plural = 'Ανταλλακτικά'
        verbose_name = 'Ανταλλακτικό'

    def get_absolute_url(self):
        # Spareparts ==>> app name στο urls
        return reverse('Spareparts:list_spareparts', kwargs={'spare_part_id': self.pk})

    def __str__(self):
        return f'{self.Μηχάνημα} {self.description}'
