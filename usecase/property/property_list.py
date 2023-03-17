from repositories.property.property_list import PropertyListRepo

class PropertyListCase():
    def __init__(self,repo=PropertyListRepo) -> None:
        self.repo=repo

    def get(self):
        result=self.repo.get_property()
        
        return result    
        