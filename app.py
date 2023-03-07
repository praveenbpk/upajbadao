from flask import Flask,redirect,request,url_for,session,jsonify
from routes.seasons_bp import *
from routes.crop import*
from routes.advisory import *
from routes.scheme import *
from flask_cors import CORS
import sys 
sys.dont_write_bytecode = True

app=Flask(__name__)
CORS(app)


app.register_blueprint(season__bp) 
app.register_blueprint(crop_bp)
app.register_blueprint(advisory_bp)
app.register_blueprint(scheme_bp)   



if __name__ == '__main__':

    app.run(host='localhost',debug=True)