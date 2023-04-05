from flask import Blueprint,session
from repositories.property.property_list import PropertyListRepo
from repositories.feature.feature_list import FeatureListRepo
from repositories.contact import ContactRepo
from repositories.room import RoomRepo
from repositories.property.property_image import imageRepo

save_blueprint=Blueprint('save_blueprint',__name__)

@save_blueprint.route('/save', methods=['POST'])

def save():
    name = session.get('property')
    fea = session.get('features')
    contact = session.get('output')
    Room = session.get('Roomout')
    image = session.get('image')
    

    print("name",name)
    namerepo= PropertyListRepo()
    namerepo.save_property(name)
    fearepo=FeatureListRepo()
    fearepo.save_feature(fea)
    conrepo=ContactRepo()
    conrepo.save_contact(contact)
    room=RoomRepo()
    room.save_room(Room)

    imgrepo= imageRepo()
    imgrepo.save_image(image)
    
    return "all data saved"