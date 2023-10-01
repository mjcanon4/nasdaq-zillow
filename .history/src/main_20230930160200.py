import pandas as pd
import numpy as np
import requests as req

data = req.get(f"https://data.nasdaq.com/api/v3/datatables/ZILLOW/DATA?indicator_id=ZSFH&region_id=99999&api_key={api_key}")
print(data)