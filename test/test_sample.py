import sys
import os

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.insert(0, app_path)

from flask_app_deploy import app

test_client = app.test_client()


def test_hello():
    response = test_client.get("/")
    assert response.status_code == 200
    assert 'Hello, world!' in response.get_data().decode("utf-8")


def test_add():
    response = test_client.get("/add/10/20")
    assert response.status_code == 200
    result = response.get_json()["num1 + num2"]
    assert result == 30


def test_subtract():
    response = test_client.get("/subtract/35/20")
    assert response.status_code == 200
    result = response.get_json()["num1 - num2"]
    assert result == 15


def test_multiply():
    response = test_client.get("/multiply/10/20")
    assert response.status_code == 200
    result = response.get_json()["num1 * num2"]
    assert result == 200


def test_divide():
    response = test_client.get("/divide/100/20")
    assert response.status_code == 200
    result = response.get_json()["num1 / num2"]
    assert result == 5


def test_modulo():
    response = test_client.get("/modulo/10/3")
    assert response.status_code == 200
    result = response.get_json()["num1 % num2"]
    assert result == 1
