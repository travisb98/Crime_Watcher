# this py file will call the api for the current and previous year, clean the data, and save all features for both years into a json file
import pandas as pd
import requests
import json
import datetime
import pickle
import math
import numpy as np
from sklearn.cluster import KMeans

# defind the current and previous year
current_year = datetime.datetime.now().year
last_year = current_year - 1

# function that calls api and returns the features for a given year
def callAndStore(year):
    url = f'https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Police_Incidents_{year}/FeatureServer/0/query?where=1%3D1&outFields=reportedDateTime,offense,description,centerLong,centerLat&outSR=4326&f=json'
    # make api request
    response = requests.get(url).json()

    features = [x for x in response['features']]

    return features

crime_list=[]

# for all features in the current and prior year.....
for crime in (callAndStore(current_year)+callAndStore(last_year)):
    clean_crime={
        'date':datetime.datetime.fromtimestamp(crime['attributes']['reportedDateTime']/1000).strftime("%m/%d/%Y"),
        'time':datetime.datetime.fromtimestamp(crime['attributes']['reportedDateTime']/1000).strftime("%H:%M:%S"),
        'centerLong': crime['attributes']['centerLong'],
        'centerLat':crime['attributes']['centerLat'],
        'description':crime['attributes']['description'].strip()
        }
    crime_list.append(clean_crime)

incidents = pd.DataFrame(crime_list)

Clusters=500
# Initialize and Fit KMeans Model
clusterer = KMeans(n_clusters=Clusters,random_state=42).fit(incidents[["centerLong","centerLat"]])

# Run Predictions
predictions = clusterer.predict(incidents[["centerLong","centerLat"]])

# Add column for clusters to incidents dataframe
incidents["cluster"] = predictions

# Save Model using Pickle
# pickle.dump(clusterer, open("../models/clusterer.pkl", "wb"))

crime_severity={
"AUTOMOBILE THEFT": 4,
"THEFT-MOTR VEH PARTS": 2.5,
"OTHER THEFT": 2.5,
"THEFT FROM MOTR VEHC": 2,
"BURGLARY OF DWELLING": 5,
"BURGLARY OF BUSINESS": 4,
"ROBBERY PER AGG": 8,
"ASSLT W/DNGRS WEAPON": 6,
"ROBBERY INCLUDING AUTO THEFT": 4,
"ROBBERY OF PERSON": 4,
"BIKE THEFT": 2,
"CSC - RAPE": 9,
"SHOPLIFTING": 4,
"2ND DEG DOMES ASLT": 4,
"THEFT BY SWINDLE": 3,
"DOMESTIC ASSAULT/STRANGULATION": 4,
"ROBBERY OF BUSINESS": 4,
"ASLT-SGNFCNT BDLY HM": 4,
"ASLT4-LESS THAN SUBST HARM": 4,
"THEFT FROM PERSON SNATCH/GRAB": 4,
"ARSON": 8,
"MURDER (GENERAL)": 11,
"CSC - SODOMY": 9,
"THEFT FROM BUILDING": 4,
"3RD DEG DOMES ASLT": 6,
"CSC - PENETRATE WITH OBJECT": 9,
"ASLT-GREAT BODILY HM": 9,
"OTHER VEHICLE THEFT": 4,
"ASLT4-SUBST HARM OR WEAPON": 6,
"OBS - PETTY THEFT": 2,
"ON-LINE THEFT": 2.5,
"FAIL TO PAY - TAXI/HOTEL/REST": 2.5,
"ARSON-3RD DEGREE": 3,
"OBS-CSCR - USE EXT 1, 2 OR 3": 8,
"POCKET-PICKING": 4,
"LOOTING": 5,
"SCRAPPING-RECYCLING THEFT": 2,
"1ST DEG DOMES ASLT": 4,
"MURDER - 2ND DEGREE": 11,
"HACKING - THEFT OF SERVICE": 3,
"ARSON-1ST DEGREE": 8,
"ACCESS/ALTER SYSTEM/NETWORK": 3,
"ARSON-5TH DEGREE": 3,
"GAS STATION DRIV-OFF": 2.5,
"DO NOT USE": 0
}

#This assigns a danger value to each cluster
Cluster_Danger=[0 for x in range(Clusters)]
for crime in crime_list:
    try:
        Cluster_Danger[clusterer.predict([[crime["centerLong"],crime["centerLat"]]])[0]]+=crime_severity[crime["description"]]
    except KeyError:
        print("An error occured on the keys")
        print(crime["description"])
        print("")
print(Cluster_Danger)

#This creates a normalized danger value for each cluster between 0 and 10
Normal_Cluster_Danger=[]
MaxDanger=max(Cluster_Danger)
for cluster in Cluster_Danger:
    Normal_Cluster_Danger.append(math.ceil(cluster/MaxDanger*10))
print("")
print("")
print(Normal_Cluster_Danger)

