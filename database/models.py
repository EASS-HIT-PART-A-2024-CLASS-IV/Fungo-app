from sqlalchemy import Column, Integer, String 
from database import Base

class User(Base):
    __tablename__= 'users'
    
    email = Column(String, primary_key = True)
    
    password = Column(String)
    
    username = Column(String, unique = True)
    
    phone_number = Column(String)
    
    car_number = Column(Integer)