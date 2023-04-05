import mysql.connector
import configparser
class Config():
    def __init__(self) -> None:
        self.config=configparser.ConfigParser()
        
        self.config.read('/home/lenovo/Desktop/cookies/project/modules/config.ini')
        
        
        self.conn=mysql.connector.connect(
          host=self.config.get('myproject1','host'),
          user=self.config.get('myproject1','user'),
          password=self.config.get('myproject1','password'),
          database=self.config.get('myproject1','database'),
          auth_plugin='mysql_native_password'
    )
    
    
        self.cursor=self.conn.cursor()