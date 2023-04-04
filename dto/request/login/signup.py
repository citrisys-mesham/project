import dataclasses


@dataclasses.dataclass
class SignupRequest:
    
    username:str
    password:str