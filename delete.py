import os

# 獲取程序所在文件夾的路徑
current_directory = os.path.dirname(os.path.abspath(__file__))

# 列出該文件夾中的所有文件和子文件夾
files_and_folders = os.listdir(current_directory)

# 初始化一個變量，用於確認刪除操作
confirm_delete = input("確認刪除程序所在文件夾中的所有文件，除了程序本身？(y/n): ")

if confirm_delete.lower() == "y":
    # 遍歷文件和子文件夾，刪除文件
    for item in files_and_folders:
        item_path = os.path.join(current_directory, item)
        if os.path.isfile(item_path) and item != os.path.basename(__file__):
            os.remove(item_path)
    print("已刪除所有文件，但保留了程序本身。")
    input()
else:
    print("未執行刪除操作。")
    input()