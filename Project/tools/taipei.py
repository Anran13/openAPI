import requests
from io import StringIO
from csv import DictReader
from requests import RequestException, HTTPError
import streamlit as st

@st.cache_data # temporal data used
def get_youbikes()->list:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'
    try:
        r = requests.request('GET', url)
        r.raise_for_status()     

    # check: if the HTTP request returned an unsuccessful status code.
    except HTTPError as e:
        raise Exception("Server problem!")
    # check all: all exceptions
    except RequestException as e:
        raise Exception("Connection problem!")

    else:
        print("Download successfully!")
        file = StringIO(r.text)
        list_reader = list(DictReader(file))
        return list_reader