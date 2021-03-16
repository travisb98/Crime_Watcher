import pandas as pd
import requests
import json
import datetime
import pickle
import math
import random
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

import crime_api

def ClusterPredict():

    #This is a list of all crimes found so far and the correlated severity
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

    #These are the parameters for how much data the linear regression model will consider
    #After a thorough analysis we found that 50 clusters and 14 days of prior information was best
    Clusters = 50
    PriorDays = 14

    #### calls the api for a number of prior days and return a list of crimes
    crime_list=crime_api.callCrimeAPI(PriorDays)

    incidents = pd.DataFrame(crime_list)

    # Initialize and Fit KMeans Model
    clusterer = KMeans(n_clusters=Clusters,random_state=42).fit(incidents[["centerLong","centerLat"]])

    # Run Predictions
    predictions = clusterer.predict(incidents[["centerLong","centerLat"]])

    # Add column for clusters to incidents dataframe
    incidents["cluster"] = predictions

    # Save Model using Pickle
    pickle.dump(clusterer, open("./resources/clusterer.pkl", "wb"))

    today=datetime.date.today()

    InitDay=today-datetime.timedelta(days=PriorDays)

    #This assigns a danger value to each cluster that is not normalized
    Cluster_Danger=[[0 for x in range(Clusters)] for y in range(PriorDays)]

    for crime in crime_list:
        MDY = [int(x) for x in crime["date"].split("/")]
        date = datetime.date(MDY[2],MDY[0],MDY[1])
        if date == InitDay:
            try:
                Cluster_Danger[0][clusterer.predict([[crime["centerLong"],crime["centerLat"]]])[0]]+=crime_severity[crime["description"]]
            except KeyError:
                print("An error occured on the keys")
                print(crime["description"])
                print("")
        elif date > InitDay and date < today:
            num=int(str(date-InitDay).split(",")[0].split()[0])
            try:
                Cluster_Danger[num][clusterer.predict([[crime["centerLong"],crime["centerLat"]]])[0]]+=crime_severity[crime["description"]]
            except KeyError:
                print("An error occured on the keys")
                print(crime["description"])
                print("")

    #This creates a Scaled danger value for each cluster between 0 and 10
    MaxDanger=0
    for day in Cluster_Danger:
        if MaxDanger<max(day):
            MaxDanger=max(day)

    Scaled_Cluster_Danger=[[] for y in range(PriorDays)]
    for day in range (PriorDays):
        for cluster in Cluster_Danger[day]:
            Scaled_Cluster_Danger[day].append(cluster/MaxDanger*10)

    Training_Data=[]
    for d,day in enumerate(Scaled_Cluster_Danger):
        for c,cluster in enumerate(day):
            Training_Data.append({
                "Day": d,
                "Cluster": c,
                "Danger": cluster
            })
    Training=pd.DataFrame(Training_Data)

    Predictions=[]
    for cluster in range(Clusters):
        CurrentTraining=Training.loc[Training['Cluster']==cluster]

        #Setting up X and y to train our linear model
        X_train = CurrentTraining["Day"].values.reshape(-1, 1)
        y_train = CurrentTraining["Danger"].values.reshape(-1, 1)

        #Create the model
        model = LinearRegression()

        #Fit the model to the training data. 
        model.fit(X_train, y_train)

        # Use our model to predict a value
        predicted = model.predict([[PriorDays]])
        Predictions.append(min(max(math.ceil(predicted[0][0]),0),10))


    Predictions=np.array(Predictions).reshape(-1,1)
    PreDICT=[]
    for i,Prediction in enumerate(Predictions):
        PreDICT.append({"Cluster":i,
        "Danger":Prediction[0]})

    FinalPredictions=pd.DataFrame(PreDICT)
    print(FinalPredictions)

    # print(f'the danger score for cluster 5 is {FinalPredictions.Danger[5]}')

    return FinalPredictions



# #### getting user danger value

def dangerScore(user_coordinates):

    lat = float(user_coordinates['userLat'])

    lon = float(user_coordinates['userLong'])
    
    model = pickle.load(open("./resources/clusterer.pkl", 'rb'))

    #### normally lat lon, but im pretty sure this model takes lon,lat
    userCluster=model.predict([[lon,lat]])[0]
    ### get danger score for user from prediction df
    dangerScore =ClusterPredict().Danger[userCluster]

    print(f'danger score is {dangerScore}')

    return dangerScore




#     model.predict([lat,lon]])


