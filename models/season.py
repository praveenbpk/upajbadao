from utilities.helpers import openDbconnection
import uuid



class Seasons(): 

  @classmethod 
  def getseasonAlldata(cls):
        try:
            connection, cursor = openDbconnection()
            cursor.execute(
                """SELECT name_en,name_hi,name_mr,image FROM m_season"""
            )
            account = cursor.fetchall()
            cursor.close()
            connection.close()
            cursor.execute(
                """SELECT name_en,name_hi,name_mr,image FROM m_season"""
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