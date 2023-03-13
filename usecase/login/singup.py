from repositories.login.singup import SingupRepo 
from dto.request.login.singup import SingupRequest




class SingupUsecase:

    def __init__(self, repo=SingupRepo):
        self.repo= repo

    def handle(self, request:SingupRequest):
        
           data=self.repo.insert(request)
           print("handledata",data)
           return data        
      