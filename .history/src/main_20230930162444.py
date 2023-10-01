import pandas as pd
import numpy as np
import quandl

# quandl.read_key()
data = quandl.get_table('ZILLOW/DATA', indicator_id='ZSFH', region_id='99999')
print(data)
