from flask_restful import Resource, Api
from flask import Flask, request
from flask import Blueprint
from controllers.season import *


season__bp= Blueprint('season__bp',__name__)
api = Api(season__bp)


class Seasons(Resource):
     
      def get(self,lan):
          
        if (request.method == "GET" ):
            
            response = getseason(lan)
            return response

# class bookmark(Resource):
#      def get(self,uuid,fav):
      
#         if uuid and fav == 1:
#             response = bookmark_add_remove(uuid,fav)
#             return response
        # else:
        #     response = bookmarkremove(uuid,fav)
        #     return response    

class get_season(Resource):
    def get(self,uuid,lan):
        if uuid:
            response=get_single_season(uuid,lan)
            return response  
        else: 
            return {"result":False,'message':"season not found" },404
        
class getcrop(Resource):
    def get(self,uuid,lan):
        if uuid:
            response=get_single_crop(uuid,lan)
            return response  
        else: 
            return {"result":False,'message':"crop not found" },404
        
class advisory(Resource):
    def get (self,uuid,lan):
        if uuid:
            response=get_advisory(uuid,lan)
            return response


class govt_scheme(Resource):
    def get(self,uuid,lan):
        if uuid:
            response=get_scheme(uuid,lan)
            return response

        
api.add_resource(get_season,'/season/<uuid>/<lan>')
api.add_resource(getcrop,'/crop/<uuid>/<lan>')
api.add_resource(advisory,'/advisory/<uuid>/<lan>')
api.add_resource(govt_scheme,'/scheme/<uuid>/<lan>')

