from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/user/{username}")
def read_user_details(username: str):
    print(f"https://api.github.com/users/{username}")
    resp = requests.get(f"https://api.github.com/users/{username}")
    return {"result": resp.json()}



@app.get("/users/")
def find_first_forty_users():
    print(f"https://api.github.com/users/")
    resp = requests.get(f"https://api.github.com/users")
    return {"result": resp.json()}