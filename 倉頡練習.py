import random
import json
import tkinter as tk

# 使用相对路径加载JSON字库文件
characters_file_path = 'cangjie.json'

# 初始化一个空的字典来存储字库数据
characters = {}

# 加载字库数据
def load_characters(characters_file_path):
    with open(characters_file_path, 'r', encoding='utf-8') as json_file:
        characters = json.load(json_file)
    return characters

def save_characters(characters, characters_file_path):
    with open(characters_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(characters, json_file, ensure_ascii=False, indent=2)

def calculate_total_probability(characters):
    total_probability = sum(characters[character]['probability'] for character in characters)
    return total_probability

def select_random_character(characters):
    # 根据概率选择汉字
    weighted_characters = list(characters.keys())
    probabilities = [characters[char]['probability'] for char in weighted_characters]
    random_character = random.choices(weighted_characters, probabilities)[0]
    return random_character

def initialize_probabilities():
    for character in characters:
        characters[character]['probability'] = 1/4800
    save_characters(characters, characters_file_path)
    show_random_character()
    result_label.config(text='概率已初始化')
    update_total_probability_label()

def update_probabilities(characters, input_character, is_correct):
    total_probability = calculate_total_probability(characters)
    input_probability = characters[input_character]['probability']  # 存储当前字符的概率值
    
    for character in characters:
        if character == input_character:
            if is_correct:
                characters[character]['probability'] = input_probability / 2  # 答对，概率减半
            else:
                characters[character]['probability'] = input_probability * 2  # 答错，概率加倍
        else:
            if is_correct:
                characters[character]['probability'] *= (1 - input_probability)  # 答对，其他字概率适当减少
            else:
                characters[character]['probability'] /= (1 - input_probability)  # 答错，其他字概率适当增加
    
    save_characters(characters, characters_file_path)
    update_total_probability_label()

def update_total_probability_label():
    total_probability = calculate_total_probability(characters)
    total_probability_label.config(text=f'总概率之和：{total_probability:.4f}')

def show_random_character():
    random_character = select_random_character(characters)
    character_label.config(text=f'请输入汉字：{random_character}')
    entry.delete(0, 'end')  # 清空输入框

def check_answer(event=None):
    user_input = entry.get()
    current_character = character_label.cget("text")[6:]  # 提取当前字符
    is_correct = (user_input == characters[current_character]['cangjie'])
    update_probabilities(characters, current_character, is_correct)
    
    if is_correct:
        result_label.config(text='答对了！')
    else:
        result_label.config(text=f'答错了，正确的拼音是：{characters[current_character]["cangjie"]}')
    
    show_random_character()

# 创建主窗口
root = tk.Tk()
root.title("汉字练习")

# 创建汉字显示标签
character_label = tk.Label(root, text='', font=("Helvetica", 24))
character_label.pack()

# 创建输入框
entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack()

# 创建检查按钮
check_button = tk.Button(root, text="检查答案", command=check_answer)
check_button.pack()

# 创建答案结果标签
result_label = tk.Label(root, text='', font=("Helvetica", 16))
result_label.pack()

# 创建初始化概率按钮
initialize_button = tk.Button(root, text="初始化概率", command=initialize_probabilities)
initialize_button.pack()

# 创建总概率显示标签
total_probability_label = tk.Label(root, text='', font=("Helvetica", 16))
total_probability_label.pack()

# 加载字库数据
characters = load_characters(characters_file_path)

# 更新总概率显示标签
update_total_probability_label()

# 显示第一个汉字
show_random_character()

# 将输入框与"Enter"键绑定，以便按Enter键提交答案
root.bind('<Return>', check_answer)

# 启动主循环
root.mainloop()