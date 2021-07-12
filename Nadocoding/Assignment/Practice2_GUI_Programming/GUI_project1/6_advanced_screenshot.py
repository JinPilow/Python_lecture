import keyboard
import time
from PIL import ImageGrab


def screenshot():
    # 2021년 7월 10일 16시 51분 30초 -> _20210710_165130
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9키를 누르면 스크린샷 저장
# keyboard.add_hotkey("a", screenshot) # 사용자가 a키를 누르면 스크린샷 저장
# keyboard.add_hotkey("ctrl+shift+s", screenshot) # 사용자가 ctrl+shift+s키를 누르면 스크린샷 저장

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행