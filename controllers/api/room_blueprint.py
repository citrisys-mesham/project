from flask import Blueprint,request


room_blueprint=Blueprint('room_blueprint',__name__)

@room_blueprint.route('/room',methods=['POST'])

def insert_room():
    data=request.get_data()
    print(data)
    return data