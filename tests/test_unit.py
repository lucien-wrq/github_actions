from fastapi.testclient import TestClient
from random import randint
import pytest, math
from application.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World!"

def test_return_square():
    response = client.get("/4")
    assert response.status_code == 200
    assert response.json() == 16

def test_return_square_twice():
    response = client.get("/twice/4")
    assert response.status_code == 200
    assert response.json() == 32

list_of_numbers = [randint(1, 10) for i in range(0, 10)]

@pytest.mark.parametrize('number', list_of_numbers)
def test_return_square_twice(number: int):
    response = client.get(f"/twice/{number}")
    assert response.status_code == 200
    assert response.json() == math.pow(number, 2) * 2
