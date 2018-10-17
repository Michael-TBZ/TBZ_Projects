# Locate unique dates in CSV and put them in seperate files.

import pandas as pd

df = pd.read_csv('testfile.txt', sep='\t')
[df.loc[df['Datum'] == date].to_csv('data_' + str(date) + '.csv', sep='\t') for date in df.Datum.unique()]


