from django.contrib import admin

from .models import Orders
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class OrdersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['machine', 'date', 'spare_part', 'price', 'pieces', 'total']

    class Meta:
        model = Orders


admin.site.register(Orders, OrdersAdmin)
