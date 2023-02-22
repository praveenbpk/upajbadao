
from utilities.errors import invalid, not_found, unhandled, unauthorised, failed
from models.season import *



def getseason(lan):
     try:     
        result = Seasons.getseasonAlldata(lan)
        if result != False:
            print(result)
            return ({'result':True,'data':result}), 200
        else:
            return invalid('Bad request',400)
     except Exception as e:
          return str(e)

def get_state(lan):
     try:     
        result = Seasons.getstate(lan)
        if result != False:
            print(result)
            return ({'result':True,'data':result}), 200
        else:
            return invalid('Bad request',400)
     except Exception as e:
          return str(e)

def get_district(lan,uuid_state):
     try:     
        result = Seasons.getdistrict(lan,uuid_state)
        if result != False:
            print(result)
            return ({'result':True,'data':result}), 200
        else:
            return invalid('Bad request',400)
     except Exception as e:
          return str(e)
        
        
def get_tehsil(lan,uuid_district):
     try:     
        result = Seasons.gettehsil(lan,uuid_district)
        if result != False:
            
            return ({'result':True,'data':result}), 200
        else:
            return invalid('Bad request',400)
     except Exception as e:
          return str(e)        
        

# def bookmark_add_remove(uuid,fav):
#     active = "added successfully"
#     deactive =" bookmark removed successfully"
    
#     try:    
#         if uuid and fav == 1:
#             result = Seasons.bookmark_add(uuid,fav)
#             return ({'result':True,'message':active}),202
    
                
#         else:
#             result = Seasons.remove_bookMark(uuid,fav)
#             return ({'result':True,'message':deactive}),202
#     except Exception as e:
#           return str(e)

def user_create(**user):
    print(user['uuid_tehsil'])
    try:   
        if user['uuid_tehsil']:
            
          result = Seasons.User(**user)
          msg = " successfully created  User!"
          return ({'result':True,"message": msg}), 200  
      
        else:
             return invalid('Bad request',400)
        
    except Exception as e:
          return str(e)
    
def user_device(**user_device):
    try:   
        if user_device['uuid_user']:
            
          result = Seasons.Userdevice(**user_device)
          msg = " successfully created !"
          return ({'result':True,"message": msg}), 200  
      
        else:
             return invalid('Bad request',400)
        
    except Exception as e:
          return str(e)
    
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


def get_advisory(uuid,lan):
    try:
        if uuid:
            data=Get_advisory.getadvisory(uuid,lan)   
            return {'result':True,'advisory':data},200
        else:
            return invalid('bad request'),400
    except Exception as e:
        return str(e)
    
def get_scheme(uuid,lan):
    try:
        if uuid:
            data=Get_scheme.getscheme(uuid,lan)
            return {'result':True,'scheme':data},200
        else:
            return invalid('bad request'),400
    except Exception as e:
        return str(e)


def getAlllist(text):
     try:     
        if len(text) >= 4 :
         print(text,'length')
         croplist = Seasons.getsearch_crop_data(text)
         seasonlist = Seasons.getsearch_season_data(text)
         advisorylist = Seasons.getsearch_advisorylist(text)
         goverlist = Seasons.getseaarch_goverschemelist(text)
         Alllist = croplist,seasonlist,advisorylist,goverlist
         return ({'result':True,'data':Alllist}), 200
        else:
            return invalid('Bad request',400)
     except Exception as e:
          return str(e)