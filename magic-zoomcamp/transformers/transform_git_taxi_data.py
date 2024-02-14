import pandas as pd
import re


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print('Rows with zero passengers: ', data['passenger_count'].isin([0]).sum())
    print('Rows with zero distance: ', data['trip_distance'].isin([0.0]).sum())
    print("Before conversion:", data['lpep_pickup_datetime'].dtype)

    unique_vendor_ids = data['VendorID'].unique()
    # Print the unique VendorID values
    print("Unique VendorID values:", unique_vendor_ids)
    
    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
    print("After conversion:", data['lpep_pickup_datetime'].dtype)
    
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    def camel_to_snake(name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
    data.columns = [camel_to_snake(col) for col in data.columns]
    print(data.columns)

    # Apply parentheses around each condition
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]




@test
def test_output(output, *args):
    assert 'vendor_id' in output.columns, "'vendor_id' column is missing"
    assert output['vendor_id'].isnull().sum() == 0, "'vendor_id' contains null values"
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'