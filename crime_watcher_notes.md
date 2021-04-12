
# Post presentation ideas
- give user's the ability to select certain locations, including their own, and load crime reports in that area (use draggable pin, extract coordinates from pins new location) your coordinates, stadium, downtown, campus, etc
      - use geopy to look up coordinates with a landmark/location description
- most common crime near you is x
- plot ALLL crimes, not just nearby crimes
- color code the markers based on crime type of vicinity of crime
- Use min and max coordinates to to set a boundry around minneapolis
- change the name of the repository to Minneapolis_Crime_Watcher ?
- numeric identfier for markers
- relative danger score (ie your area is the 3rd most dangerous area in minneapolis)
- make most recent crimes how up on top
- cross browser compatability
- figure out how we can make it an actual downloadable app. maybe we can make it work offline by loading it with a bunch of data and use it instead of the api when the app is offline.....?
- If users want, they can enter their address and phone number to receive text message notifications of crimes in their area
- feed day of the week and hourly data to the machine learning algorithm to find hourly and daily patterns
- a slider that selects the number of days back
- make needle flat on initial page load
- utilize other apis
     - Neighborhood Crime Stats :  https://opendata.minneapolismn.gov/datasets/neighborhood-crime-stats/
     - Police use of force : https://opendata.minneapolismn.gov/datasets/police-use-of-force
- re-write/re-format javascript
- run clustering daily
- save crime severity as json file
- make desktop view
- 



# **To do List !**

- delete pins if they already exist to avoid duplicate pins(Travis)
- make sure to upload a finalized version of the app to pythonAnywhere. Or better yet, connect pythonAnywhere account to github repository(Travis)
- review and edit code comments/layout
- implement scheduled execution of ClusterPredict() to update daily
- use new minneapolis crime watcher url
- get rid of d3 and just use jquery
- figure out if we can move api calls to the backend to protect our keys
     - https://kazuar.github.io/visualize-trip-with-flask-and-mapbox/











# Presentation
- Intro/Overview - Connor
- API connection/Data Source - Travis
- Machine Learning -Joe Kell
- Flask App - Travis
- Map, Gauge, and Table - Joe M
- HTML CSS and Design - Connor
- Wrap-up/Student Demo - Joe Kell
