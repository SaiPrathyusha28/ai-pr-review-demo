import json, os

def load_data(file):
    data = []
    f = open(file, "r")    
    for line in f.readlines():
        data.append(line.strip())
    f.close()              
    
    return data

def save_data(filename, content):
    file = open(filename, "w")   
    for x in content:
        file.write(x + "\n")     
    file.close()

def divide(a, b):
    return a / b    

config = json.loads(open("config.json").read())  

result = divide(10, 0)
print(result)
