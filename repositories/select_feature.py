from dto.request.select_feature import FeatureReq
from .ibase import IBaseRepository
from entities.select_feature import Feature

class SelectFeatureRepo(IBaseRepository):
    def insert(self, request: FeatureReq):
        feature = Feature(select_feature=request.select_feature)
        features = feature.select_feature if isinstance(feature.select_feature, list) else feature.select_feature.split(",")
        values = [(f.strip(),) for f in features]
        sql = """
        INSERT INTO select_feature (feature)
        VALUES (%s)
        """
        self.cursor.executemany(sql, values)
        self.conn.commit()
        print('Inserted successfully')
        return values
