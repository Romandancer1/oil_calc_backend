from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OilAccumulation,OilDebit,OilStock
from .serializers import OilAccumulationSerializer, OilDebitSerializer, OilStockSerializer
# Create your views here.
import json

from .OilModels import OilGeoModel, OilPredictionModel

class OilModelView(APIView):
    def get(self, request):
        oil_accumulation_table = OilAccumulation.objects.all()
        oil_debit_table = OilDebit.objects.all()
        oil_stock_table = OilStock.objects.all()
        data = OilPredictionModel.predict_data(float(request.GET.get('oilCoeff')), int(request.GET.get('debit')), oil_accumulation_table,
                                               oil_debit_table,
                                               oil_stock_table)


        return Response({'oil_table': data})
