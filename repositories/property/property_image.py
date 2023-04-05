from repositories.ibase import IBaseRepository
from flask import request
from werkzeug.utils import secure_filename




class imageRepo(IBaseRepository):
    def insert(self):
        print("insert")
        # sql="""
        # insert into image(image)values(%s);
        # """
        profile_picture=f"/static/image/property/{secure_filename((request.files['files']).filename)}"
        print("profile_image",profile_picture)

        # self.cursor.execute(sql,(profile_picture,))
        # self.conn.commit()
        return profile_picture
    

    def save_image(self,image):
        print("save image",type(image))
        print("save image",image)


        sql="""
        insert into image(image)values(%s);
        """

        self.cursor.execute(sql,(image,))
        self.conn.commit()

        print ("image inserted")
