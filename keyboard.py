import keyboard
import signal

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

# 定義一個處理Ctrl + C信號的函數，什麼也不做
def handle_ctrl_c(signal, frame):
    pass

# 設置Ctrl + C信號處理程序
signal.signal(signal.SIGINT, handle_ctrl_c)

# 無限循環，直到手動結束程式
keyboard.wait()
