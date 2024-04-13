import os

os.remove("blaa.txt")

#check if file exist

import os
if os.path.exists("blaa.txt"):
    os.remove("blaa.txt")
else:
    print("The file does not exist")

#remove the folder

import os 

os.rmdir("fileopen")