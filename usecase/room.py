from repositories.room import RoomRepo
from dto.request.room import RoomRequest
class RoomCase():
    def __init__(self,repo:RoomRepo) -> None:
        self.repo=repo
    def use(self,request:RoomRequest):
        result=self.repo.insert(request)
        return result