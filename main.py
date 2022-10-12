import pynput
from pynput import mouse
import time
import random
keyboard = pynput.keyboard.Controller()

#word list
greeting = ["안녕하세요", "환영합니다", "반갑습니다", "반가워요", "어서오세요", "반가워요", "만나서 반가워요", "카페에 오신걸 환영합니다"]
mainword = ["잘 부탁드립니다", "행복한 하루 되세요!", "잘 지내보아요", "자주 뵈요", "좋은 하루 되세요", "즐거운 하루 되세요", "항상 행복하세요"]
emotion = ["!", "~!", "^^", "~", "^^;", ":)", "~^^", "'◡'", "✌️ ̆̈", "(ง •̀_•́)ง", "(＾་།＾)", "⌒•_•⌒"]

while True:
    comment = random.choice(greeting) + random.choice(emotion)
    if random.randint(0, 1) == 0:
        comment = f"{comment} {random.choice(mainword)}{random.choice(emotion)}"
    print(f"Click the mouse to type '{comment}'")

    #Wait for mouse click
    with mouse.Listener(on_click=lambda x, y, button, pressed: pressed) as listener:
        listener.join()

    #typeing the comment
    for i in comment:
        if i == ' ':
            keyboard.press(pynput.keyboard.Key.space)
            time.sleep(random.uniform(0.02, 0.1))
            keyboard.release(pynput.keyboard.Key.space)
        elif i == '\n':
            keyboard.press(pynput.keyboard.Key.enter)
            time.sleep(random.uniform(0.05, 0.1))
            keyboard.release(pynput.keyboard.Key.enter)
        else:
            keyboard.press(i)
            time.sleep(random.uniform(0.005, 0.02))
            keyboard.release(i)
    #press COMMAND + ENTER
    keyboard.press(pynput.keyboard.Key.cmd)
    keyboard.press(pynput.keyboard.Key.enter)
    time.sleep(random.uniform(0.05, 0.1))
    keyboard.release(pynput.keyboard.Key.cmd)
    keyboard.release(pynput.keyboard.Key.enter)


