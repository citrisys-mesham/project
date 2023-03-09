import mysql.connector
import configparser
class Config():
    def __init__(self) -> None:
        self.config=configparser.ConfigParser()
        
        self.config.read('/opt/flask-project/project/models/config/config_file.ini')
        
        
        self.conn=mysql.connector.connect(
          host=self.config.get('myproject1','host'),
          user=self.config.get('myproject1','user'),
          password=self.config.get('myproject1','password'),
          database=self.config.get('myproject1','database')
    )
    
    
        self.cursor=self.conn.cursor()