import os
import shutil

# 获取当前目录
current_directory = os.getcwd()

# 查找空文件夹并将路径写入日志
empty_folders = []
for foldername, subfolders, filenames in os.walk(current_directory, topdown=False):
    if not subfolders and not filenames:
        empty_folders.append(foldername)

# 获取桌面路径
desktop_directory = os.path.expanduser("~/Desktop")

# 构建日志文件路径
log_file = os.path.join(desktop_directory, "empty_folders_log.txt")

# 将空文件夹路径写入日志文件
with open(log_file, "w") as f:
    for folder in empty_folders:
        f.write(folder + "\n")

# 询问用户是否移入回收站
response = input("是否将这些空文件夹移到回收站？(y/n): ").strip().lower()

if response == "y":
    # 移入回收站
    for folder in empty_folders:
        try:
            shutil.rmtree(folder)
            print(f"已将文件夹 '{folder}' 移入回收站")
        except Exception as e:
            print(f"移入文件夹 '{folder}' 到回收站时出错: {e}")

# 程序执行完毕后等待用户输入
input("按 Enter 键退出程序...")
