from dto.request.property_get import AddPropertyRequest
from entities.property_get import Property
from repositories.ibase import IBaseRepository
class PropertyRepo(IBaseRepository):
    
    def insert(self,request:AddPropertyRequest):
        property=Property(pro_name=request.pro_name)
        Property1=property.pro_name if isinstance(property.pro_name, list) else property.pro_name.split(",")
        values = [(f.strip(),) for f in Property1]

        sql="""
           insert into selected_property(pro_name)
           values(%s)
        """

        self.cursor.executemany(sql,values)
        self.conn.commit()

        return values
