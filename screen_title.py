import time
import pyautogui
import sys
import win32gui
import win32ui
import win32con
import win32api


def window_capture(filename):
    hwnd: int = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取窗口信息
    titlename = "阴阳师-网易游戏"  # 活动窗口标题
    hwnd = win32gui.FindWindow(0, titlename)  # 根据titlename信息查找窗口
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 获取左上和右下的坐标
    w = int((right - left) * 0.318)  # 截图图片的宽
    h = int((bottom - top - 50) * 0.217)  # 截图图片的高
    print(w)
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (left + 5, top + 30), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


# 点击一次窗口
#titlename = "阴阳师-网易游戏"
#hwnd = win32gui.FindWindow(0, titlename)
#left, top, right, bottom = win32gui.GetWindowRect(hwnd)
#pyautogui.moveTo(left + 2, top + 2)
#pyautogui.click()
#win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)

# 截图并打印截图耗时
beg = time.time()
for i in range(10):
    window_capture("ji.jpg")
end = time.time()
print(end - beg)
