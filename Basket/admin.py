from django.contrib import admin

from .models import Basket
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class BasketAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['machine', 'ml_code', 'spare_part', 'price', 'pieces', 'total']

    class Meta:
        model = Basket


admin.site.register(Basket, BasketAdmin)
