from flask import Flask, request, Blueprint, render_template, redirect, url_for
from repositories.login.forgot_password import ForgotRepository
from dto.request.login.forgot_password import UpdateForgotRequest

class ForgotPasswordUsecase:
    def __init__(self, repo: ForgotRepository):
        self.repo = repo
        print("repo1", repo)

    def handle(self, request: UpdateForgotRequest):
        data = self.repo.get_data(request)
        print("*startdata", data)
        if len(data) == 0:
            print("html")
            return data
        else:
            data = self.repo.update(request) 
            print("usedata", data)
            return data
