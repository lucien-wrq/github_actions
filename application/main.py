import math 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello World!"

@app.get("/{number}")
def return_square(number: int):
    return get_square(number)

@app.get("/twice/{number}")
def return_square_twice(number: int):
    """
    Hello doc
    """
    return get_square(number) + get_square(number)

def get_square(number: int):
    return math.floor(math.pow(number, 2))