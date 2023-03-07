from utilities.errors import invalid, not_found, unhandled, unauthorised, failed
from models.crop import *
import sys 
sys.dont_write_bytecode = True



def get_single_season(uuid,lan):
    try:
        if uuid:
            data=Get_season.getseason(uuid,lan)
            return {'result':True,'season':data},200
        else:
            return False
    except Exception as e:
        return str(e)
    
def get_single_crop(uuid,lan):
    try:
        if uuid:
            data=Get_season.getcrop(uuid,lan)
            
            crop,c_name,content=data
            for x in range(0,len(crop)):
                data={}
                data['crop']=crop
                for x in range(0,len(c_name)):
                    data['recomm']=c_name
                    for y in data['recomm']:
                        y['content']=content
                        print(y)
                    print(c_name)
                
                return {'result':True,'data':data},200
        else:
            return False
    except Exception as e:
        return str(e)  