import csv
import requests
import matplotlib as plt
import pandas as pd
import datetime
import numpy as np


CSV_URL = 'http://api.covid19india.org/csv/latest/vaccine_doses_statewise_v2.csv'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    # for row in my_list:
    #     print(row)

df = pd.DataFrame(my_list)     
df.drop(index=df.index[0], 
        axis=0, 
        inplace=True)
df.columns =    ['date','state','first_dose','second_dose','Total']
df['date'] = df['date'].apply(lambda x: datetime.datetime.strptime(x,'%d/%m/%Y'))

df.set_index('date',drop=True,inplace=True)
print(df)


states = pd.DataFrame(df['state'].unique())
states.columns = ['state']
'Print Vaccine Data'

df.first_dose = df['first_dose'].apply(lambda x: int(x))
df.second_dose = df['first_dose'].apply(lambda x: int(x))
df.second_dose = df['Total'].apply(lambda x: int(x))

for state in states['state']:

    df[df['state'] ==state][['first_dose','second_dose','Total']].plot(title=state + ' : Vaccine Data')
    
