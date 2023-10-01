import pandas as pd
import numpy as np
import quandl

quandl.ApiConfig.api_key = 'vsWryznSzB9MQFg5X-ug'
quandl.get_table('ZILLOW/DATA', indicator_id='ZSFH', region_id='99999')
