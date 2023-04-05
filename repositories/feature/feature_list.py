from repositories.ibase import IBaseRepository
from flask import request

class FeatureListRepo(IBaseRepository):
    def get_feature(self):
        sql="select list_id,feature_list from feature_list"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.conn.commit()

        return result
    
    def save_feature(self,features):
         print("save feature",features)

         
         if isinstance(features, list):
    # Use the list as is
            values = [(f.strip(),) for f in features]
         else:
    # Split the string into a list
             features = features.split(",")
             values = [(f.strip(),) for f in features]

         sql = """
     INSERT INTO select_feature (feature)
     VALUES (%s)
    """
         self.cursor.executemany(sql, values)
         self.conn.commit()
         print('features inserted')


        #  features = feature.select_feature 
        #  if isinstance(feature.select_feature, list) 
        #    else feature.select_feature.split(",")
        #  values = [(f.strip(),) for f in features]
        #  sql = """
        #  INSERT INTO select_feature (feature)
        #  VALUES (%s)
        # """
        #  self.cursor.executemany(sql, values)
        #  self.conn.commit()
        #  print('features inserted')
         
