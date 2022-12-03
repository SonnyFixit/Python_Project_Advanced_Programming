from fastapi import FastAPI, File, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordRequestForm

from datetime import datetime
from datetime import timedelta

from check_prime_number import display_prime
from invert_image_colors import invert_colors
from user_verification import fake_users_db, UserInDB, fake_hash_password, get_current_user, get_current_active_user, get_user, User


import uvicorn

app = FastAPI()

str_hello =  "Hello there! Enter specified urls to access different endpoints"

@app.get("/")
async def root():
   return str_hello


@app.get("/prime/{number}")
async def check_if_prime(number: int):
    if isinstance(number, int) and number < 9223372036854775807 and number >= 2:
        return display_prime(number)
    else:
        return {"Provided data is not an integer between 0 - 9223372036854775807" }

@app.post("/picture/invert")
async def invert_image(file: bytes = File(...)):
    return StreamingResponse(invert_colors(file), media_type="image/JPEG")


@app.get("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/ShowTime")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return datetime.now().strftime("%H:%M:%S")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)