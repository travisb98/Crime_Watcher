##### this py file will call the api for the current and previous year, clean the data, and save all features for both years into a json file

import pandas as pd
import requests
import json
import datetime

### defind the current and previous year
current_year = datetime.datetime.now().year
last_year = current_year - 1


### function that calls api and returns the features for a given year
def callAndStore(year):
    url = f'https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Police_Incidents_{year}/FeatureServer/0/query?where=1%3D1&outFields=reportedDateTime,offense,description,centerLong,centerLat&outSR=4326&f=json'
    ### make api request
    response = requests.get(url).json()

    features = [x for x in response['features']]

    return features

feature_list=[]

##### for all features in the current and prior year.....
for feature in (callAndStore(current_year)+callAndStore(last_year)):
    clean_feature={
        'date':datetime.datetime.fromtimestamp(feature['attributes']['reportedDateTime']/1000).strftime("%m/%d/%Y"),
        'time':datetime.datetime.fromtimestamp(feature['attributes']['reportedDateTime']/1000).strftime("%H:%M:%S"),
        'centerLong': feature['attributes']['centerLong'],
        'centerLat':feature['attributes']['centerLat'],
        'description':feature['attributes']['description'].strip()
        }
    feature_list.append(clean_feature)

### write response to json file
with open(f'../resources/Police_Incidents_{last_year}_to_{current_year}.json','w+') as json_file:
    json.dump(feature_list,json_file)

