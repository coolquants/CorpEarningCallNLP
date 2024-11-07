
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

def get_daily_prices(ticker):
    return "notyet"


def read_pdf_as_corpus(pdf_path):
    """
    Define the function to read the PDF and extract text
    :param pdf_path: pdf file path
    :return: list of corpus for the pdf with each page as an object
    """
    import pandas as pd
    import fitz  # PyMuPDF
    corpus = []
    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        # Iterate over all pages
        for page_num in range(pdf.page_count):
            page = pdf.load_page(page_num)  # Load the page
            text = page.get_text()  # Extract text from the page
            corpus.append(text)  # Add page text to the corpus
    corpus = pd.DataFrame(corpus)
    corpus.to_parquet('Data/temp.parquet') #need to have dynamic name schedule