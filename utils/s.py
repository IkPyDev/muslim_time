
import json



with open("regions_user","r+") as file:
    data = file.read()
    data.replace("}{","},{")


# f = json.load()
print(data)