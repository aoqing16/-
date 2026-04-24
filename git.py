import os

repo_path = r"C:\Users\ZhuanZ1\Desktop\多平台信息订阅"

os.chdir(repo_path)

os.system("git add .")
os.system('git commit -m "auto update"')
os.system("git push")