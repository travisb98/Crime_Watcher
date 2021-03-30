# This code is currently being ran from the "app" folder

from flask import Flask, render_template, jsonify, request, redirect, url_for, Response
# from flask_session import Session
from flask_cors import CORS, cross_origin
import markdown
import sys
import json
# crime api module we made
import crime_api
# algorithm to get danger score
import danger_score_algorithm

#create app
app = Flask(__name__)

# Secret key that is needed for session
# app.secret_key ='thisRandomStringIsNeededWhenUsingFlaskSessions'
# SECRET_KEY = "thisRandomStringIsNeededWhenUsingFlaskSessions"
# SESSION_TYPE = 'filesystem'

#Locations will be for dropdown
# {
#     "Minnehaha Falls": {"lat": 44.9153307, "long": -93.2110006},
#     "First Avenue": {"lat": 44.9785315, "long": -93.2759978},
#     "Stone Arch Bridge": {"lat": 44.9809433, "long": -93.2534122},
#     "Minneapolis Institute of Art": {"lat": 44.9586219, "long": -93.2741806},
#     "U.S. Bank Stadium": {"lat": 44.976614, "long": -93.2670266},
#     "Lake Harriet": {"lat": 44.9220232, "long": -93.3097262},
#     "Target Field": {"lat": 44.9823467, "long": -93.2796528}
# }

# Path for PythonAnywhere
sys.path.append('/home/travisb98/mplsCrime')

# instead of running ClusterPredict() every time a new person presses the button, we should use "from apscheduler.scheduler import Scheduler" to run ClusterPredict() on a daily basis
#WIP^

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

    # if the method was post(error handling)
    if request.method == 'POST':
        print('method was post')
        # using the danger_score_algorithm module to determine the danger score
        dangerScore = int(danger_score_algorithm.dangerScore({'userLat':request.form['userLat'],'userLong':request.form['userLong']}))
        
        # data we'll be sending to front end
        data = {
            'userData':{'dangerScore':dangerScore,'userLat':float(request.form['userLat']),'userLong':float(request.form['userLong'])},
            'crimeData':crime_api.nearbyCrimes(request.form,5)}



        # Convert data to json
        json_data = json.dumps(data)

        return Response(json_data, mimetype='application/json') 
    else:
        # Redirect when "/load" is added to the url

        print('Load page only available through button click\nRedirecting to home')

        return redirect('/')


@app.route("/about")
def about():
    print('Server Received request for about page')
    # psuedo: convert markdown template to html and render it 
    
    # this converts our markdown file to html
    with open('./templates/app_readme.md','r') as mdfile:
        text = mdfile.read()
        html = markdown.markdown(text)
    return html




if __name__ == "__main__":
    app.run(debug=True)
   

