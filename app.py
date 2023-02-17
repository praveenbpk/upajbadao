from flask import Flask,redirect,request,url_for,session,jsonify
from routes.seasons_bp import season__bp
from flask_cors import CORS

app=Flask(__name__)
CORS(app)


app.register_blueprint(season__bp) 



if __name__ == '__main__':

    app.run(host='localhost',debug=True)