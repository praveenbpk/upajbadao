from flask import Blueprint, jsonify
import sys 
sys.dont_write_bytecode = True

# init blueprint
errors = Blueprint("errors", __name__)

@errors.errorhandler(403)
def forbidden(errorMsg=None):
  message = { 
    'result': False,
    'message': errorMsg,
    'err_code': 403
  }
  resp = jsonify(message)
  resp.status_code = 403
  resp.headers['Content-Type'] = 'application/json'
  resp.headers['Access-Control-Allow-Origin'] = '*'
  resp.headers['Access-Control-Allow-Credentials'] = 'true' 
  return resp

@errors.errorhandler(401)
def unauthorised(errorMsg=None):
  message = { 
    'result': False,
    'message': errorMsg,
    'err_code': 401
  }
  resp = jsonify(message)
  resp.status_code = 401
  resp.headers['Content-Type'] = 'application/json'
  resp.headers['Access-Control-Allow-Origin'] = '*'
  resp.headers['Access-Control-Allow-Credentials'] = 'true' 
  return resp


@errors.errorhandler(404)
def not_found(errorMsg="", body=None, params=None, form=None):
  data_obj = {}
  msg = errorMsg
  
  if body:
    msg = "Missing some required fields"
    data_obj["json_body"] = body
  if form:
    msg = "Missing some required fields"
    data_obj["form_body"] = form
  if params:
    msg = "Missing some required fields"
    data_obj["query_params"] = params


  message = { 
    'result': False,
    'err_code': 404,
    'message': msg,
    'data': data_obj
  }

  resp = jsonify(message)
  resp.status_code = 404
  resp.headers['Content-Type'] = 'application/json'
  resp.headers['Access-Control-Allow-Origin'] = '*'
  resp.headers['Access-Control-Allow-Credentials'] = 'true' 
  return resp


@errors.errorhandler(400)
def invalid(errorMsg,errCode=0):
  message = { 
    'result': False,
    'err_code': errCode,
    'message': errorMsg
  }
  resp = jsonify(message)
  resp.status_code = 400
  resp.headers['Content-Type'] = 'application/json'
  resp.headers['Access-Control-Allow-Origin'] = '*'
  resp.headers['Access-Control-Allow-Credentials'] = 'true' 
  return resp

def failed(errorMsg):
  message = { 
    'result': False,
    'err_code': 200,
    'message': errorMsg
  }
  resp = jsonify(message)
  resp.status_code = 200
  resp.headers['Content-Type'] = 'application/json'
  resp.headers['Access-Control-Allow-Origin'] = '*'
  resp.headers['Access-Control-Allow-Credentials'] = 'true' 
  return resp


@errors.errorhandler(500)
def unhandled(errorMsg=None):
  if not errorMsg:
    errorMsg = "Unhandled exception"
  message = { 
    'result': False,
    'err_code': 500,
    'message': errorMsg
  }
  resp = jsonify(message)
  resp.status_code = 500
  resp.headers['Content-Type'] = 'application/json'
  resp.headers['Access-Control-Allow-Origin'] = '*'
  resp.headers['Access-Control-Allow-Credentials'] = 'true' 
  return resp