######## this code is currently being ran from the "app" folder

from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from flask_session import Session
from flask_cors import CORS

import socket
import geocoder
import requests
import json

## this module is being finalized and will return api calls
import crime_api

##### we shouldn't hard code this variable, we'll need to make it dynamic to detect if we're on pythonanywhere
#### local server
local_server = 'http://127.0.0.1:5000/'



#create app
app = Flask(__name__)
## just a random key that is needed for session
app.secret_key ='thisRandomStringIsNeededWhenUsingFlaskSessions'
SECRET_KEY = "thisRandomStringIsNeededWhenUsingFlaskSessions"
SESSION_TYPE = 'filesystem'

app.config.from_object(__name__)
Session(app)



@app.route("/")
def home():

    print('home page was reached')
    return render_template('splash.html',button_name='splash page button name')


# @app.route("/coor",methods =['POST'])
@app.route("/coor",methods =['POST','GET'])
def coor():
    print('-------------------------')
    print('coor route reached')
    print('-------------------------')


    #######
    if request.method == 'POST':
        print('request method was POST')
        #### get the coordinates that we posted
        rf = request.form
        coordinates = {'userlat':rf['userlat'],'userlon':rf['userlon']}
        #### storing the user coordinates in the flask session 
        session['usercoor'] = coordinates
        sessionCoordinates = session['usercoor']

        print(f'the coordinates in the session are{sessionCoordinates}')

        return redirect('/results')

    else:
        print('the method must have been GET')
        if 'usercoor' in session:
            print('The usercoor is present in the session  ')

            ### extract coordinates from session 
            coordinates = session['usercoor']

            return f'<h1>Get Method on COOR route and coordinates exist in session {coordinates}</h1>'

        else:
            print('the coordinate variable was not saved to the session when the GET request was made')
            print('this shouldnt be happening')
            rf = request.form
            return f'<h1> the coordinate variable was not saved to the session when the GET request was made. Request Form: {rf}</h1>'



@app.route('/results')
def results():
    print('reached results page')

    if 'usercoor' in session:
        print('usecoor was present in session')

        ### get the coordinates variable from the session
        coordinates = session['usercoor']
        print(f'session coordinates are {coordinates}')
        #### these are place holder variables
        dangerscore = 8

        #### call api to return list of crimes that occured nearby
        flask_list = crime_api.nearbyCrimes(float(coordinates['userlat']),float(coordinates['userlon']),5)

        text1 = f'Your danger score is {dangerscore} '
        text2 = f'Your coordinates are {coordinates}'
        list_title ='List of crimes'
        button_name = 'reLoad'

        userlat = coordinates['userlat']
        userlon = coordinates['userlon']

        # session.pop('usercoor',None)

        return render_template('results.html', flask_list=flask_list,text1=text1,text2=text2,list_title=list_title,button_name=button_name,userlat=userlat,userlon=userlon)
        # return render_template('results.html',button_name='buttooooon', text1 = coordinates)
        # return f'<h1>results page coordinates{coordinates}</h1>'
    else:
        print ('user coor was not present in session by the time the results page was hit')

        return f'<h1>user coor was not present in session</h1>'

        
if __name__ == "__main__":
    app.run(debug=True)
    # app.run()






####### everything below this obnoxious block is test code
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################


#### route group 2
# # # ############################################################################################################
# # # ############################################################################################################
# # # ############################################################################################################

# ######
# @app.route("/",methods =['POST','GET'])
# def home():

#     if request.method == 'POST':
#         ###### load results page with coordinates from javascript
#         print('post request received')

#         flask_list=['crime1','crime2','crime3','crime4','crime5','crime6']
#         text1 = f'Teeeeg'
#         text2 = f'asfd'
#         list_title ='asdf'
#         button_name = 'reLoad' 




#         return render_template('results',flask_list=flask_list,text1=text1,text2=text2,list_title=list_title,button_name=button_name)
#     else:
#         ###### load basic index page
#         flask_list=['this','is','a','list','from','flask']
#         text1 = f'This is text 1'
#         text2 = f'string served up by flask'
#         list_title ='Press Load to to Generate List of Crimes'
#         button_name = 'Load'
#         return render_template('index.html',flask_list=flask_list,text1=text1,text2=text2,list_title=list_title,button_name=button_name)


# ############# end route group 2
# # # ############################################################################################################
# # # ############################################################################################################
# # # ############################################################################################################ 











# # ##### route group 1 (doesn't work great, results page only comes up after pressing the button then refreshing the page)
# ### the javascript map loads but the new html isn't rendering
# # ############################################################################################################
# # ############################################################################################################
# # ############################################################################################################
# @app.route('/results')
# def results():
#     print('results route reached')
#     return f'<h1>This is the results page</h1>'

# #  homepage
# @app.route("/")
# def home():
#     print("Server received request for 'Home' page...")

#     ###### this isn't working, maybe I should have the 2 options under here set up as 2 different routes?
#     #### if the coor route has already been accessed the the coordinates exists
#     if 'usercoor' in session:
#         print('The usercoor is present in the session  ')

#         ### extract coordinates from session 
#         coordinates = session['usercoor']

#         #### Delete the session data do avoid for loop issue
#         # session.pop('usercoor',None)

#         dangerscore = 7
#         flask_list=['crime1','crime2','crime3','crime4','crime5','crime6']
#         text1 = f'Your danger score at {coordinates} is {dangerscore}'
#         text2 = f'Your Location and Crimes:'
#         list_title ='List of Recent Crimes in Your Area:'
#         button_name = 'Reload'

#         return render_template('results.html',flask_list=flask_list,text1=text1,text2=text2,list_title=list_title,button_name=button_name)
#         # return '<h1>the usercoor in the home route was present</h1>'
         
#     else :
#         #### this route should be hit when the user first comes to the page
#         print('The usercoor does not exist in the session')
#         flask_list=['this','is','a','list','from','flask']
#         text1 = f'This is text 1'
#         text2 = f'string served up by flask'
#         list_title ='Press Load to to Generate List of Crimes'
#         button_name = 'Load'
#         return render_template('index.html',flask_list=flask_list,text1=text1,text2=text2,list_title=list_title,button_name=button_name)

# # GET and POST set up:
# # https://www.youtube.com/watch?v=9MHYHgh4jYc&t=33s
# # Sessions:
# # https://www.youtube.com/watch?v=iIhAfX4iek0
# ### this route will pull the coordinates from the javascript

# @app.route('/coor',methods =['POST','GET'])
# def coor():
#     print('------------------------')
#     print('------------------------')
#     print('coor route was reached')
#     print('------------------------')
#     print('------------------------')

#     if request.method =='POST':
#         print('method was post')
#         rf = request.form
#         coordinates = {'userlat':rf['userlat'],'userlon':rf['userlon']}
#         #### storing the user coordinates in the flask session 
#         session['usercoor'] = coordinates
#         print('------------------------')
#         print('------------------------')
#         print(f'coordinates from post method{coordinates}')
#         print('------------------------')
#         print('------------------------')
#         return redirect('/')
#         # return redirect('/results')
#         # return redirect(url_for('results'))

#     else:
#         print('method was not post')
#         # return '<h1>method was not post</h1>'
#         # return ' coor route method was not post'
#         return redirect('/')
# ##### end route group 1 
# ############################################################################################################
# ############################################################################################################
# ############################################################################################################

















###### the "if __name__ == "__main__"" statement will need to be different when we're hosting on pythonanywhere
##### notes on using flask and pythonanywhere https://help.pythonanywhere.com/pages/Flask/
#### section on how to use app.run() will be applicable here 
##### considering the implications of this article, i think we'll need to make code that detects if we're...
##### ...runing our code locally or on pythonanywhere, then executes different code depending on where we're currently hosting.
#####





# @app.route('/result/<usrcoor>')
# def result(usrcoor):
#     return f'<h1>{usrcoor}</h1>'


# #### grab the request's form option to get the variables we passed from javascript
# r = request.form
# coordinates = {'userlat':r['userlat'],'userlon':r['userlon']}
# print("---------------------")
# print('This variable was sent to flask from the javasacript file:')
# print(coordinates)
# print('the variable type is')
# print(type(coordinates))
# print("---------------------")
# fake_list=['crime1','crime2','crime3','crime4','crime5','crime6']
# result_message = f'your fake danger score is 12/10 at coordinates {coordinates}'
# button_name = 'Reload'
# return render_template('results.html',list=fake_list,text=result_message,button_name=button_name)
####psudeo code
######## hit api to get list of recent crimes in the area (x number of miles from coordinates)
# return redirect('/')
# return redirect(url_for('results'), code=307)
# return redirect(url_for('results',coordinates = coordinates))


    # crime_list=['fakecrime1','fakecrime2','fakecrime3']
    # new_message = f'your coordinates are {coordinates}'
    # new_button_name = 'Button name from flask'
    # new_page_name = 'Minneapolis Crime Watcher'
    # return render_template('index.html',list=crime_list,text=new_message,button_name=new_button_name,page_name=new_page_name)





    # if 'coordinates' in globals():
    #     print(f'coordinates passed to global variable')

    #     crime_list=['fake crime 1','fake crime 2','fake crime 2']
    #     message =f'your coordinates are {coordinates}'

    # else :
    #     crime_list=['this','is','a','list','from','flask']
    #     message = f'string served up by flask'



    ####psuedo code 
    #### if cordinates have already been pulled, meaning the coor route was already hit,.....
    ############# return render_template('index.html, ###one set of variables)
    ##### else
    ############# return render_template('index.html, second set of variables)


    # ##### if the coordinates variable exists in the global set of variables, return different html
    # if 'coordinates' in globals():
    #     newmessage = f'your coordinates are {coordinates}'
    #     return render_template('index.html',list=test_list,text=newmessage,button_name=button_name,page_name=page_name)
    # else:
    #     return render_template('index.html',list=test_list,text=message,button_name=button_name,page_name=page_name)









# ### just using this route to get the user's ip address
# @app.route("/location",methods=['GET'])
# def location():
    
#     # geoip_data = simple_geoip.get_geoip_data(request.environ['HTTP_X_FORWARDED_FOR'])  
#     # geoip_data = simple_geoip.get_geoip_data(request.environ['REMOTE_ADDR'])
#     # geoip_data = simple_geoip.get_geoip_data(request.remote_addr)
#     # geoip_data = request.remote_addr

#     return "filler text"
#     # return jsonify(data=geoip_data)






# from flask_simple_geoip import SimpleGeoIP
# from config import sgipAPIKey, sgipURL





### https://pypi.org/project/Flask-Simple-GeoIP/
###


# # The API key is obtained from the GEOIPIFY_API_KEY environment variable.
# # Alternatively it can be set as follows:
# app.config.update(GEOIPIFY_API_KEY=sgipAPIKey)


# # Initialize the extension for simple geo_ip
# simple_geoip = SimpleGeoIP(app)

# # The API key is obtained from the GEOIPIFY_API_KEY environment variable.
# # Alternatively it can be set as follows:
# app.config.update(GEOIPIFY_API_KEY=sgipAPIKey)


# GEOIPIFY_API_KEY=sgipAPIKey



# if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
#     return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
# else:
#     return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200


# # geo_loc_url = f'https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={sgipAPIKey}&ipAddress={ip_address}'
# # response = request.get(geo_loc_url)
# # print(response)

# # geoip_data = simple_geoip.get_geoip_data(ip_address)


# return jsonify()

# # r = requests.get(url).json()
# # j = json.load(r)

# # response_list = [ for x in ]


# #### using flask
# # ip_address =request.remote_addr

# # return f'Home page. Your ip address is {url}. Your coordinates are{r}'


# # return ".Welcome to my 'Home' page!"


# ###### "clever" solution offered by pytyhon anywhere
# from socket import gethostname
# [...]
# if __name__ == '__main__':
#     if 'liveconsole' not in gethostname():
#         app.run()



#### this code might be useful for getting user location
# import geocoder
# g = geocoder.ip('me')
# print(g.latlng)


# # #### using socket library
# # hostname =socket.gethostname()
# # ip_address = socket.gethostbyname(hostname)

# ip_address = '174.20.116.141'

# g = geocoder.ip(ip_address)

# coor = g.latlng
