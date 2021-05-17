import os, glob

os.chdir("C:\\Users\\joabh\\Pictures")
for file in glob.glob("*.jpg"):
    print(file)