import json

def loadJson(filePath):
    with open(filePath, "r") as file:
        return json.load(file)

def dumpJson(jsonObject, filePath):
    with open(filePath, "w") as file:
        json.dump(jsonObject, file, indent=4, ensure_ascii=False)
        file.write("\n")
