from fastapi import FastAPI, File, Depends, HTTPException, status

import uvicorn

from check_prime_number import display_prime


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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)