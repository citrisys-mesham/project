from flask import Blueprint,request,json,jsonify,render_template,redirect,url_for,session
from dto.request.room import RoomRequest
from usecase.room import RoomCase
from repositories.room import RoomRepo

room_blueprint=Blueprint('room_blueprint',__name__)

@room_blueprint.route('/room',methods=['POST'])

def insert_room():
    room =request.form["room_type"]
    bed =request.form["bed_count"]
    capacity=request.form["room_capacity"]
    bath =request.form["bathroom"]
    # print("insert room")
    # data = request.form.to_dict()

    # print("roomdata",data)
    # data=json.loads(data1)
    # print("roomdata",data1)
    room_request=RoomRequest(room,bed,capacity,bath)
    
    room_repo=RoomRepo()
    case=RoomCase(room_repo)
    Roomout=case.use(room_request)
    # return redirect(url_for('api_blueprint.feature_list_blueprint.all'))

    session['Roomout']=Roomout
    print ("output2", Roomout)
    return redirect (url_for("api_blueprint.review_blueprint.getroom"))