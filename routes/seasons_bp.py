from flask_restful import Resource, Api
from flask import Flask, request
from flask import Blueprint


season__bp= Blueprint('season__bp',__name__)
api = Api(season__bp)


class Seasons(Resource):
     
      def get(self):
          
        if (request.method == "GET" ):
            
            response = get_seasonlist()
            return response

class bookmark(Resource):
     def get(self,uuid,fav):
      
        if uuid and fav == 1:
            response = bookmarkAdd(uuid,fav)
            return response
        else:
            response = bookmarkremove(uuid,fav)
            return response    