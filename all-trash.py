import os
import send2trash

def delete_files_in_directory(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            # 排除程式本身
            if file_path != os.path.abspath(__file__):
                # 詢問使用者是否要刪除檔案
                confirm = input(f"確定要刪除檔案 '{file_path}' 嗎？ (y/n): ")
                if confirm.lower() == 'y':
                    send2trash.send2trash(file_path)
                    print(f"已刪除檔案 '{file_path}'")
                else:
                    print(f"未刪除檔案 '{file_path}'")

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # 詢問使用者是否要刪除資料夾
            confirm = input(f"確定要刪除資料夾 '{dir_path}' 嗎？ (y/n): ")
            if confirm.lower() == 'y':
                send2trash.send2trash(dir_path)
                print(f"已刪除資料夾 '{dir_path}'")
            else:
                print(f"未刪除資料夾 '{dir_path}'")

if __name__ == "__main__":
    # 取得當前程式的路徑
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 提示使用者確認
    confirmation = input(f"確定要刪除 '{current_dir}' 資料夾及其內容嗎？ (y/n): ")
    if confirmation.lower() == 'y':
        # 執行刪除動作
        delete_files_in_directory(current_dir)
        print("已刪除所有檔案和資料夾。")
    else:
        print("未執行刪除操作。")