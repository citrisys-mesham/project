from flask import Blueprint,current_app,request
from werkzeug.utils import secure_filename
import os


property_image_blueprint=Blueprint('property_image_blueprint',__name__)

@property_image_blueprint.route('/')

def proImage():
    current_app.config['UPLOAD_FOLDER'] ="/home/whirldata/Documents/new/projectnew/project/static/image/property_image"
    picture_url=request.files['profile_picture']
    filename = secure_filename(picture_url.filename)
    print(filename)
    # print("image",profile_picture)
    picture_url.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(picture_url.filename)))
    return "profile_image"