from repositories.select_feature import SelectFeatureRepo
from dto.request.select_feature import FeatureReq
class SelectFeatureUse():
    def __init__(self,repo:SelectFeatureRepo) -> None:
        self.repo=repo

    def data_case(self,request:FeatureReq):
        case=self.repo.insert(request)    
        return case