import math
from datetime import datetime
import pandas as pd


class OilPredictionModel:
    def __init__(self):
        pass

    @staticmethod
    def predict_data(initial_oil_reserves: float,
                     water_debt: int,
                     oil_accumulation_table,
                     oil_debit_table,
                     oil_stock_table):
        geo_model = OilGeoModel.count_model(oil_accumulation_table, oil_debit_table, oil_stock_table)
        predicted_model = {'data': []}
        date_list = pd.date_range('2021-01-01', '2026-02-01', freq='MS').tolist()
        oil_extraction_sum = 0
        for index, date in enumerate(date_list):
            try:
                date_delta = date_list[index + 1] - date
            except IndexError:
                continue

            nearest_obv = OilPredictionModel.get_nearest_obv((oil_extraction_sum / initial_oil_reserves), geo_model)
            oil_extraction = (int(date_delta.days) * water_debt) * (1 - nearest_obv)
            oil_extraction_sum += oil_extraction
            debit = oil_extraction / date_delta.days
            predicted_model['data'].append(
                {
                    'date': date.strftime("%d-%m-%Y"),
                    'oil_extraction': round(oil_extraction, 2),
                    'debit': round(debit, 2)
                }
            )

        return predicted_model

    @staticmethod
    def get_nearest_obv(value_to_search, geo_model):
        list = []
        list_out = []
        for index, element in enumerate(geo_model['data']):
            list.append(element['selection_oil_capacity'])
        # absolute_difference_function = lambda list_value: abs(list_value - value_to_search)
        closest_value_index = min(range(len(list)), key=lambda i: abs(list[i] - value_to_search))
        # closest_value_index = min(list, key=lambda i: list[i] - value_to_search)

        return geo_model['data'][closest_value_index]['OBV']


class OilGeoModel:
    def __init__(self):
        pass

    @staticmethod
    def count_model(oil_accumulation_table, oil_debit_table, oil_stock_table):
        geo_model = {'data': []}
        table_length = len(oil_accumulation_table)
        Npmax = oil_accumulation_table[table_length - 1].oil_accumulated
        for counter in range(1, len(oil_accumulation_table)):
            Np = int(oil_accumulation_table[counter].oil_accumulated)
            geo_model['data'].append(
                {
                    'Np': Np,
                    'current_water_factor': math.ceil(
                        oil_debit_table[counter].water_debit / oil_debit_table[counter].oil_debit),
                    'selection_oil_capacity': 0.00 if counter == 1 else Np / Npmax,
                    'OBV': oil_debit_table[counter].water_debit / oil_debit_table[counter].liquid_debit,
                    'bottomhole_formation_plane': oil_accumulation_table[counter].water_accumulated_upload / (
                                oil_stock_table[0].oil_stock_value * 1.39),
                    'oil_extraction_coeff': oil_accumulation_table[counter].oil_accumulated / oil_stock_table[
                        0].oil_stock_value
                }
            )
        return geo_model
