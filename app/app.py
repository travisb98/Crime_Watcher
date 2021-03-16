######## this code is currently being ran from the "app" folder

from flask import Flask, render_template, jsonify, request, redirect, url_for, Response
# from flask_session import Session
from flask_cors import CORS, cross_origin

import sys
import geocoder
import requests
import json

### crime api module we made
import crime_api

### algorithm to get danger score
import danger_score_algorithm

#create app
app = Flask(__name__)
## just a random key that is needed for session
# app.secret_key ='thisRandomStringIsNeededWhenUsingFlaskSessions'
# SECRET_KEY = "thisRandomStringIsNeededWhenUsingFlaskSessions"
# SESSION_TYPE = 'filesystem'


#### if on python anywhere.......
##### path for pythonAnywhere
sys.path.append('/home/travisb98/mplsCrime')




# app.config.from_object(__name__)
# Session(app)
CORS(app)

@app.route("/")
def home():
    print('Server Received request for home page')
    return render_template('index.html')


@app.route("/load", methods =['POST','GET'])
def load():
    print('server received request to load server')

    ## if the method was post(error handling)
    if request.method == 'POST':
        print('method was post')
        ## using the danger_score_algorithm module to determine the danger score
        dangerScore = int(danger_score_algorithm.dangerScore({'userLat':request.form['userLat'],'userLong':request.form['userLong']}))
        
        ##### data we'll be sending to front end
        data = {
            'userData':{'dangerScore':dangerScore,'userLat':float(request.form['userLat']),'userLong':float(request.form['userLong'])},
            'crimeData':crime_api.nearbyCrimes(request.form,5)}

        print('Pre JsonD data on server:')
        print(data)
        print('-----------------')

        ### convert data to json
        json_data = json.dumps(data)
        print('Json data sending to client')
        print(json_data)
        print('-----------------')

        # return response to server
        return Response(json_data, mimetype='application/json') 
    else:
        ### if someboy types /load in the url

        print('somebody tried to access the load page')

        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
   

