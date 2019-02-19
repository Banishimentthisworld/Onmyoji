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


# 点击一次窗口
titlename = "阴阳师-网易游戏"
hwnd = win32gui.FindWindow(0, titlename)
win32gui.EnableWindow(hwnd, True)
win32gui.SetForegroundWindow(hwnd)
pyautogui.click()
# 截图并打印截图耗时
beg = time.time()
for i in range(10):
    window_capture("ji.jpg")
end = time.time()
print(end - beg)


def cycle_capture(img_name):
    # 载入并显示图片
    img = cv2.imread(img_name)
    img = cv2.resize(img, (873, 230))
    # cv2.imshow('1', img)
    # 降噪（模糊处理用来减少瑕疵点）
    result = cv2.blur(img, (5, 5))
    # cv2.imshow('2', result)
    # 灰度化,就是去色（类似老式照片）
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('3', gray)
    # param1的具体实现，用于边缘检测
    canny = cv2.Canny(img, 40, 80)
    # cv2.imshow('4', canny)

    # 霍夫变换圆检测
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=35, minRadius=20, maxRadius=40)
    tr = random.uniform(0.5, 1)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    if circles is None:
        pyautogui.moveTo(1677, 410)
        pyautogui.click()
        time.sleep(tr)
        return 'None'
    else:
        # print(len(circles[0]))
        # print('-------------我是条分割线-----------------')
        # 根据检测到圆的信息，画出每一个圆
        for circle in circles[0]:
            # 圆的基本信息
            cycle = []
            # print(circle[0])
            # print(circle[1])
            # 坐标行列(就是圆心)
            x = int(circle[0])
            y = int(circle[1])
            x1 = int(left + ((x / 970) * (right - left)))
            y1 = int(top + (((y + 172.5) / 575) * (bottom - top)))
            # 点击
            pyautogui.moveTo(x1, y1)
            pyautogui.click()
            time.sleep(tr)
            pyautogui.moveTo(1677, 410)
            pyautogui.click()
            time.sleep(tr)
            # 半径
            # r = int(circle[2])
            # 在原图用指定颜色圈出圆，参数设定为int所以圈画存在误差
            # img = cv2.circle(img, (x, y), r, (0, 0, 255), 1, 8, 0)
            # cv2.imshow('5', img)
            pyautogui.moveTo(1677, 410)
            pyautogui.click()
            time.sleep(tr)

while True :
    cycle_capture('ji.jpg')


# 显示新图像
# 按任意键退出1
# cv2.waitKey(0)
# cv2.destroyAllWindows()


