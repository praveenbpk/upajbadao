from controllers.crop import *
from flask_restful import Resource, Api
from flask import Flask, request
from flask import Blueprint
import sys 
sys.dont_write_bytecode = True

crop_bp= Blueprint('crop_bp',__name__)
api = Api(crop_bp)

class get_croplist(Resource):
    def get(self,uuid,lan):
        if uuid:
            response=get_single_season(uuid,lan)
            return response  
        else: 
            return {"result":False,'message':"season not found" },404
        
class getcrop_details(Resource):
    def get(self,uuid,lan):
        if uuid:
            response=get_single_crop(uuid,lan)
            return response  
        else: 
            return {"result":False,'message':"crop not found" },404

class search(Resource):
    def get(self,uuid):
        if uuid:
            response=get_single_crop(uuid)
            return response  
        else: 
            return {"result":False,'message':"crop not found" },404




api.add_resource(get_croplist,'/croplist/<uuid>/<lan>')
api.add_resource(getcrop_details,'/crop_details/<uuid>/<lan>')
api.add_resource(search,'/search/<text>')