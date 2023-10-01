import pandas as pd
import numpy as np
import quandl
import zipcodes
import os

quandl.read_key()

city = 'New York City'
state = 'NY'

city_zipcodes = zipcodes.filter_by(city=city, state=state)
city_zips = []
for code in city_zipcodes:
    city_zips.append(code['zip_code'])

dir_exists = os.path.exists(f"{city}_{state}")
path = os.path.join(f"{city}_{state}")

if dir_exists:
    print('No need to create a new directory')
else:
    os.mkdir(path)

num_of_zips = len(city_zips)
print(f"There are {num_of_zips} zipcodes in {city}, {state}")

for zip in city_zips:

    zip = str(zip)

    df = pd.DataFrame()
    df = quandl.get_table('ZILLOW/DATA', indicator_id='ZSFH', region_id=zip)
    df.sort_values(by=['date'])
    df.to_csv(f"{city}_{state}/{zip}.csv", index=False, sep=',')
