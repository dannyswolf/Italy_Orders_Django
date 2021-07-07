from django.contrib import admin

from .models import Machines
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class MachinesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['model', 'prices_date']

    class Meta:
        model = Machines


admin.site.register(Machines, MachinesAdmin)
