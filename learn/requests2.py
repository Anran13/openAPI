# import requests
# from io import StringIO
# from csv import DictReader
# from requests import RequestException, HTTPError

# url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'
# # url = 'https://data.tpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000' # error url


# # step1: request to api
# try:
#     r = requests.request('GET', url)
    
#     # step2: api response
#     # if r.status_code == 200:
#     #     print("Download successfully!")
#     #     # string to file object
#     #     file = StringIO(r.text)
#     #     list_reader = list(DictReader(file))
#     # else:
#     #     print("Error!")
#     r.raise_for_status()
    

# # check: if the HTTP request returned an unsuccessful status code.
# except HTTPError as e:
#     print(e)
# # check all: all exceptions
# except RequestException as e:
#     print(e)

# else:
#     print("Download successfully!")
#     file = StringIO(r.text)
#     list_reader = list(DictReader(file))
#     print(list_reader)

from tools import taipei

try:
    youbikes = taipei.get_youbikes()
except Exception as e:
    print(e)
else:
    print(youbikes)
