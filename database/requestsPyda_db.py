from pydantic import BaseModel

class RequestRegister(BaseModel):
    email: str
    
    password: str
    
    username: str
    
    phone_number: str
    
    car_number: int

class RequestLog(BaseModel):
    email: str
    
    password: str
    
