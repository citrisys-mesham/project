from repositories.ibase import IBaseRepository


class PropertyListRepo(IBaseRepository):
    def get_property(self):
        sql="select pro_id,pro_name from property"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.conn.commit()

        return result

        