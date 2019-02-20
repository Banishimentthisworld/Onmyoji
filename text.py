import time
import pyautogui
# import syd
import win32gui, win32ui, win32con, win32api
import cv2
import random


def window_capture(filename):
    # 窗口的编号，0号表示当前活跃窗口
    hwnd = 0
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取窗口信息
    titlename = "阴阳师-网易游戏"
    # 根据titlename信息查找窗口
    hwnd = win32gui.FindWindow(0, titlename)
    # 获取左上和右下的坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # 截图图片的宽
    w = int((right - left) * 0.9)
    # 截图图片的高
    h = int((bottom - top) * 0.4)
    # 截取图片的起点
    s = left
    e = int(top+(bottom-top)*0.3)
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (s, e), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


def cycle_capture(img_name):
    # 载入图片
    img = cv2.imread(img_name)
    # 缩放图片
    img = cv2.resize(img, (873, 230))
    # 降噪（模糊处理用来减少瑕疵点）
    result = cv2.blur(img, (5, 5))
    # 灰度化,就是去色（类似老式照片）
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # param1的具体实现，用于边缘检测
    canny = cv2.Canny(img, 40, 80)
    # 霍夫变换圆检测
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=35, minRadius=20, maxRadius=40)
    if circles is None:
        return None
    else:
        return circles[0]


while True:
    # 随机延时
    tr = random.uniform(0.5, 1)
    # 窗口置顶
    titlename = "阴阳师-网易游戏"
    hwnd = win32gui.FindWindow(0, titlename)
    win32gui.EnableWindow(hwnd, True)
    win32gui.SetForegroundWindow(hwnd)
    # 获取窗口信息
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    start_bottom = [(left + (right - left) * 0.876), (top + (bottom - top) * 0.723)]
    # 截图
    for i in range(10):
        window_capture("ji.jpg")
    # 查找圆
    cycles = cycle_capture('ji.jpg')

    # 如果没有检测到圆，就点击开始按钮
    if cycles is None:
        pyautogui.moveTo(start_bottom[0], start_bottom[1])
        pyautogui.click()
        time.sleep(tr)
    else:
        for cycle in cycles:
            print(cycle)
            # 如果检测到圆，就点击圆心
            x = int(cycle[0])
            y = int(cycle[1])
            x1 = int(left + ((x / 970) * (right - left)))
            y1 = int(top + (((y + 172.5) / 575) * (bottom - top)))
            pyautogui.moveTo(x1, y1)
            pyautogui.click()
            time.sleep(tr)
            # 排除结算界面的干扰，点击两下
            pyautogui.moveTo(start_bottom[0], start_bottom[1])
            pyautogui.click()
            pyautogui.click()
            time.sleep(tr)
# 显示新图像
# 按任意键退出1
# cv2.waitKey(0)
# cv2.destroyAllWindows()


