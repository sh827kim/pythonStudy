# glob : 경로 내의 폴더, 파일 목록 조회

import glob
print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능

import os
print(os.getcwd())
folder = "sample_dir"

if os.path.exists(folder):
    print("Already Exists")
    os.rmdir(folder)
    print(folder, "folder deleted")
else:
    os.makedirs(folder)
    print("Folder created")

print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))


import datetime
print("Today is ", datetime.date.today())

today = datetime.date.today()
time_delta = datetime.timedelta(days=100)
print("after 100 days ", today + time_delta)