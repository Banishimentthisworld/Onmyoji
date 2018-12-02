import pyautogui
i = 1
while i == 1:
    currentMouseX, currentMouseY = pyautogui.position()
    print('X轴=' + str(currentMouseX) + '  Y轴=' + str(currentMouseY))