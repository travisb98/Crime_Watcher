######## this code is currently being ran from the "app" folder

from flask import Flask, render_template, jsonify, request, redirect, url_for, Response
# from flask_session import Session
from flask_cors import CORS, cross_origin

import socket
import geocoder
import requests
import json
import crime_api

##### we shouldn't hard code this variable, we'll need to make it dynamic to detect if we're on pythonanywhere
#### local server
local_server = 'http://127.0.0.1:5000/'


#create app
app = Flask(__name__)
## just a random key that is needed for session
# app.secret_key ='thisRandomStringIsNeededWhenUsingFlaskSessions'
# SECRET_KEY = "thisRandomStringIsNeededWhenUsingFlaskSessions"
# SESSION_TYPE = 'filesystem'

# app.config.from_object(__name__)
# Session(app)
CORS(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/load", methods =['POST','GET'])
def load():

    ## after hitting the api to get crimes in the are, I should look up the danger score for each crime and add it to the crime list
    if request.method == 'POST':
        #### we'll want to fill this danger score in once it's determined
        danger_score = 7
        ##### data we'll be sending to front end
        data = {
            'userData':{'dangerScore':danger_score,'userLat':float(request.form['userLat']),'userLong':float(request.form['userLong'])},
            'crimeData':crime_api.nearbyCrimes(request.form,5)}


        json_data = json.dumps(data)

        # return response to server
        return Response(json_data, mimetype='application/json') 
    else:
        ### if someboy types /load in the url
        return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
   

