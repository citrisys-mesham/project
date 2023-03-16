from repositories.feature.feature_list import FeatureListRepo

class FeatureListCase():
    def __init__(self,repo=FeatureListRepo) -> None:
        self.repo=repo

    def get(self):
        result=self.repo.get_feature()
        return result    
        