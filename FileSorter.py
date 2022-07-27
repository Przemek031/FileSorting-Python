import os
import shutil
l = list(os.listdir())
print(l)
for x in l:
    if os.path.isfile(x) == True:
        print(os.path.getsize(x))
        if x != "FileSorter.py":
            if os.path.getsize(x) > 5242880:
                shutil.move(os.path.abspath(x),"Bigger than 5Mb")
            elif os.path.getsize(x) < 5242880:
                shutil.move(os.path.abspath(x),"Smaller than 5Mb")