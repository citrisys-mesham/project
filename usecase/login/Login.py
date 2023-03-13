from flask import Blueprint, request, render_template, session, redirect, url_for
from repositories.login.login import LoginRepo
from dto.request.login.login import LoginRequest

class LoginUsecase:

    def __init__(self, repo=LoginRepo):
        self.repo= repo

    def handle(self, request:LoginRequest):
        
           data=self.repo.get_data(request.username,request.password)
           print("handledata",data)
           return data        
      
