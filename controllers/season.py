
from utilities.errors import invalid, not_found, unhandled, unauthorised, failed
from models.season import *



def getseason(lan):
     try:     
        result = Seasons.getseasonAlldata(lan)
        if result:
            return ({'result':True,'data':result}), 200
        else:
            return invalid('Bad request',400)
     except Exception as e:
          return str(e)



def bookmark_add_remove(uuid,fav):
    active = "added successfully"
    deactive =" bookmark removed successfully"
    
    try:    
        if uuid and fav == 1:
            result = Seasons.bookmark_add(uuid,fav)
            return ({'result':True,'message':active}),202
    
                
        else:
            result = Seasons.remove_bookMark(uuid,fav)
            return ({'result':True,'message':deactive}),202
    except Exception as e:
          return str(e)
    
def get_single_season(uuid,ln):
    try:
        if uuid:
            data=Get_season.getseason(uuid,ln)
            return {'result':True,'season':data},200
        else:
            return False
    except Exception as e:
        return str(e)
    
def get_single_crop(uuid,ln):
    try:
        if uuid:
            data=Get_season.getcrop(uuid,ln)
            return {'result':True,'season':data},200
        else:
            return False
    except Exception as e:
        return str(e)   