import os
import tkinter as tk
import tkinter.font as tkFont
import json
from tkinter import messagebox

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size / (1024 ** 3)  # 将文件夹大小转换为GB

def calculate_folder_sizes():
    for group_name, group_data in grouped_data.items():
        total_size_gb = 0
        for folder_path, _ in group_data["paths"]:
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                size_gb = get_folder_size(folder_path)
                total_size_gb += size_gb
                for idx, (path, _) in enumerate(group_data["paths"]):
                    if path == folder_path:
                        group_data["paths"][idx] = (path, size_gb)  # 更新文件夹大小
        group_data["total_size_gb"] = total_size_gb

def calculate_folder_size():
    folder_path = folder_path_entry.get()
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        size_gb = get_folder_size(folder_path)
        result_label.config(text=f"文件夹大小：{size_gb:.2f} GB")
        
        group_name = folder_group_entry.get()
        if group_name:
            # 更新分组数据
            update_group_data(group_name, folder_path, size_gb)
        
        # 更新多行文本框中的数据
        update_textbox()
        
        # 保存数据到 JSON 文件
        save_data_to_json()
    else:
        result_label.config(text="无效的文件夹路径")

def update_group_data(group_name, folder_path, size_gb):
    if group_name not in grouped_data:
        grouped_data[group_name] = {"total_size_gb": 0, "paths": []}
    
    # 检查路径是否已经存在于同一组中
    for path, _ in grouped_data[group_name]["paths"]:
        if path == folder_path:
            return
    
    grouped_data[group_name]["total_size_gb"] += size_gb
    grouped_data[group_name]["paths"].append((folder_path, size_gb))

def update_textbox():
    data_textbox.delete(1.0, tk.END)  # 清空多行文本框
    
    for group_name, group_data in grouped_data.items():
        total_size_gb = group_data["total_size_gb"]
        
        # 显示组名和总大小
        data_textbox.insert(tk.END, f"组名：{group_name}\n")
        data_textbox.insert(tk.END, f"总大小：{total_size_gb:.2f} GB\n")
        
        # 显示文件夹路径和大小
        for folder_path, size_gb in group_data["paths"]:
            data_textbox.insert(tk.END, f"文件夹路径：{folder_path}\n")
            data_textbox.insert(tk.END, f"大小：{size_gb:.2f} GB\n")
        
        data_textbox.insert(tk.END, "\n")

def save_data_to_json():
    with open("data.json", "w") as json_file:
        json.dump(grouped_data, json_file)

def load_data_from_json():
    if os.path.exists("data.json"):
        with open("data.json", "r") as json_file:
            return json.load(json_file)
    return {}

def delete_group(group_name):
    if group_name in grouped_data:
        confirm = messagebox.askokcancel("确认删除", f"您确定要删除组 '{group_name}' 吗？")
        if confirm:
            del grouped_data[group_name]
            # 更新多行文本框和保存数据到 JSON 文件
            update_textbox()
            save_data_to_json()

def delete_folder_path(folder_path):
    for group_name, group_data in grouped_data.items():
        paths = group_data["paths"]
        for path_info in paths:
            if path_info[0] == folder_path:
                confirm = messagebox.askokcancel("确认删除", f"您确定要删除路径 '{folder_path}' 的信息吗？")
                if confirm:
                    paths.remove(path_info)
                    group_data["total_size_gb"] -= path_info[1]
                    # 更新多行文本框和保存数据到 JSON 文件
                    update_textbox()
                    save_data_to_json()

# 创建主窗口
root = tk.Tk()
root.title("文件夹大小计算器")

# 增大字体到原来的1.5倍
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=int(default_font.cget("size") * 1.5))

# 输入文件夹路径的文本框
folder_path_label = tk.Label(root, text="请输入文件夹路径:", font=default_font)
folder_path_label.grid(row=0, column=0, padx=10, pady=10)

folder_path_entry = tk.Entry(root, font=default_font)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)

# 组名的文本框
folder_group_label = tk.Label(root, text="组名：", font=default_font)
folder_group_label.grid(row=1, column=0, padx=10, pady=10)

folder_group_entry = tk.Entry(root, font=default_font)
folder_group_entry.grid(row=1, column=1, padx=10, pady=10)

# 计算按钮
calculate_button = tk.Button(root, text="计算文件夹大小", command=calculate_folder_size, font=default_font)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# 删除组按钮
delete_group_button = tk.Button(root, text="删除组", command=lambda: delete_group(folder_group_entry.get()), font=default_font)
delete_group_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# 删除文件夹大小信息按钮
delete_info_button = tk.Button(root, text="删除文件夹信息", command=lambda: delete_folder_path(folder_path_entry.get()), font=default_font)
delete_info_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# 显示文件夹大小结果的标签
result_label = tk.Label(root, text="", justify="left", font=default_font)
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# 多行文本框显示历史数据
data_textbox = tk.Text(root, width=50, height=20, wrap=tk.WORD, font=default_font)
data_textbox.grid(row=0, column=2, rowspan=6, padx=10, pady=10)

# 初始化分组数据字典
grouped_data = load_data_from_json()

# 自动重新计算已保存的文件夹大小
calculate_folder_sizes()

# 更新多行文本框
update_textbox()

# 启动主循环
root.mainloop()
