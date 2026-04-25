import os
import subprocess
a = r"C:\Users\ZhuanZ1\Desktop\多平台信息订阅"
os.chdir(a)
subprocess.run(['git','add','.'],shell=True,check=True)
subprocess.run(['git','commit','-m','自研更新订阅'],shell=True,check=True)
subprocess.run(['git','push','origin','main'],shell=True,check=True)
print('提交成功')