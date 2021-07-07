from django.db import models
from django.urls import reverse
from Machines.models import Machines
from Spareparts.models import SpareParts


# Create your models here.
class Basket(models.Model):
    basket_id = models.AutoField(primary_key=True, db_column='ID', blank=False,
                                 null=False)  # Field name made lowercase.
    machine = models.ForeignKey(Machines, db_column='machine', blank=False, null=False, on_delete=models.PROTECT)
    ml_code = models.CharField(max_length=30, blank=True, null=True)
    spare_part = models.OneToOneField(SpareParts, db_column='spare_part', blank=False, null=False,
                                      on_delete=models.PROTECT)
    price = models.FloatField(blank=True, null=True)
    pieces = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'basket'
        ordering = ['machine']
        verbose_name_plural = 'Ανταλλακτικά'
        verbose_name = 'Ανταλλακτικό'

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('Orders:basket', kwargs={'basket_id': self.pk})

    def __str__(self):
        return f'{self.machine} {self.spare_part} {self.price} {self.pieces} {self.total}'
