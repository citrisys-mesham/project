from dataclasses import dataclass

@dataclass
class Room():
    pro_id:int
    room_type:str
    bed_count:int
    room_capacity:int
    bathroom:int
    