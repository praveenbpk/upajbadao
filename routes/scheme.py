from flask_restful import Resource, Api
from flask import Flask, request
from flask import Blueprint
from controllers.scheme import *
import sys 
sys.dont_write_bytecode = True

scheme_bp= Blueprint('scheme_bp',__name__)
api = Api(scheme_bp)



class govt_scheme(Resource):
    def get(self,uuid,lan):
        if uuid:
            response=get_scheme(uuid,lan)
            return response
        
        
        
api.add_resource(govt_scheme,'/scheme/<uuid>/<lan>')