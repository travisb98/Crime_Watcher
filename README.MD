# Crime website

---

## Overview
For this project, we'll use data on police incidents in minneapolis to build a machine learning model that determines a safety score based on a user's location and other demographics. The application will display the users location on a map with other crime related data. 


## Programs, Languages and tools
- Python
- Scikit-Learn
- Javasacript
- HTML
- CSS
- Plotly?
- mapbox?
- Python Anywhere
- Pandas
- Requests

## Data Sources
- https://opendata.minneapolismn.gov/datasets/police-incidents-2021/data?orderBy=neighborhood&orderByAsc=false
- https://www.revisor.mn.gov/court_rules/rule/sg-5/


##  Steps/game plan
- Extract:
    - created python file update_2021.py that downloads and updates the 2021 csv
- Transform:
    - blah blah
- Load:
    - blah blah blah
- clean data
- train model
- use sentencing guidelines to create dictionary for severity of offenses https://www.revisor.mn.gov/court_rules/rule/sg-5/
- 2 options
    - cluster then model danger
    - grid then model danger




# notes from class brain storming
https://opendata.minneapolismn.gov/

https://opendata.minneapolismn.gov/datasets/police-incidents-2021/data?orderBy=neighborhood&orderByAsc=false


similar project:

https://towardsdatascience.com/demand-forecast-boston-crime-data-64a0cff54820


How safe are you in minneapolis based on location

machine learn to classify how safe we are

geofencing, extra feature

safety score

2 models, one for if you want to include your race or not

numerical

everything is quantified, murder is 10, rape is 9, etc

have a feature that does retraining

would we want to make a web based version or a browser based

how are we going to host it? https://www.pythonanywhere.com/

use rate limiter for number

have users enter their own API key

star out api key when user enters it into text field

use this for making the map https://plotly.com/javascript/scattermapbox/

how would the events of 2020 affect our dataset?

where are we starting and ending our data time wise ?

should we use tableau to do a preliminary analysis on the data?


day 2
---

how many clusters is to many clusters?

safety is y, time is x

safety score = if a crime happens to you now, how bad will it be

grid up the city

we should write up code that downloads and updates the police incidents spread sheet


day 3
---
activities to look at
    - voices
    - lsd


# steps
    - ETL 
        - look into API or CSV options, make it download
        - ETL should download data for current and prior year, clean then combine data
        - delete uneeded csv
        - "enter number of days you want to use to predict"
    - 
    - 
    - 
    - Front End
        - map that shows current location and recent crimes in vicinity
        - guage that shows danger level for your location
        - possible danger shading around border of map

# joes step list

1. Download all data using API or csv's
2. Clean and filter data and delete csv's if they exist storing data in ram 
3. run clustering model to determine which cluster each point is in or optionally train a new clustering model
4. Run Aggregation algorithm creating new data set and deleting old
5. train model using up to date data
6. predict current time period and return value


# notes on python anywhere

https://www.pythonanywhere.com/

- depending on the modules we'll be using, 
- PythonAnywhere has a bunch of modules installed, which is great. However, if we're using modules that aren't included in their prepackaged environment, we'll need to create a virtual environment
- Which modules are already included in PythonAnywhere : https://www.pythonanywhere.com/batteries_included/
- Notes on setting up a virtual environment : https://help.pythonanywhere.com/pages/Virtualenvs
