import pandas as pd
import requests

try:
    # Define the URL of the CSV file
    url = "https://api.mockaroo.com/api/2066ab40?count=1000&key=8bf92810"
    
    # Use requests to get the data with proper headers
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/csv'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes
    
    # Read the CSV data from the response content
    df = pd.read_csv(pd.io.common.StringIO(response.text))
    
    # Display the DataFrame
    print(df)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    # Alternative: Use a public dataset
    public_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
    print(f"\nTrying alternative public dataset from: {public_url}")
    df = pd.read_csv(public_url)
    print(df)