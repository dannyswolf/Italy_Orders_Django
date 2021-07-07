from django.contrib import admin

from warehouse import models as warehouse_models
from django.db.models.base import ModelBase

# https://www.protechtraining.com/blog/post/tutorial-using-djangos-multiple-database-support-477

for name, var in warehouse_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)


