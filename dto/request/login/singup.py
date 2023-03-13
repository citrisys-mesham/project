import dataclasses


@dataclasses.dataclass
class SingupRequest:
    print("SingupRequest")
    username:str
    password:str