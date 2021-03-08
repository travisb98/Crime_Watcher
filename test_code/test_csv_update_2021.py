
import pandas as pd
import csv
#### this code will update the 2021 csv

csvUrl2021 = 'https://opendata.arcgis.com/datasets/cb6a8b1d01b74feea5d3f96fa79bb6bf_0.csv'

updated_df=pd.read_csv(csvUrl2021)

updated_df.to_csv('Police_Incidents_2021.csv', index=False)

