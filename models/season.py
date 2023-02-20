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
    def getcrop(uuid,lan):
        try:
            connection,cursor=openDbconnection()
            if lan=='1':
               cursor.execute(""" SELECT uuid,name_en,desc_en, status, created_at, updated_at
                 FROM m_crop where uuid=%s  """,(uuid))
            elif lan=='2':
                cursor.execute(""" SELECT uuid,name_hi,desc_hi, status, created_at, updated_at
                 FROM m_crop where uuid=%s """,(uuid))
            elif lan=='3':
                cursor.execute(""" SELECT uuid,name_mr,desc_mr,status, created_at, updated_at
                 FROM m_crop where uuid=%s """,(uuid))
            rows=cursor.fetchone()
            cursor.close()
            connection.close()
            if rows:
                return rows
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
            
