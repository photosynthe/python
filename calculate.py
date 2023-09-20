# 导入用于数学表达式计算的库
import math

while True:
    # 获取用户输入的数学表达式
    expression = input("请输入数学表达式：")

    try:
        # 使用eval()函数计算表达式的结果（请谨慎使用eval，不要接受不受信任的输入）
        result = eval(expression)

        # 打印结果
        print("计算结果为:", result)

    except Exception as e:
        print("发生错误:", e)