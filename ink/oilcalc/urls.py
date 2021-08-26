from django.urls import path

from .views import OilModelView

app_name = 'oilcalc'

urlpatterns = [
    path('oil-model-calc/', OilModelView.as_view())
]