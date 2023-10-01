import pandas as pd
import numpy as np
import quandl
import zipcodes
import os

city = 'Greensboro'
state = 'NC'

city_zipcodes = zipcodes.filter_by(city=city, state=state)
city_zips = []
for code in city_zipcodes:
    city_zips.append(code['zip_code'])

path = os.path.join(f"{city}_{state}")

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)

print(len(city_zips))

quandl.read_key()

# df = pd.DataFrame()
# df = quandl.get_table('ZILLOW/DATA', indicator_id='ZSFH', region_id='77007')

# print(df.columns)
# max_len = df.index.max()
# print(max_len)
# print(df)
# df.sort_values(by=['date'])

# df.to_csv('houston_files/77007.csv', index=False, sep=',')


for zip in city_zips:

    zip = str(zip)

    df = pd.DataFrame()
    df = quandl.get_table('ZILLOW/DATA', indicator_id='ZSFH', region_id=zip)
    df.sort_values(by=['date'])
    df.to_csv(f"{city}_{state}/{zip}.csv", index=False, sep=',')
