import win32gui


def get_child_windows(parent):
 '''
 获得parent的所有子窗口句柄
  返回子窗口句柄列表
  '''
 if not parent:
  return
 hwndChildList = []
 win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwndChildList)
 return hwndChildList

list = [0]
list = get_child_windows(1247034)