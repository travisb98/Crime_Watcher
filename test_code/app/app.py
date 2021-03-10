######## this code is currently being ran from the "app" folder

from flask import Flask, render_template, jsonify, request, redirect
import socket
import geocoder
import requests
import json
#### might need this????
# import requests

#create app
app = Flask(__name__)

#  homepage
@app.route("/")
def home():
    #### this route will serve up the home page,

    print("Server received request for 'Home' page...")

    #### not even sure if we should be passing these variables from flask, maybe html or javascript is better idk
    test_list=['this','is','a','list','from','flask']
    message = f'string served up by flask'
    button_name = 'Button name from flask'
    page_name = 'Minneapolis Crime Watcher'

    return render_template('index.html',list=test_list,text=message,button_name=button_name,page_name=page_name)


### this route will pull the coordinates from the javascript
@app.route('/coor',methods =['POST','GET'])
def coor():
    r = request.form

    coordinates = {'userlat':r['userlat'],'userlon':r['userlon']}
    # r = request.stream
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

    return redirect('/')




# # This route could be used for running the machine learning prediction
# @app.route("/load")
# def load():
#     print("route")
#     # dangerscore = 8
#     # return "the machine says your danger score is "
#     # we could return
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
