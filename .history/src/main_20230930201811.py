import pandas as pd
import numpy as np
import quandl
import logging
import csv

houston_zip = [77002, 77021, 77040, 77059, 77078, 77098, 77384, 77479, 77547,
               77003, 77022, 77041, 77060, 77079, 77099, 77385, 77484, 77571,
               77004, 77023, 77042, 77061, 77080, 77204, 77386, 77489, 77573,
               77005, 77024, 77043, 77062, 77081, 77325, 77388, 77492, 77574,
               77006, 77025, 77044, 77063, 77082, 77336, 77389, 77493, 77578,
               77007, 77026, 77045, 77064, 77083, 77338, 77396, 77494, 77581,
               77008, 77027, 77046, 77065, 77084, 77339, 77401, 77497, 77584,
               77009, 77028, 77047, 77066, 77085, 77345, 77406, 77498, 77586,
               77010, 77029, 77048, 77067, 77086, 77346, 77407, 77502, 77587,
               77011, 77030, 77049, 77068, 77087, 77354, 77429, 77503, 77588,
               77012, 77031, 77050, 77069, 77088, 77357, 77433, 77504, 77598,
               77013, 77032, 77051, 77070, 77089, 77365, 77447, 77505,
               77014, 77033, 77052, 77071, 77090, 77373, 77449, 77506,
               77015, 77034, 77053, 77072, 77091, 77375, 77450, 77507,
               77016, 77035, 77054, 77073, 77092, 77377, 77459, 77520,
               77017, 77036, 77055, 77074, 77093, 77379, 77469, 77530,
               77018, 77037, 77056, 77075, 77094, 77380, 77472, 77532,
               77019, 77038, 77057, 77076, 77095, 77381, 77477, 77536,
               77020, 77039, 77058, 77077, 77096, 77382, 77478, 77546]

quandl.read_key()

df = pd.DataFrame()
df = quandl.get_table('ZILLOW/DATA', indicator_id='ZSFH', region_id='77003')

# for zip in houston_zip:
#     df = quandl.get_table(
#         'ZILLOW/DATA', indicator_id='ZSFH', region_id=zip)
#     print(df)

print(df.columns)
print(df.index('region_id'))

# with open('77003.csv', 'w', newline='') as file:
#     csv.writer(file)
#     row_list = [[df.value]]
