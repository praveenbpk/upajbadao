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
    def get(self,uuid):
        if uuid:
            response=get_single_season(uuid)
            return response  
        else: 
            return {"result":False,'message':"season not found" },404
        
class getcrop(Resource):
    def get(self,uuid):
        if uuid:
            response=get_single_crop(uuid)
            return response  
        else: 
            return {"result":False,'message':"crop not found" },404
