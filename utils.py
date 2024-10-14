import pandas as pd
import io

def get_sp500_tickers(url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"):
    """
    This function gets S&P 500 tickers from Wikipeadia
    :param url: wikipeadia sp500 webpage as default
    :return: dataframe of the sp500 table
    """
    import requests

    # Disable SSL verification warnings for Wikipedia
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    # Fetch the content without verifying the SSL certificate
    response = requests.get(f"{url}", verify=False)

    # Read the content as a CSV file with pandas
    ticker_df = pd.read_html(io.StringIO(response.text))[0]
    return ticker_df