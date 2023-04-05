from repositories.ibase import IBaseRepository


class PropertyListRepo(IBaseRepository):
    def get_property(self):
        sql="select pro_id,pro_name from property"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.conn.commit()

        return result
    
    def save_property(self,name):
        print("save property",type(name))
        print("save property",name)
        
    
        sql="""
           insert into selected_property(pro_name)
           values(%s)
        """

        self.cursor.execute(sql,(name,))
        self.conn.commit()

        print ("property inserted")