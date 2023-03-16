from repositories.ibase import IBaseRepository

class RoomRepo(IBaseRepository):
    def insert():
        sql="""
        insert into room (pro_id,room_type,bed_count,room_capacity,bathroom)
        values(%s,%s,%s,%s,%s)"""

        