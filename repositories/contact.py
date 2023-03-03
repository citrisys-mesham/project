from dto.request.contact import AddContactRequest
from entities.contact import Conduct
from repositories.ibase import IBaseRepository


class ContactRepo(IBaseRepository):
    def insert(self,request:AddContactRequest):
        
        sql="""
        insert into contact(door_number,street_name,city,state,country,zip_code,phone_number,email)
        values(%s,%s,%s,%s,%s,%s,%s,%s)
        """

        contact_val=Conduct(
            door_number=request.door_number,
            street_name=request.street_name,
            city=request.city,
            state=request.state,
            country=request.country,
            zip_code=request.zip_code,
            phone_number=request.phone_number,
            email=request.email
            
        )
        
        val=tuple(contact_val.__dict__.values())
        self.cursor.execute(sql,val)
        print('r5')
        self.conn.commit()
       
        return contact_val
