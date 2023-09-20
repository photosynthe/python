import zipfile
import os

def zip_current_folder():
    # 获取当前程序所在文件夹的路径
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # 获取当前文件夹的名称
    folder_name = os.path.basename(current_folder)
    
    # 压缩后的ZIP文件名与文件夹名称相同
    zip_filename = f"{folder_name}.zip"
    
    try:
        # 创建一个ZIP文件并打开以写入内容
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 遍历当前文件夹下的所有文件和子文件夹
            for root, dirs, files in os.walk(current_folder):
                for file in files:
                    # 构建文件的绝对路径
                    file_path = os.path.join(root, file)
                    # 排除程序文件的创建
                    if file_path != os.path.abspath(__file__):
                        # 构建ZIP文件内的相对路径
                        arcname = os.path.relpath(file_path, current_folder)
                        # 排除ZIP文件的创建
                        if not arcname.endswith('.zip'):
                            # 将文件添加到ZIP压缩包中
                            zipf.write(file_path, arcname)
                
                for dir in dirs:
                    # 构建目录的绝对路径
                    dir_path = os.path.join(root, dir)
                    # 构建ZIP文件内的相对路径
                    arcname = os.path.relpath(dir_path, current_folder)
                    # 排除ZIP文件的创建
                    if not arcname.endswith('.zip'):
                        # 将空目录添加到ZIP压缩包中
                        zipf.write(dir_path, arcname)

        print(f"成功创建ZIP文件：{zip_filename}")
    
    except Exception as e:
        print(f"创建ZIP文件时出错：{str(e)}")

if __name__ == "__main__":
    zip_current_folder()