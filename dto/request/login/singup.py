import dataclasses


@dataclasses.dataclass
class SingupRequest:
    
    username:str
    password:str