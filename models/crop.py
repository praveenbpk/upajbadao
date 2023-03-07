from utilities.helpers import openDbconnection
import uuid
import sys
sys.dont_write_bytecode = True



class Get_season():
    @classmethod
    def getseason(cls,uuid,lan):
        try:
            connection,cursor=openDbconnection()
            if lan=='1':
               cursor.execute(""" SELECT m_crop.uuid,m_crop.name_en,m_crop.desc_en, m_crop.status,m_crop.image, CAST(m_crop.created_at as CHAR)as created_at,
                CAST(m_crop.updated_at as char)as updated_at
                FROM recomm_crop join m_crop on 
                recomm_crop.uuid_crop=m_crop.uuid  where uuid_season=%s  """,(uuid))
            elif lan=='2':
                cursor.execute(""" SELECT m_crop.uuid,m_crop.name_hi,m_crop.desc_hi, m_crop.status,m_crop.image, CAST(m_crop.created_at as CHAR)as created_at,
                CAST(m_crop.updated_at as char)as updated_at
                FROM recomm_crop join m_crop on 
                recomm_crop.uuid_crop=m_crop.uuid  where uuid_season=%s  """,(uuid))
            elif lan=='3':
                cursor.execute(""" SELECT m_crop.uuid,m_crop.name_hi,m_crop.desc_hi, m_crop.status,m_crop.image, CAST(m_crop.created_at as CHAR)as created_at,
                CAST(m_crop.updated_at as char)as updated_at
                FROM recomm_crop join m_crop on 
                recomm_crop.uuid_crop=m_crop.uuid  where uuid_season=%s  """,(uuid))
            rows=cursor.fetchall()
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


