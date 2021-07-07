from django.contrib import admin

from .models import SpareParts
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class SparePartsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['Μηχάνημα', 'part_nr', 'description', 'ml_code', 'ital_code', 'ital_price', 'info_code',
                    'info_site_code', 'info_price']

    class Meta:
        model = SpareParts


admin.site.register(SpareParts, SparePartsAdmin)
