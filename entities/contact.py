from dataclasses import dataclass


@dataclass
class Conduct:
    door_number:str
    street_name:str
    city:str
    state:str
    country:str
    zip_code:str
    phone_number:str
    email:str
    
    