import pandas as pd
import requests
import json
import datetime


def _annualCall(year,daysback):
    #### crime api url
    crime_url =f"https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Police_Incidents_{year}/FeatureServer/0/query?where=reportedDateTime>=CURRENT_TIMESTAMP+-INTERVAL\'{daysback}\'DAY&outFields=reportedDateTime,offense,description,centerLong,centerLat&outSR=4326&f=json"
    ### make api request
    response = requests.get(crime_url).json()
    ## reduce to a variable that just includes the features
    features = [x for x in response['features']]

    return features

##### this function determines how many times we'll need to hit the API, handles it accordingly, and returns cleaned data
##### this function will accept daysback as a parameter and return all crimes from (today - daysback) through today
##### the way this is written, i think the daysback interger might need to be under a certain amount
def callCrimeAPI(daysback):

    # ### define the current  date and the date x number of days in the past(iefirst_day)
    today = datetime.datetime.now()
    first_day = today - datetime.timedelta(days=daysback)
    print(f'your requested date range is {first_day} through {today}')

    ##### this if statement only works if the first_day is in the current or prior calendar year. It won't work if the 'daysback' variable puts us more than 2 calendar years in the past
    ##### i could put a limit on the value of daysback with a try except block
    ##### ..... or i could make the code more dynamic by counting the number of years between 'today' and 'first_day', storing that as a variable, then doing that number of api calls

    #### if the begining date is in the same year and today's year...
    if (today.year == first_day.year):
        print('hit the current year api for the date range')
        #### just call the api once for this year 
        crime_list = _annualCall(today.year,daysback)
    else:
        print('hit the api twice, once for each year, and combine the results')
        #### get the datetime object for the begining of this year
        start_of_current_year = datetime.datetime(today.year,1,1)
        ### how many days have passed since the begining of the year
        elapsed_time_delta = today - start_of_current_year
        ### hit the api twice, once for each year
        crime_list = _annualCall(today.year,elapsed_time_delta.days)+_annualCall(first_day.year,daysback)

    clean_crime_list =[]

    ##### for all features in the current and prior year.....
    for feature in crime_list :
        clean_feature={
            'date':datetime.datetime.fromtimestamp(feature['attributes']['reportedDateTime']/1000).strftime("%m/%d/%Y"),
            'time':datetime.datetime.fromtimestamp(feature['attributes']['reportedDateTime']/1000).strftime("%H:%M:%S"),
            'centerLong': feature['attributes']['centerLong'],
            'centerLat':feature['attributes']['centerLat'],
            'description':feature['attributes']['description'].strip()
            }
        clean_crime_list.append(clean_feature)
    return clean_crime_list

#### pass in  the latitude, longitude and number of days back to return recent nearby crimes
def nearbyCrimes(lat,lon,daysback):
    apiresults = callCrimeAPI(daysback)

    # print(f'length of api results: {len(apiresults)}')

    nearby_crimes_list =[]

    for crime in apiresults:
        if (lon-.02) < crime['centerLong'] < (lon+.02) and (lat-.02) < crime['centerLat'] < (lat+.02):
            nearby_crimes_list.append(crime)
    # print(f'length of nearby crimes:{len(nearby_crimes_list)}')

    return nearby_crimes_list