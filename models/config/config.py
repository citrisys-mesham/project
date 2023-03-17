import mysql.connector
import configparser
class Config():
    def __init__(self) -> None:
        self.config=configparser.ConfigParser()
        
<<<<<<< HEAD
        self.config.read('/opt/flask-project/project/models/config/config_file.ini')
=======
        self.config.read('/opt/flask-project/project/project/models/config/config_file.ini')
>>>>>>> a5a9baba330bd160ce76a9bd7b6c7e014274535f
        
        
        self.conn=mysql.connector.connect(
          host=self.config.get('myproject1','host'),
          user=self.config.get('myproject1','user'),
          password=self.config.get('myproject1','password'),
          database=self.config.get('myproject1','database'),
          auth_plugin='mysql_native_password'
    )
    
    
        self.cursor=self.conn.cursor()