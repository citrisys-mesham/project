import dataclasses
from entities.login import Login

@dataclasses.dataclass
class LoginRequest:
    print("jghg")
    username:str
    password:str