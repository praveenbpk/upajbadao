from utilities.errors import invalid, not_found, unhandled, unauthorised, failed
from models.advisory import *
import sys 
sys.dont_write_bytecode = True

def get_advisory(uuid,lan):
    try:
        if uuid:
            data=Get_advisory.getadvisory(uuid,lan)   
            return {'result':True,'advisory':data},200
        else:
            return invalid('bad request'),400
    except Exception as e:
        return str(e)
    