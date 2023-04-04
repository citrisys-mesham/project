from repositories.ibase import IBaseRepository
from dto.request.login.signup import SignupRequest
from entities.login.signup import signup

class SignupRepo(IBaseRepository):

    def insert(self,add_daties:SignupRequest):
        new_daties= signup(
            username=add_daties.username,
            password=add_daties.password

        )

        val=(
            new_daties.username,
            new_daties.password
        )
        print("new_daties",new_daties,type(new_daties))
        print("val",new_daties,type(new_daties))
        sql="insert into login values(%s,%s)"
        self.cursor.execute(sql,val)
        print('r5')
        self.conn.commit()


        return new_daties