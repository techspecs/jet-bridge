from jet_bridge.models import data_types

from sqlalchemy.sql import sqltypes

map_data_types = [
    {'query': sqltypes.VARCHAR, 'date_type': data_types.TEXT},
    {'query': sqltypes.TEXT, 'date_type': data_types.TEXT},
    {'query': sqltypes.BOOLEAN, 'date_type': data_types.BOOLEAN},
    {'query': sqltypes.INTEGER, 'date_type': data_types.INTEGER},
    {'query': sqltypes.SMALLINT, 'date_type': data_types.INTEGER},
    {'query': sqltypes.NUMERIC, 'date_type': data_types.FLOAT},
    {'query': sqltypes.DATETIME, 'date_type': data_types.DATE_TIME},
    {'query': sqltypes.TIMESTAMP, 'date_type': data_types.DATE_TIME},
]
default_data_type = data_types.TEXT


def map_data_type(value):
    for rule in map_data_types:
        if isinstance(value, rule['query']):
            return rule['date_type']
    return default_data_type
