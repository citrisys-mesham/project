from dataclasses import dataclass


@dataclass
class UpdateForgotRequest:
    username: str
    password: str
    
