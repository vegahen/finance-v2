import os

from utility.fileutility import loadJson, dumpJson

configPath = "config.json"

configSatisfied = False
configChanged = True
newSession = True
while not configSatisfied:
    configSatisfied = True

    if configPath not in os.listdir("."):
        dumpJson({ "dataPath": "{INSERT_PATH_TO_YOUR_DATA_REPOSITORY}" }, configPath)
        print("Your 'config.json' file has been created. In order to start using this program, you need to specify a data repository.\n")
        configSatisfied = False
    else:
        config = loadJson(configPath)
        for key in config:
            if config[key][:8] == "{INSERT_":
                configSatisfied = False
                configChanged = False
    
    if not configSatisfied:
        if configChanged or newSession:
            print("There are missing fields in your 'config.json' file.\nAll fields requiring input are marked with {INSERT_XXX}, where 'XXX' further describes the needed value.\nPress ENTER to continue after the fields are filled.")
        else:
            print("There are still missing fields.", end="")
        foo = input()
    newSession = False

if not configChanged:
    print()

dataPath = config["dataPath"]
dataConfigName = "dataconfig.json"
dataConfigPath = os.path.join(dataPath, dataConfigName)

dataConfigSatisfied = False
dataConfigChanged = True
newSession = True
while not dataConfigSatisfied:
    dataConfigSatisfied = True

    if dataConfigName not in os.listdir(dataPath):
        dumpJson({}, dataConfigPath)
        print("Your 'dataconfig.json' file has been created in your data repository.\n")
