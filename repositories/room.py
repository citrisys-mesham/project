from repositories.ibase import IBaseRepository
from entities.room import Room
from dto.request.room import RoomRequest
class RoomRepo(IBaseRepository):
    def insert(self,request:RoomRequest):
        # sql="""
        # insert into room (room_type,bed_count,room_capacity,bathroom)
        # values(%s,%s,%s,%s)"""
        val=Room(
           
            room_type=request.room_type,
            bed_count=request.bed_count,
            room_capacity=request.room_capacity,
            bathroom=request.bathroom
        )
        # val1=tuple(val.__dict__.values())
        # self.cursor.execute(sql,val1)
        # self.conn.commit()
        return val
