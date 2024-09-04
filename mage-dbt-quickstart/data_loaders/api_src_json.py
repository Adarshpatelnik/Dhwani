# import io
# import pandas as pd
# import requests
# if 'data_loader' not in globals():
#     from mage_ai.data_preparation.decorators import data_loader
# if 'test' not in globals():
#     from mage_ai.data_preparation.decorators import test
 
 
# @data_loader
# def load_data_from_api(*args, **kwargs):
#     """
#     Template for loading data from API
#     """
#     url = 'https://api.nationalize.io/?name=nathaniel'
#     response = requests.get(url)
#     data = response.json()  # Parse JSON response
 
#     # Convert JSON data to DataFrame
#     # Extract the 'country' list from the JSON data
#     df = pd.json_normalize(data['country'])
#     return df
 
 
# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
#     assert not output.empty, 'The output DataFrame is empty'
 
 
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
    Template for loading data from API
    """
    url = 'https://api.nationalize.io/?name=nathaniel'
    response = requests.get(url)
    data = response.json()  # Parse JSON response
 
    # Flatten the top-level data
    top_level_data = {
        'count': data['count'],
        'name': data['name']
    }
 
    # Flatten the 'country' list
    country_df = pd.json_normalize(data['country'])
 
    # Add the top-level data to each row of the country DataFrame
    for key, value in top_level_data.items():
        country_df[key] = value
 
    # Reorder columns if needed to have top-level data at the beginning
    columns_order = ['count', 'name'] + [col for col in country_df.columns if col not in top_level_data.keys()]
    country_df = country_df[columns_order]
 
    return country_df
 
 
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert not output.empty, 'The output DataFrame is empty'