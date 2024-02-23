from fastapi import FastAPI, HTTPException, Depends
from requestsPyda import RequestBodyRegion, RequestRegister, RequestLog 
from db_areas import db_areas_tlv
import httpx
import json

app = FastAPI()

user_logged = {}

@app.get("/")
async def root():
    return {"message": "app is up and running!"}

@app.post("/v1/login/")
async def login(user : RequestLog):
    global user_logged
    user_dict = user.dict() 
    response = httpx.post("http://database:6699/login_query/", json=user_dict)
    if response.status_code == 401:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    elif response.status_code == 200:
        response_json = response.json()
        user_logged = response_json.get("user")
        if user_logged:
            return {"user": user_logged}
    
@app.post("/v1/register/")
async def register(user : RequestRegister):
    user_dict = user.dict()
    response = httpx.post("http://database:6699/register_query/", json=user_dict)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=500, detail="could not resolve issue")

@app.get("/v1/main_page/")
async def main_page():
    global user_logged
    username = user_logged["username"]
    car_number = user_logged["car_number"]
    return {"message": f"Welcome {username}, Owner of car number {car_number}"}
    
@app.post("/v1/startparking/")
async def parking_area(region : RequestBodyRegion):
    try:
        if region.time_parking > 0:
            for regiondb in db_areas_tlv:
                if regiondb["region"] == region.region:
                    price = round((regiondb["price"]*region.time_parking),2)
                    return {"message" : f"The price for the lease of this park in this region is: {price}", "price" : price}
    except:
        return {"message" : "Error - negative number inserted"}
    
@app.get("/v1/user_info/")
async def get_user_info():
    global user_logged
    return {"User Name" : user_logged["username"],
            "User Car Number" : user_logged["car_number"],
            "User Email" : user_logged["email"],
            "User phone number" : user_logged["phone_number"]}


    

