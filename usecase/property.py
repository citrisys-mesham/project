from repositories.property import PropertyRepo
from dto.request.property import AddPropertyRequest
class PropertyCase():
    def __init__(self,repo:PropertyRepo) -> None:
        self.repo=repo


    def use_case(self,request:AddPropertyRequest):
        
        case=self.repo.insert(request)

        return case