def hex_to_int(hex_str):
    try:
        return int(hex_str, 16)
    except ValueError:
        return None

def calculate_hex(expression):
    parts = expression.split('-')
    if len(parts) != 2:
        return "无效的表达式"
    
    num1 = hex_to_int(parts[0])
    num2 = hex_to_int(parts[1])
    
    if num1 is None or num2 is None:
        return "无效的数字格式"
    
    result = num1 - num2
    return result, hex(result)

while True:
    expression = input("请输入16进制表达式或输入'退出'来退出：")
    
    if expression.lower() == '退出':
        break
    
    result, hex_result = calculate_hex(expression)
    print(f"16进制结果: {hex_result[2:]}")  # 去掉0x前缀
    print(f"10进制结果: {result}")
