# 初始化 ans 变量为 None
ans = None

# 进入无限循环
while True:
    # 获取用户输入
    expression = input("请输入表达式（输入'ans'使用上一次的结果，输入'exit'退出程序）: ")

    # 如果用户输入'exit'，则退出循环
    if expression == 'exit':
        break

    # 如果用户输入'ans'，则输出上一次的结果
    if expression == 'ans':
        if ans is not None:
            print(f'上一次的结果是: {ans}')
        else:
            print('没有上一次的结果')
        continue

    try:
        # 使用 eval 函数计算表达式的结果
        result = eval(expression)

        # 将结果存储到 ans 变量中
        ans = result

        # 输出计算结果
        print(f'计算结果是: {result}')
    except Exception as e:
        # 如果计算失败，输出错误信息
        print(f'计算失败: {e}')

# 退出程序
print('程序已退出。')
