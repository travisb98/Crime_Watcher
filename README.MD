# Minneapolis Crime Watcher Application
![Minneapolis Skyline](FinalImages/minneapolis.jpg)
## Overview

This application uses machine learning to answer the question "How safe am I at this location in Minneapolis?". Access the application [here](https://travisb98.pythonanywhere.com/)

By using an algorithm to convert recently reported crimes in Minneapolis to danger scores for each of the 500 sections (created with clustering), a linear regression model calculates the current danger level of the user's location. The application also displays the user's location on a map along with recently reported crimes in that area. 

## Data Sources

Crime data comes from [Open Minneapolis](https://opendata.minneapolismn.gov/datasets/police-incidents-2021/data?orderBy=neighborhood&orderByAsc=false) where all past police incidents are hosted. Incidents from the previous day are added at 9:30 am central time each day.

Crime severities come from [the Minnesota Courts](https://www.revisor.mn.gov/court_rules/rule/sg-5/).

## Tools and Languages

- Python (hosted on Python Anywhere)
    - Flask
    - Scikit-Learn
    - Pandas
    - requests
    - Pickle
- HTML
- CSS
  - Bootstrap
- JavaScript
  - D3
  - Jquery
  - Leaflet/Mapbox
  - Ajax


## Steps

### API Connection

### Machine Learning
1. Use API to collect current and past year's crime data
2. Use these reported crimes' locations to train a clustering model
3. Run Aggregation algorithm to develop the danger score of each cluster for each day that will be considered in the predictive model
4. Train linear model using the danger level of the previous 14 days
5. Predict the danger level of each cluster for the current day

### Flask App

### Map

### Gauge
The gauge and needle are based off of Preethi Ranjit's tutorial on [Creating an SVG Gauge Meter Animation](https://www.hongkiat.com/blog/svg-meter-gauge-tutorial/). We modified the code from the tutorial to add our own scale, colors, and size. When a danger score is returned from the server, it will be both reflected on the gauge and displayed underneath it.

### Information flow for the application
- send user coordinates from browser to server
- the server hits the opendata api, gets recent crimes in the users area, and calculates a danger score
- The server returns the danger score and nearby crimes
- Plot user's location
- Plot nearby crimes
- Display nearby crimes in a list




## Conclusion

Overall, this project is a great showcase of multiple tools and languages including machine learning, Python, Javascript, CSS, and HTML. Machine learning is used to predict the danger score for the user's location. Python was used to create the server, access the database, and provide the api endpoints. HTML and CSS were used to create the general page structure and styling. Javascript was used to create the visuals on the page.
    
 ![Final Product](FinalImages/PageSnip.PNG)




# **To do List !**
- make html and css pretty(connor)
- decide on means of generating crime data. should the section headers be present before the data is processed, or should the section headers populate with the data being passed from the server???(connor/travis) - filler text?
- Link to readme on page
- reorganize files in github and delete the data we don't need since the api is implemented
- finish gauge (Joe M) and implement into flask app
- finish readme (Joe Kell)
- Present with python anywhere and ask for a class mate in minneapolis to share their screen and demonstrate our app
- make sure to upload a finalized version of the app to pythonAnywhere. Or better yet, connect pythonAnywhere account to github repository(Travis)



# Future Updates
- goldeneye transition
- add descriptive locations to the list of crimes with geopy or geocoder(ie nicollet and third street)
- Places : your coordinates, stadium, downtown, campus, etc
- most common crime near you is x
- plot ALLL crimes, not just nearby crimes
- color code the markers
- geofencing minneapolis borders, just use min and max coordinates of minneapolis
- change the name of the repository to Minneapolis_Crime_Watcher ?
- figure out if we can move api calls to the backend to protect our keys
- numeric identfier for markers


