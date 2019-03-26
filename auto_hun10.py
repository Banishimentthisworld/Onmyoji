import random
import time
import win32gui
import pyautogui
import win32con
import button
import threading
import sys
import pyHook
import pythoncom
import queue
# 历遍所有窗口，筛选出阴阳师的窗口
hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

# hd为存放句柄的数组，hh为计数符号
hd = [0]
hh = 0
# 筛选出所有阴阳师窗口，将其打印出来，并存放到数组中
for h, t in hwnd_title.items():
    if t == '阴阳师-网易游戏':
        hd.append(h)
        hh += 1
        print(hd[hh])


def onKey(event):
    if event.Key == 'Q':
        sys.exit(0)
    return True


def Keyboard():
    hookmanager = pyHook.HookManager()
    hookmanager.KeyDown = onKey
    hookmanager.HookKeyboard()
    pythoncom.PumpMessages()


def main0():
    # 获取窗口信息
    i = 1
    while i == 1:
        h = 1
        while h <= hh:
            hwnd = hd[h]
            h += 1
            # 根据titlename信息查找窗口
            # hwnd = win32gui.FindWindow(0,titlename)
            win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
            # 窗口激活置顶
            win32gui.EnableWindow(hwnd, True)
            win32gui.SetForegroundWindow(hwnd)
            # 等比例缩放找到按钮
            x = [0]
            ratios = ('button_h10', 'button_xsfy')
            buttons = button.get_bottom(hwnd, ratios, button.ratio_types)
            x.extend(['button_h10', 'button_xsfy', 'button_h10'])
            # 设置随机延时和抖动
            tr = random.uniform(0.5, 1)
            pr = random.uniform(3, 10)
            # 打印随机抖动
            print('抖动 x轴=' + str(pr) + ' ,' + 'y轴=' + str(tr))
            # 移动到对应位置，点击鼠标
            for X in x:
                if X != 0:
                    pyautogui.moveTo(buttons[X][0] + pr, buttons[X][1] + tr)
                    pyautogui.click()
                    # 打印和设置延时
                    print('延时' + str(tr))
                    time.sleep(tr)



if __name__ == '__main__':
    t1 = threading.Thread(target=Keyboard,)
    t2 = threading.Thread(target=main0, )
    t1.start()
    t2.start()
