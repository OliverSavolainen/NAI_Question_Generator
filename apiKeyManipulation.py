import os
def save_api_key(api_key):
    with open("api_key.txt", "w") as f:
        if api_key != "" and os.stat("api_key.txt").st_size == 0:
            f.write(api_key)

def get_api_key():
    with open("api_key.txt", "r") as f:
        return f.read()