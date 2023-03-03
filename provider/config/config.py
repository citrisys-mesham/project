import mysql.connector 
import configparser
class Config():
    def __init__(self) -> None:
        self.config=configparser.ConfigParser()
        
        self.config.read('/home/lenovo/Desktop/myproject/property/provider/config/config_file.ini')
        print(self.config.get('contact','host'))
        
        self.conn=mysql.connector.connect(
          host=self.config.get('contact','host'),
          user=self.config.get('contact','user'),
          password=self.config.get('contact','password'),
          database=self.config.get('contact','database')
    )
    
    
        self.cursor=self.conn.cursor()