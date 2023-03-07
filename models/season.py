from utilities.helpers import openDbconnection
import uuid
import sys
sys.dont_write_bytecode = True


class Seasons(): 

  @classmethod 
  def getseasonAlldata(cls,lan):
        try:
            connection, cursor = openDbconnection()
            if lan == '1' :
                cursor.execute(
                    "SELECT uuid as season_uuid,name_en as name,image FROM m_season"
                )
            elif lan == '2':
                 cursor.execute(
                    "SELECT uuid as season_uuid,name_hi as name,image FROM m_season"
                )
            elif lan == '3':
                 cursor.execute(
                    "SELECT uuid as season_uuid,name_mr as name,image FROM m_season"
                )
            account = cursor.fetchall()
            print(account)
            cursor.close()
            connection.close()
            
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e
  
  @classmethod 
  def getsearch_crop_data(cls,text):
        print(text)
        text = text+'%'
        try:
            connection, cursor = openDbconnection()
            print(text)
            if text:
                    cursor.execute(
                            
                            """SELECT uuid as crop_uuid,name_en,name_hi, name_mr, desc_en, desc_hi, desc_mr, image, status
                            FROM m_crop WHERE  name_en LIKE %s OR name_hi LIKE %s  OR name_mr LIKE %s""",(text,text,text)
                        ) 
            account = cursor.fetchall()
            cursor.close()
            connection.close()
            
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e
  @classmethod 
  def getsearch_season_data(cls,text):
        print(text)
        text = text+'%'
        try:
            connection, cursor = openDbconnection()
            print(text)
            if text:
                    cursor.execute(
                            
                            """SELECT  uuid as season_uuid, name_en, name_hi, name_mr, desc_en, desc_hi, desc_mr, image, status
                            FROM m_season WHERE  name_en LIKE %s OR name_hi LIKE %s  OR name_mr LIKE %s""",(text,text,text)
                        )
            account = cursor.fetchall()
            print(account,'details')
            cursor.close()
            connection.close()
            
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e
  @classmethod 
  def getsearch_advisorylist(cls,text):
        print(text)
        text = text+'%'
        try:
            connection, cursor = openDbconnection()
            print(text)
            if text:
                      cursor.execute(
                            
                            """SELECT uuid as crop_uuid,uuid, uuid_tehsil, category_en, category_hi, category_mr, title_en, title_hi, title_mr, desc_en, desc_hi, desc_mr, image, address_en, address_hi, address_mr, geo_lat, geo_lng, status
                            FROM advisory WHERE title_en LIKE %s OR title_hi LIKE %s  OR title_mr LIKE %s """,(text,text,text)
                        )
            account = cursor.fetchall()
            print(account,'details')
            cursor.close()
            connection.close()
            
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e
  
  @classmethod 
  def getseaarch_goverschemelist(cls,text):
        print(text)
        text = text+'%'
        try:
            connection, cursor = openDbconnection()
            print(text)
            if text:
                    cursor.execute(
                            
                          """SELECT uuid as scheme_uuid,uuid_tehsil, category_en, category_hi, category_mr, title_en, title_hi, title_mr, desc_en, desc_hi, desc_mr, image, weblink, downloadlink, status
                            FROM govt_scheme WHERE  title_en LIKE %s OR title_hi LIKE %s  OR title_mr LIKE %s""",(text,text,text)
                       )
            account = cursor.fetchall()
            print(account,'details')
            cursor.close()
            connection.close()
            
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e 
  @classmethod 
  def bookmark_add(cls,uuid,fav):
        try:
            cursor.execute(
                """SELECT name_en,name_hi,name_mr, FROM m_crop"""
            )
            account = cursor.fetchall()
            cursor.close()
            connection.close()
            
            
            connection, cursor = openDbconnection()
            bookmark_uuid = str(uuid.uuid4())
            cursor.execute(
                    "INSERT INTO bookmark (uuid,fav,uuid_crop) VALUES (  % s, %s, % s)",
                    (
                      uuid,
                      fav  
                    )
                )
            connection.commit()
            account = cursor.fetchone()
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e

  @classmethod
  def remove_bookMark(cls,uuid,fav):
        try:
            connection,cursor = openDbconnection()
            cursor.execute(""" update bookmark set fav=%s, where uuid = %s """,(fav,uuid))
            cursor.close()
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            raise ValueError(str(e))
        

  @classmethod
  def User(cls,**user):
        try:
            connection, cursor = openDbconnection()
            user_uuid = str(uuid.uuid4())
            cursor.execute(
                    "INSERT INTO user(uuid,name,phonenumber,email,address1,address2,uuid_tehsil,geo_lat,geo_lng) VALUES (  % s,% s, % s, % s,% s, % s, % s, % s, % s)",
                    (
                     user_uuid,
                     user['name'],
                     user['phonenumber'],
                     user['email'],
                     user['address1'],
                     user['address2'],
                     user['uuid_tehsil'],
                     user['geo_lat'],
                     user['geo_lng']
                            
                    )
                )
            connection.commit()
            account = cursor.fetchone()
            if account:
               return account
            else: 
                return False        
        except Exception as e:
         return e

  @classmethod
  def Userdevice(cls,**userdevice):
        print(userdevice)
        try:
            connection, cursor = openDbconnection()
            user_uuid = str(uuid.uuid4())
            cursor.execute(
                    "INSERT INTO user_device (uuid,uuid_user,device_id,device_name,device_model,platform_type,os_version,fcm_token) VALUES (  % s,% s, % s, % s,% s, % s, % s, % s)",
                    (
                     user_uuid,
                     userdevice['uuid_user'],
                     userdevice['device_id'],
                     userdevice['device_name'],
                     userdevice['device_model'],
                     userdevice['platform_type'],
                     userdevice['os_version'],
                     userdevice['fcm_token'],
                    
                            
                    )
                )
            connection.commit()
            account = cursor.fetchone()
            if account:
               return account
            else: 
                return False        
        except Exception as e:
         return e


  @classmethod 
  def getstate(cls,lan):
        try:
            connection, cursor = openDbconnection()
            if lan == '1' :
                cursor.execute(
                    "SELECT uuid as state_uuid,state_en as name FROM loc_state"
                )
            elif lan == '2':
                 cursor.execute(
                    "SELECT uuid as state_uuid,state_hi as name FROM loc_state"
                )
            elif lan == '3':
                 cursor.execute(
                    "SELECT uuid as state_uuid,state_mr as name FROM loc_state"
                )
            account = cursor.fetchall()
            print(account)
            cursor.close()
            connection.close()
            
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e
        
  @classmethod 
  def getdistrict(cls,lan,uuid_state):                                       
        
        try:
            connection, cursor = openDbconnection()
            if lan == '1' :
                cursor.execute(
                    "SELECT uuid as district_uuid,district_en as name FROM loc_district WHERE uuid_state  = % s",(uuid_state)
                )
            elif lan == '2':
                 cursor.execute(
                    "SELECT uuid as district_uuid,district_hi as name FROM loc_district WHERE uuid_state  = % s",(uuid_state)
                )
            elif lan == '3':
                 cursor.execute(
                    "SELECT uuid as district_uuid,district_mr as name FROM loc_district WHERE uuid_state  = % s",(uuid_state)
                )
            account = cursor.fetchall()
            print(account)
            cursor.close()
            connection.close()
            
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e
    
  @classmethod 
  def gettehsil(cls,lan,uuid_district):                                       
        
        try:
            print(uuid_district) 
            
            connection, cursor = openDbconnection()
            if lan == '1' :
                cursor.execute(
                    "SELECT uuid as tehsil_uuid,tehsil_en as name FROM loc_tehsil WHERE uuid_district  = % s",(uuid_district)
                )
            elif lan == '2':
                 cursor.execute(
                    "SELECT uuid as tehsil_uuid,tehsil_hi as name FROM loc_tehsil WHERE uuid_district  = % s",(uuid_district)
                )
            elif lan == '3':
                 cursor.execute(
                    "SELECT uuid as tehsil_uuid,tehsil_mr as name FROM loc_tehsil WHERE uuid_district  = % s",(uuid_district)
                )
            account = cursor.fetchall()
            print(account)
            cursor.close()
            connection.close()
            
            if account:
                return account
            else:
                return False
        except Exception as e:
            return e




