import  os
from pathlib import Path

files = os.listdir('exchanges')
print(files)

k = [1,2,3,4,5,7,8,9,2,4,4]
for i in k:
    del i
print(k)