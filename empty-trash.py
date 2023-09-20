import os
from send2trash import send2trash

def find_empty_folders(path):
    empty_folders = []
    for folder_name, subfolders, filenames in os.walk(path, topdown=False):
        for subfolder in subfolders:
            folder_path = os.path.join(folder_name, subfolder)
            if not os.listdir(folder_path):  # 檢查文件夾是否為空
                empty_folders.append(folder_path)
    return empty_folders

def write_to_log(empty_folders, log_file):
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("以下是需要移入回收站的空文件夾列表：\n")
        for folder in empty_folders:
            f.write(folder + '\n')

def main():
    current_directory = os.getcwd()  # 獲取當前腳本所在的文件夾路徑
    empty_folders = find_empty_folders(current_directory)

    if not empty_folders:
        print("沒有空文件夾需要處理。")
        input()
        return

    log_file = "empty_folders_log.txt"
    write_to_log(empty_folders, log_file)

    print(f"已將需要移入回收站的空文件夾列表寫入日誌文件：{log_file}")
    print("以下是需要移入回收站的空文件夾列表：")
    for folder in empty_folders:
        print(folder)

    confirmation = input("是否要移入回收站上述空文件夾？ (y/n): ")
    if confirmation.lower() == 'y':
        for folder in empty_folders:
            try:
                print(f"正在移入回收站文件夾：{folder}")
                send2trash(folder)  # 將空文件夾移入回收站
                open_log_file(log_file)
            except Exception as e:
                print(f"無法移入回收站文件夾 {folder}: {str(e)}")

if __name__ == "__main__":
    main()
