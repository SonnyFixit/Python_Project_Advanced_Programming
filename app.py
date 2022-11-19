from fastapi import FastAPI, File, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from jose import JWTError
from jose import jwt

from passlib.context import CryptContext

from datetime import datetime
from datetime import timedelta

from PIL import Image
from PIL import ImageChops


from check_prime_number import display_prime
from invert_image_colors import invert_colors


import uvicorn

app = FastAPI()

@app.get("/")
async def root():
   return {"Hello there!"}


@app.get("/prime/{number}")
async def check_if_prime(number: int):
    if isinstance(number, int) and number < 9223372036854775807 and number >= 2:
        return display_prime(number)
    else:
        return {"Provided data is not an integer between 0 - 9223372036854775807" }

@app.post("/picture/invert")
async def invert_image(file: bytes = File(...)):
    return StreamingResponse(invert_colors(file), media_type="image/JPEG")

@app.post("/picture/invert2")
async def invert_image2():
    
    img = Image.open("test.jpg")
    img.show()

    inv_img = ImageChops.invert(img)
    inv_img.show()



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)