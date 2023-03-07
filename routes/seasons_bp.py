from flask_restful import Resource, Api
from flask import Flask, request
from flask import Blueprint
from controllers.season import *
import sys 
sys.dont_write_bytecode = True

season__bp= Blueprint('season__bp',__name__)
api = Api(season__bp)


class Seasons(Resource):
    def post(self):
        
        if ( request.method == "POST"  ):
            
            name = request.form["name"],
            print(name,'name')
            phonenumber = request.form["phonenumber"]
            email = request.form["email"]
            image = request.form["image"]
            address1 = request.form["address1"]
            address2 = request.form["address2"]
            uuid_tehsil = request.form["uuid_tehsil"]
            geo_lat = request.form["geo_lat"]
            geo_lng = request.form["geo_lng"]
            print(geo_lng)
         
            response = user_create(name = name,phonenumber = phonenumber,email =email,image =image,address1 =address1,address2=address2,uuid_tehsil=uuid_tehsil,geo_lat=geo_lat,geo_lng=geo_lng)
            return response
        
        else:
             return({'message':'bad request'}),400
     
    def get(self,lan):
          
        if (request.method == "GET" ):
            
            response = getseason(lan)
            return response


        
class Location(Resource):
      def get(self,lan,uuid_state = None,uuid_district = None):
          
          if uuid_state is not None and lan :
              response = get_district(lan,uuid_state)
              return response
          
          elif uuid_district is not None  and lan:
              response = get_tehsil(lan,uuid_district)
              return response
          else:
            response = get_state(lan)
            return response

class UserDevice(Resource):
     def post(self):
        
        if ( request.method == "POST"  ):
            uuid_user = request.form["uuid_user"]
            device_id = request.form["device_id"]
            device_name = request.form["device_name"]
            device_model = request.form["device_model"]
            platform_type = request.form["platform_type"]
            os_version = request.form["os_version"]
            fcm_token = request.form["fcm_token"]
           
            response = user_device(uuid_user = uuid_user,device_id = device_id,device_name =device_name,device_model =device_model,platform_type =platform_type,os_version=os_version,fcm_token=fcm_token)
            return response
        
        else:
             return({'message':'bad request'}),400


class search(Resource):
      def get(self,text):
          if text is not None  :
              response = getAlllist(text)
              return response
          

api.add_resource(Seasons,"/seasonlist/<lan>","/user")
api.add_resource(UserDevice,"/user_device")
api.add_resource(Location,"/state/<lan>","/district/<uuid_state>/<lan>","/tehsil/<uuid_district>/<lan>")
