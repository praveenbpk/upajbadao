from utilities.helpers import openDbconnection
import uuid
import sys
sys.dont_write_bytecode = True




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
        
            