import requests

def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/user/{user_id}")
    if response.status_code == 200:
        return {"id": 1, "name": "John Doe"}
    return None