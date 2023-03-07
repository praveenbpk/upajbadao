from utilities.errors import invalid, not_found, unhandled, unauthorised, failed
from models.scheme import *
import sys 
sys.dont_write_bytecode = True



def get_scheme(uuid,lan):
    try:
        if uuid:
            data=Get_scheme.getscheme(uuid,lan)
            return {'result':True,'scheme':data},200
        else:
            return invalid('bad request'),400
    except Exception as e:
        return str(e)