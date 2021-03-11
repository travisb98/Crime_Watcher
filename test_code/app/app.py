######## this code is currently being ran from the "app" folder

from flask import Flask, render_template, jsonify, request, redirect
import socket
import geocoder
import requests
import json

### this module is being finalized and will return api calls
# import crime_api

#create app
app = Flask(__name__)

#  homepage
@app.route("/")
def home():
    #### this route will serve up the home page,

    print("Server received request for 'Home' page...")

    #### not even sure if we should be all passing these variables from flask, maybe html or javascript is better idk
    fake_list=['this','is','a','list','from','flask']
    message = f'string served up by flask'
    button_name = 'Button name from flask'
    page_name = 'Minneapolis Crime Watcher'


    return render_template('index.html',list=fake_list,text=message,button_name=button_name,page_name=page_name)


### this route will pull the coordinates from the javascript
@app.route('/coor',methods =['POST','GET'])
def coor():
    print('------------------------')
    print('------------------------')
    print('------------------------')
    print('coor route was reached')
    print('------------------------')
    print('------------------------')
    print('------------------------')


    #### grab the request's form option to get the variables we passed from javascript
    r = request.form


  
    coordinates = {'userlat':r['userlat'],'userlon':r['userlon']}
    print("---------------------")
    print("---------------------")
    print("---------------------")
    print('This variable was sent to flask from the javasacript file:')
    print(coordinates)
    print('the variable type is')
    print(type(coordinates))
    print("---------------------")
    print("---------------------")
    print("---------------------")


    ####psudeo code
    ######## hit api to get list of recent crimes in the area (x number of miles from coordinates)








    #### I think i might actually want to make a 'results.html' page to direct to here 
    return redirect('/')




# # This route could be used for running the machine learning prediction
#### also, instead of making this a seperate route it might make more sense to put this in the route above that pulls the coordinates "/coor"
# @app.route("/load")
# def load():
    #psuedo code:
    ### hit  https://opendata.minneapolismn.gov/ api and use the date filter to return recent crimes in the area


    #run a function from an imported py file that makes prediction based on the users's location. This function should return recent crime in the area



#     return redirect('/')



###### the "if __name__ == "__main__"" statement will need to be different when we're hosting on pythonanywhere
##### notes on using flask and pythonanywhere https://help.pythonanywhere.com/pages/Flask/
#### section on how to use app.run() will be applicable here 
##### considering the implications of this article, i think we'll need to make code that detects if we're...
##### ...runing our code locally or on pythonanywhere, then executes different code depending on where we're currently hosting.
#####



if __name__ == "__main__":
    app.run(debug=True)
    




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
