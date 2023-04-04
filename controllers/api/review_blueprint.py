from flask import Blueprint,request,render_template,redirect,session,url_for

# contact_blueprint=Blueprint('contact_blueprint',__name__)
review_blueprint=Blueprint('review_blueprint',__name__)




@review_blueprint.route('/getcontact')
def getcontact():
    print("getcontact")

    output = session.get('output')
    print ("getcontact",output)
    # return redirect('/api/review/showproperty')
    # return render_template('room.html')
    return redirect('/api/property_list/all')

@review_blueprint.route('/getproperty', methods=['POST'])

def getproperty():
    name = request.form['property']
    session['property'] = name
    print ("get property",name)
    return redirect('/api/feature_list/all')


@review_blueprint.route('/getfeature', methods=['POST'])

def getfeature():
    fea =request.form.getlist('features')
    session['features'] = fea
    print ("get features",fea)
    # return redirect('/api/review/showproperty')
    return render_template('room.html')


   
@review_blueprint.route('/getroom')
def getroom():
    print("getroom")
    Room = session.get('Roomout')
    print ("getcontact",Room)
    # return redirect('/api/review/showproperty')
    return render_template("property_image.html")

@review_blueprint.route('/geimage')
def getimage():
    print("getimage")
    image = session.get('image')
    print ("getcontact",image)
    return redirect('/api/review/showproperty')

@review_blueprint.route('/showproperty')

def showproperty():
    name = session.get('property')
    fea = session.get('features')
    output = session.get('output')
    Room = session.get('Roomout')
    image = session.get('image')
    print ("show property",name ,fea)
    return render_template('review.html', property=name ,feature=fea,conduct=output,Room=Room,image=image)
