##### this py file will call the api for the current and previous year, clean the data, and save all features for both years into a json file

import pandas as pd
import requests
import json
import datetime
import pickle

from sklearn.cluster import KMeans

### define the current and previous year
current_year = datetime.datetime.now().year
last_year = current_year - 1


### function that calls api and returns the features for a given year
def callAndStore(year):
    url = f'https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Police_Incidents_{year}/FeatureServer/0/query?where=1%3D1&outFields=reportedDateTime,offense,description,centerLong,centerLat&outSR=4326&f=json'
    ### make api request
    response = requests.get(url).json()

    features = [x for x in response['features']]

    return features

crime_list=[]

##### for all features in the current and prior year.....
for feature in (callAndStore(current_year)+callAndStore(last_year)):
    clean_feature={
        'date':datetime.datetime.fromtimestamp(feature['attributes']['reportedDateTime']/1000).strftime("%m/%d/%Y"),
        'time':datetime.datetime.fromtimestamp(feature['attributes']['reportedDateTime']/1000).strftime("%H:%M:%S"),
        'centerLong': feature['attributes']['centerLong'],
        'centerLat':feature['attributes']['centerLat'],
        'description':feature['attributes']['description'].strip()
        }
    crime_list.append(clean_feature)


incidents = pd.DataFrame(crime_list)

# Initialize and Fit KMeans Model
clusterer = KMeans(n_clusters=500,random_state=42).fit(incidents[["centerLong","centerLat"]])

# Run Predictions
predictions = clusterer.predict(incidents[["centerLong","centerLat"]])

# Add column for clusters to incidents dataframe
incidents["cluster"] = predictions

# Save Model using Pickle
pickle.dump(clusterer, open("../models/clusterer.pkl", "wb"))

### write response to json file
with open(f'../resources/Police_Incidents_{last_year}_to_{current_year}.json','w+') as json_file:
    json.dump(crime_list,json_file)

