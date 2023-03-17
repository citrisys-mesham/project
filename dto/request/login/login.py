import dataclasses


@dataclasses.dataclass
class LoginRequest:
   
    username:str
    password:str