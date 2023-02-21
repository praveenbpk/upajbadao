from utilities.helpers import openDbconnection
import  re
import uuid




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
        try:
            connection, cursor = openDbconnection()
            user_uuid = str(uuid.uuid4())
            cursor.execute(
                    "INSERT INTO user_device(uuid,uuid_user,device_id,device_name,device_model,platform_type,os_version,fcm_token) VALUES (  % s,% s, % s, % s,% s, % s, % s, % s)",
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
class Get_season():
    @classmethod
    def getseason(cls,uuid,lan):
        try:
            connection,cursor=openDbconnection()
            if lan=='1':
               cursor.execute(""" SELECT uuid,name_en,desc_en, status, created_at, updated_at
                 FROM m_season where uuid=%s  """,(uuid))
            elif lan=='2':
                cursor.execute(""" SELECT uuid,name_hi,desc_hi,status, created_at, updated_at
                 FROM m_season where uuid=%s """,(uuid))
            elif lan=='3':
                cursor.execute(""" SELECT uuid,name_mr,desc_mr,status, created_at, updated_at
                 FROM m_season where uuid=%s """,(uuid))
            rows=cursor.fetchone()
            cursor.close()
            connection.close()
            if rows:
                return rows
            else:
                False
        except Exception as e:
            raise ValueError(str(e))
        
    @classmethod    
    def getcrop(cls,uuid,lan):
        try:
            connection,cursor=openDbconnection()
            if lan=='1':
               cursor.execute(""" SELECT name_en as crop_name from m_crop where uuid=%s""",uuid)
               crop=cursor.fetchone()
               print(crop)
               cursor.execute(""" SELECT uuid from recomm_crop where uuid_crop=%s""",uuid)
               r_uuid=cursor.fetchone()

               cursor.execute(""" SELECT recomm_content.content1_type,recomm_content.content1_en,recomm_content.content2_type,
                recomm_content.content2_en, recomm_content.content3_type,recomm_content.content3_en,recomm_content.title_en,
                recomm_content.uuid_recomm_category from recomm_content 
                join recomm_crop on recomm_content.uuid_recomm_crop= recomm_crop.uuid
                where recomm_content.uuid_recomm_crop=%s""",r_uuid['uuid'])
               content=cursor.fetchall()
               for x in range(0,len(content)):
                   cursor.execute(""" SELECT name_en as cate_name,uuid as cid from recomm_category where uuid=%s""",content[x]['uuid_recomm_category'])
                   c_name=cursor.fetchall()

            if lan=='2':
               cursor.execute(""" SELECT name_hi as crop_name from m_crop where uuid=%s""",uuid)
               crop=cursor.fetchone()
               print(crop)
               cursor.execute(""" SELECT uuid from recomm_crop where uuid_crop=%s""",uuid)
               r_uuid=cursor.fetchone()

               cursor.execute(""" SELECT recomm_content.content1_type,recomm_content.content1_hi,recomm_content.content2_type,
                recomm_content.content2_hi, recomm_content.content3_type,recomm_content.content3_hi,recomm_content.title_hi,
                recomm_content.uuid_recomm_category from recomm_content 
                join recomm_crop on recomm_content.uuid_recomm_crop= recomm_crop.uuid
                where recomm_content.uuid_recomm_crop=%s""",r_uuid['uuid'])
               content=cursor.fetchall()
               for x in range(0,len(content)):
                   cursor.execute(""" SELECT name_hi as cate_name,uuid as cid from recomm_category where uuid=%s""",content[x]['uuid_recomm_category'])
                   c_name=cursor.fetchall()

            if lan=='3':
               cursor.execute(""" SELECT name_mr as crop_name from m_crop where uuid=%s""",uuid)
               crop=cursor.fetchone()
               print(crop)
               cursor.execute(""" SELECT uuid from recomm_crop where uuid_crop=%s""",uuid)
               r_uuid=cursor.fetchone()

               cursor.execute(""" SELECT recomm_content.content1_type,recomm_content.content1_mr,recomm_content.content2_type,
                recomm_content.content2_mr, recomm_content.content3_type,recomm_content.content3_mr,recomm_content.title_mr,
                recomm_content.uuid_recomm_category from recomm_content 
                join recomm_crop on recomm_content.uuid_recomm_crop= recomm_crop.uuid
                where recomm_content.uuid_recomm_crop=%s""",r_uuid['uuid'])
               content=cursor.fetchall()
               for x in range(0,len(content)):
                   cursor.execute(""" SELECT name_mr as cate_name,uuid as cid from recomm_category where uuid=%s""",content[x]['uuid_recomm_category'])
                   c_name=cursor.fetchall()       

            cursor.close()
            connection.close()
            if content and crop and c_name:
                return crop,c_name,content
            else:
                False
        except Exception as e:
            raise ValueError(str(e))


class Get_advisory():
    @classmethod
    def getadvisory(cls,uuid,lan):
        try:
            connection,cursor=openDbconnection()
            if lan=='1':
               cursor.execute(""" select tags_en from advisory""")
               tag=cursor.fetchone()
               print(tag)
               tag_en=[]
               cursor.execute(""" SELECT uuid, uuid_tehsil, category_en, title_en,desc_en,  
                image, address_en,  geo_lat, geo_lng, status,created_at, updated_at
                FROM advisory where uuid_tehsil=%s  """,(uuid))
               rows=cursor.fetchall()
               tags=tag['tags_en']
               tags = str(tags)
               tags = tags.split(',')
               print(tags)
               
               print(type(tags))
               tag_en.append(tags)
               for x in range(0,len(rows)):
                   rows[x]['tags']=tag_en
                      

            elif lan=='2':
                cursor.execute(""" select tags_hi from advisory""")
                tag=cursor.fetchone()
                tag_hi=[]
            
                cursor.execute(""" SELECT uuid, uuid_tehsil, category_hi, title_hi,desc_hi,  
                image, address_hi,  geo_lat, geo_lng, status,created_at, updated_at
                FROM advisory where uuid_tehsil=%s  """,(uuid))
                rows=cursor.fetchall()
                tags=tag['tags_hi']
                tags = str(tags)
                tags = tags.split(',') 
                print(tags)
                tag_hi.append(tags)
                for x in range(0,len(rows)):
                   rows[x]['tags']=tag_hi

            elif lan=='3':
                cursor.execute(""" select tags_mr from advisory""")
                tag=cursor.fetchone()
                tags_mr=[]

                cursor.execute(""" SELECT uuid, uuid_tehsil, category_mr, title_mr,desc_mr,  
                image, address_mr,  geo_lat, geo_lng, status,created_at, updated_at
                FROM advisory where uuid_tehsil=%s  """,(uuid))
                rows=cursor.fetchall()
                tags=tag['tags_mr']
                tags = str(tags)
                tags = tags.split(',')
                tags_mr.append(tags)
                for x in range(0,len(rows)):
                   rows[x]['tags']=tags_mr

            cursor.close()
            connection.close()
            if rows and tag:
                return rows[x]
            else:
                False
        except Exception as e:
            raise ValueError(str(e))
        
            
class Get_scheme():
    @classmethod
    def getscheme(cls,uuid,lan):
        try:
            connection,cursor=openDbconnection()
            if lan=='1':
               cursor.execute(""" SELECT uuid, uuid_tehsil, category_en, title_en,desc_en,  
                tags_en,image, status,created_at, updated_at
                FROM govt_scheme where uuid_tehsil=%s  """,(uuid))
               
            elif lan=='2':
                cursor.execute(""" SELECT uuid, uuid_tehsil, category_hi, title_hi,desc_hi,  
                tags_hi,image,status,created_at, updated_at
                FROM govt_scheme where uuid_tehsil=%s  """,(uuid))

            elif lan=='3':
                cursor.execute(""" SELECT uuid, uuid_tehsil, category_mr, title_mr,desc_mr,  
                tags_mr,image,status,created_at, updated_at
                FROM govt_scheme where uuid_tehsil=%s  """,(uuid))

            rows=cursor.fetchone()
            cursor.close()
            connection.close()
            if rows:
                return rows
            else:
                False
        except Exception as e:
            raise ValueError(str(e))
            
