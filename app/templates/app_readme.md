
# Minneapolis Crime Watcher Application

This application uses machine learning to answer the question "How safe am I at this location in Minneapolis?". Access the application [here](https://travisb98.pythonanywhere.com/)

By using an algorithm to convert recently reported crimes in Minneapolis to danger scores for each of the 500 sections (created with clustering), a linear regression model calculates the current danger level of the user's location. The application also displays the user's location on a map along with recently reported crimes in that area. 


For more information on the project, check out our [github page](https://github.com/travisb98/Crime_Watcher)


# API Connection
We used the API from [OpenDataMinneapolis](https://opendata.minneapolismn.gov/datasets/police-incidents-2021)
Since each year had its own api string, we developed the code to make multiple API hits, once for each year of requested data. We also used queries within the url to request data within the last x number of days, which allowed us to toggle the amount of data coming back from the API. We then used geopy to get a descriptive location of the crime by inputting the crime's coordinates. All of this functionality was built into functions within the crime_api.py file. The functions were then implemented into the flask server in the app.py file.


# Flask App
The Flask app is contained in the app.py file. The flask server contains 2 main routes. The home page that is loaded when the user initially visits the website and the load route which receives and returns data to and from the front-end javascript.

# Map
We used javascript leafly to map the user's location and locations of crimes in the user's area. To distinguish the user's maker from the crime markers, we made the user's marker green and the crime markers red. The crime markers have pop-ups that contain details related to the crime including date, time, and type of offense.

