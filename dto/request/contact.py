from dataclasses import dataclass
from .ibase import IBaseRequest

@dataclass


class AddContactRequest(IBaseRequest):
     print("ok")
     door_number:str
     street_name:str
     city:str
     state:str
     country:str
     zip_code:str
     phone_number:str
     email:str

     def __post_init__(self):
          if not self.door_number:
               return ValueError ("You missed the door number")
          elif not self.street_name:
               return ValueError ("You missed the street name")
          elif not self.city:
               return ValueError ("You missed the city")
          elif not self.state:
               return ValueError ("You missed the state")
          elif not self.country:
               return ValueError ("You missed the country")
          elif not self.zip_code:
               return ValueError ("You missed the zip code")
          elif not self.phone_number:
               return ValueError ("You missed the phone number")
          elif not self.email:
               return ValueError ("You missed the email")
          