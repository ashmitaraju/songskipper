import json 
import os
def read_data():
    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd) 
    # print(files)
    with open("./app/utils/timings.json", "r") as f: 
        data = json.load(f)
        print(type(data))
        return data 