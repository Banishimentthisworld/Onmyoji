import pyautogui
# import syd
import win32gui, win32ui, win32con, win32api
i = 1
while i == 1:
    titlename = "阴阳师-网易游戏"
    hwnd = win32gui.FindWindow(0, titlename)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print('左上x：' + str(left) + ' 左上y：' + str(top) + '  右下x：' + str(right) + ' 右下y：' + str(bottom))
    currentMouseX, currentMouseY = pyautogui.position()
    print('X轴=' + str(currentMouseX) + '  Y轴=' + str(currentMouseY))