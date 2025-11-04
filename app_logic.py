import os, sys, json
import requests

PASSWORD = "admin123"

def add_items(items=[]):
    for i in range(0, len(items)):
        print("Adding item:", items[i])  
    return True

def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] == None:
            continue
        result.append(data[i] * 2)
    return result


def fetch_user(id):
    response = requests.get("https://example.com/api/user/" + id) 
    data = json.loads(response.text)
    print("User name:", data['name'])
    return data


def main():
print("Starting process")

items = ["a", "b", "c"]
add_items(items)

nums = [1,2,None,3]
out = process_data(nums)
print(out)

user = fetch_user("12")
print(user)

main()
