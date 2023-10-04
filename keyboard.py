import keyboard

# 用於跟蹤已經觸發的按鍵
pressed_keys = set()

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN and e.name not in pressed_keys:
        pressed_keys.add(e.name)
        print(f'按下了按鍵：{e.name}')
    elif e.event_type == keyboard.KEY_UP and e.name in pressed_keys:
        pressed_keys.remove(e.name)

# 註冊鍵盤事件處理函數
keyboard.hook(on_key_event)

# 保持程式運行，直到按下Ctrl + C結束
try:
    keyboard.wait('ctrl+c')
except KeyboardInterrupt:
    pass

# 清理
keyboard.unhook_all()
