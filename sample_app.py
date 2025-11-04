import os, sys
from datetime import datetime

data = []
cache = {}

def loadData(file):
    f = open(file, "r")
    for line in f.readlines():
        data.append(line.strip())
    f.close()
    return data

def processItems(items):
    results = []
    for i in range(len(items)):
        if items[i] == "error":
            print("ERR!!")
        else:
            results.append(items[i] + " processed")
    return results

def saveToFile(filename, content):
    file = open(filename, "w")
    for x in content:
        file.write(x + "\n")
    print("✅ saved")
    file.close()

def main():
    loadData("input.txt")  
    processed = processItems(data)
    saveToFile("output.txt", processed)

    time = datetime.now()
    print("Processed at " + str(time))

main()
