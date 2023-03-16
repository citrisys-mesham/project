from flask import Blueprint,request,json,jsonify
from dto.request.room import RoomRequest
from usecase.room import RoomCase
from repositories.room import RoomRepo
room_blueprint=Blueprint('room_blueprint',__name__)

@room_blueprint.route('/room',methods=['POST'])

def insert_room():
    data=json.loads(request.get_data())
    print(data)
    room_request=RoomRequest(**data)
    
    room_repo=RoomRepo()
    case=RoomCase(room_repo)
    out=case.use(room_request)
    return jsonify(out)