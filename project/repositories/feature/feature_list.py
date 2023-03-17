from repositories.ibase import IBaseRepository


class FeatureListRepo(IBaseRepository):
    def get_feature(self):
        sql="select list_id,feature_list from feature_list"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.conn.commit()

        return result

        