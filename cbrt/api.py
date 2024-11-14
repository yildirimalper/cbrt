# cbrt/api.py
import pandas as pd
from .config import get_api_key

def fetch_data(data_group):
    """
    Fetches data from the CBRT API based on the specified data group.
    
    Parameters:
    - data_group (str): The data group ID from CBRT (e.g., "TP.DK.USD.S")

    Returns:
    - pd.DataFrame: DataFrame containing the requested data.
    """
    api_key = get_api_key()
    url = f"https://evds2.tcmb.gov.tr/service/evds/datagroups/key={api_key}&mode=0&type=csv"
    url += f"&data_group={data_group}"
    df = pd.read_csv(url)
    return df
