from dto.request.forgot import UpdateForgotRequest
from entities.forgot import Forgot
from repositories.ibase import IBaseRepository


class ForgotRepository(IBaseRepository):
     def get_data(self,username=str,password=str):
    
        sql="select username,password from login"
        self.cursor.execute(sql)
        self.result=self.cursor.fetchall()
        self.conn.commit()  

        print("loginusername",type(username),username,password)
        self.new = []
        for data in self.result:
           if data[0] == username:
            
               return data
        return self.new    
     
     
     def update(self,request:UpdateForgotRequest):
        print("insert")
        sql="update login set password=%s where username=%s"
        
        

        Forgot1= Forgot(
            username=request.username,
            password=request.password,
            
        )
        print("forgot1",Forgot1)
        val = (
            Forgot1.password,
            Forgot1.username
            
        )
        print("checkval",val)

        self.cursor.execute(sql,val)
        print('r5')
        self.conn.commit()
       
        return val
  