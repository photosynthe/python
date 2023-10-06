import openpyxl
import json

# 打开要转换的XLSX文件
workbook = openpyxl.load_workbook('xlsx.xlsx')

# 选择要处理的工作表
sheet = workbook.active

# 初始化一个空的JSON列表，用于存储数据
data_list = []

# 遍历工作表的行
for row in sheet.iter_rows(min_row=2, values_only=True):  # 假设第一行是标题行
    data_dict = {}
    data_dict['column0'] = row[0]  # 请替换为您的列名称
    data_dict['column1'] = row[1] # 请替换为您的列名称
    # 继续添加其他列...

    data_list.append(data_dict)

# 将数据列表转换为JSON格式
json_data = json.dumps(data_list, ensure_ascii=False, indent=4)

# 将JSON数据保存到文件中
with open('output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)
