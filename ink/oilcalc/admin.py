from django.contrib import admin

from .models import OilStock, OilAccumulation, OilDebit

admin.site.register(OilStock)
admin.site.register(OilDebit)
admin.site.register(OilAccumulation)
# Register your models here.
