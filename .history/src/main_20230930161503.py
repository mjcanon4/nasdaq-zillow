import pandas as pd
import numpy as np
import requests as req
import quandl

api_key = 'vsWryznSzB9MQFg5X-ug'

data = quandl.get(
    f"https://data.nasdaq.com/api/v3/datatables/ZILLOW/DATA?state=Texas&county=Harris&api_key={api_key}")
print(data)
