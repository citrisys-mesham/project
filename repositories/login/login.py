from repositories.ibase import IBaseRepository



class LoginRepo(IBaseRepository):

    # def __init__(self):
    #     sql="select username,password from login"
    #     self.cursor.execute(sql)
    #     self.result=self.cursor.fetchall()
    #     self.conn.commit()

    #     return self.result





    def get_data(self,username=str,password=str):
        sql="select username,password from login"
        self.cursor.execute(sql)
        self.result=self.cursor.fetchall()
        self.conn.commit()  

        print("loginusername",type(username),username,password)
        self.new = []
        for data in self.result:
           if data[0] == username:
               if data[1]==password:
                   print("checkdata",data)
                   return data
               return self.new
        return self.new    