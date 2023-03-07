from flask_restful import Resource, Api
from flask import Flask, request
from flask import Blueprint
from controllers.advisory import *
import sys 
sys.dont_write_bytecode = True

advisory_bp= Blueprint('advisory__bp',__name__)
api = Api(advisory_bp)

class advisory(Resource):
    def get (self,uuid,lan):
        if uuid:
            response=get_advisory(uuid,lan)
            return response
        
api.add_resource(advisory,'/advisory/<uuid>/<lan>')