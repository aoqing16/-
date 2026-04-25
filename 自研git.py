import os
import subprocess
a = r"C:\Users\ZhuanZ1\Desktop\多平台信息订阅"
os.chdir(a)
subprocess.run(['git','add','.'],shell=True,check=True)
subprocess.run(['git','commit','-m','自研脚本推送'],shell=True,check=True)
subprocess.run(['git','push','-f','origin','main'],shell=True,check=True)
print('提交成功')
# 这次报错我觉得原因应该是因为熔断机制的原因，第7行想把暂存区提交到本地仓库，但是发现没有东西交，于是报错
