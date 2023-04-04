from repositories.contact import ContactRepo
from dto.request.contact import AddContactRequest
from entities.contact import Conduct

class ContactUseCase():
    def __init__(self,repo:ContactRepo) -> None:
        self.repo=repo


    def handle(self,request:AddContactRequest)->Conduct:
        print("handle up")
        result=self.repo.insert(request)
        print("handle",type(result))
        return result    
