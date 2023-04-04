from repositories.login.signup import SignupRepo 
from dto.request.login.signup import SignupRequest




class SignupUsecase:

    def __init__(self, repo=SignupRepo):
        self.repo= repo

    def handle(self, request:SignupRequest):
        
           data=self.repo.insert(request)
           print("handledata",data)
           return data        
      