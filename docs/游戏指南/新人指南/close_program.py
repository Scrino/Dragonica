import os
import time
import subprocess

# 设置等待时间（秒）
wait_time = 60  # 1小时后关闭

# 程序名称（如 "dragonica.exe"）
program_name = "dragonica.exe"

time.sleep(wait_time)  # 等待指定时间

# 方法1：使用 taskkill 命令
os.system(f"taskkill /f /im {program_name}")

# 方法2：使用 subprocess（推荐）
# subprocess.run(["taskkill", "/f", "/im", program_name], shell=True)

# 脚本执行命令 python close_program.py