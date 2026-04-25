import subprocess
import os


def git_push_automation(commit_message="auto update"):
    # 确保在正确的项目路径下
    project_path = r"C:\Users\ZhuanZ1\Desktop\多平台信息订阅"
    os.chdir(project_path)

    try:
        # 1. 添加所有更改
        subprocess.run(("git", "add", "."), check=True)#这里的列表看起来像是为了拼接字符串呢？我感觉实现的效果其实就是打出git add .但是为什么要用中括号装起来呢？,第一串是添加到暂存区，第二串是加到本地仓库，第三串是提交远程仓库

        # 2. 提交更改
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # 3. 推送到远程仓库
        # 这里建议先 pull 一下防止冲突，或者直接 push
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("🚀 推送成功！")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 操作失败: {e}")
