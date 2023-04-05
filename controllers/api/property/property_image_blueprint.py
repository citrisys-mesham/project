from flask import Blueprint,current_app,request,session,redirect,url_for
from werkzeug.utils import secure_filename
import os
from repositories.property.property_image import imageRepo


property_image_blueprint=Blueprint('property_image_blueprint',__name__)

@property_image_blueprint.route('/image',methods=['POST'])

def proImage():
    print("image")
    current_app.config['UPLOAD_FOLDER'] ="/home/lenovo/Desktop/cookies/project/static/image/property"
    picture_url=request.files['files']
    print(picture_url)
    filename = secure_filename(picture_url.filename)
    print(filename)
    # print("image",profile_picture)
    picture_url.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(picture_url.filename)))
    repo=imageRepo()
    image=repo.insert()
    session ['image']=image
    return redirect (url_for("api_blueprint.review_blueprint.getimage"))