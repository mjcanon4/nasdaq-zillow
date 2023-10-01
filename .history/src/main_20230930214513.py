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

dir_exists = os.path.exists(f"{city}_{state}")
path = os.path.join(f"{city}_{state}")

if dir_exists:
    print('No need to create a new directory')
else:
    os.mkdir(path)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'

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
