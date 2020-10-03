import json
from datetime import datetime as dt
import matplotlib.pyplot as plt

def totaldict(mydict):
    total = 0
    for i in mydict.values():
        total += i
    return total

dirpath = f'E:/!Programming/django/Keyboard/KEYDATA/{dt.now().year}-{dt.now().month}-{dt.now().day}.json'
myfile = open(dirpath, 'r')
myjson = json.loads(myfile.read())

print(f'Number of unique keys: {len(myjson)}')
print(f'Total pressed keys: {totaldict(myjson)}')

cpjson = myjson.copy()
for i in cpjson:
    if 'Key.' in i or cpjson[i] < 10:
        myjson.pop(i)

print(list(myjson))
plt.bar(list(myjson), list(myjson.values()))
plt.show()