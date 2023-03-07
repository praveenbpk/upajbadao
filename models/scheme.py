from utilities.helpers import openDbconnection
import uuid
import sys
sys.dont_write_bytecode = True





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
            