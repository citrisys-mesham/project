from dto.request.login.forgot_password import UpdateForgotRequest
from entities.login.forgot_password import Forgot
from repositories.ibase import IBaseRepository



    #  def get_data(self,username=str,password=str):
    
    #     sql="select username,password from login"
    #     self.cursor.execute(sql)
    #     self.result=self.cursor.fetchall()
    #     self.conn.commit()  

    #     print("loginusername",type(username),username,password)
    #     self.new = []
    #     for data in self.result:
    #         if data[0] == username:
    #               print("username",username)
    #               print("datacheck",data)
    #               return data[0]
    #         print("dfhjkhgfh",data[0])
    #         return self.new    
     
class ForgotRepository(IBaseRepository):
    def get_data(self,request:UpdateForgotRequest):
        sql = "select username, password from login"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        self.conn.commit()

        
        self.new = []
        for data in self.result:
            print("check67868", data[0])
            if data[0] == request.username:
                #print("username", username)
                print("datacheck", data)
                return data[0]
        else:
                print("dfhjkhgfh", data[0])
                return self.new

     
    def update(self,request:UpdateForgotRequest):
        print("insert")
        sql="update login set password=%s where username=%s"
        
        Forgot1= Forgot(
            username=request.username,
            password=request.password,
            
        )
        val = (
            Forgot1.password,
            Forgot1.username
            
        )

        self.cursor.execute(sql,val)
        print('r5')
        self.conn.commit()
       
        return val