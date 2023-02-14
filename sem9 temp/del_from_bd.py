import os

with open(os.path.dirname(os.path.abspath(__file__))+'\db.csv', "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != "line you want to remove...":
            f.write(i)
    f.truncate()