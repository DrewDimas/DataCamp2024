import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load data without assuming knowledge of its contents or schema.
    """
    # Adjust these URLs to the direct download links for each relevant dataset
    urls = [
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    ]
    
    df_list = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            # Load the data without specifying dtype or parse_dates
            #parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
            df = pd.read_csv(io.BytesIO(response.content), compression='gzip')
            df_list.append(df)
        else:
            print(f'Failed to download {url}')

    if df_list:
        combined_df = pd.concat(df_list, ignore_index=True)
    else:
        return None  # Or handle the error as preferred

    return combined_df

@test
def test_output(output, *args) -> None:
    """
    Test to ensure data loading is successful and not empty.
    """
    assert output is not None and not output.empty, 'The output is undefined or empty'
