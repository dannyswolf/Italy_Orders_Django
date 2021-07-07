from django.db import models
from django.shortcuts import reverse
import os


# Create your models here.
class BROTHER(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BROTHER'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_brother', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:brother_delete_product', kwargs={'spare_part_id': self.pk})


class CANON(models.Model):
    ID = models.AutoField(db_column='id', primary_key=True, blank=True, null=False)
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CANON'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_canon', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:canon_delete_product', kwargs={'spare_part_id': self.pk})


class EPSON(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EPSON'

    def __str__(self):
        return f"PARTS_NR :{self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_epson', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:epson_delete_product', kwargs={'spare_part_id': self.pk})


class KONICA(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KONICA'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_konica', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:konica_delete_product', kwargs={'spare_part_id': self.pk})


class KYOCERA(models.Model):
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KYOCERA'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_kyocera', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:kyocera_delete_product', kwargs={'spare_part_id': self.pk})


class LEXMARK(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LEXMARK'

    def __str__(self):
        return f"PARTS_NR :{self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_lexmark', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:lexmark_delete_product', kwargs={'spare_part_id': self.pk})


class OKI(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OKI'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_oki', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:oki_delete_product', kwargs={'spare_part_id': self.pk})


class RICOH(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RICOH'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_ricoh', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:ricoh_delete_product', kwargs={'spare_part_id': self.pk})


class SAMSUNG(models.Model):
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)   # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SAMSUNG'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_samsung', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:samsung_delete_product', kwargs={'spare_part_id': self.pk})


class SHARP(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHARP'

    def __str__(self):
        return f'{self.PARTS_NR}   ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ}    Κωδικός: {self.ΚΩΔΙΚΟΣ}'

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_sharp', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:sharp_delete_product', kwargs={'spare_part_id': self.pk})

