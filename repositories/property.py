from dto.request.property import AddPropertyRequest
from entities.property import Property
from repositories.ibase import IBaseRepository
class PropertyRepo(IBaseRepository):
    
    def insert(self,request:AddPropertyRequest):

       sql="""
           insert into property(contact_id,pro_name,pro_description,rating)
           values(%s,%s,%s,%s)
       """
       value=Property(
         contact_id=request.contact_id,
         pro_name=request.pro_name,
         pro_description=request.pro_description,
         rating=request.rating 
        )
       
       tuple_value=tuple(value.__dict__.values())

       self.cursor.execute(sql,tuple_value)
       self.conn.commit()

       return value

