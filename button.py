import win32gui

# 按钮缩放比例
ratio_types = {'button_yyh': (0.7379227050, 0.696177062),
               'button_h10': (0.833743532, 0.79958043),
               'button_xsfy': (0.666293775, 0.593477435),
               'button_h11': (0.491173416, 0.289703316),
               }


# ratio_0 = ('button_yyh',)
# 定位bottom
def get_bottom(hwnd, ratios, ratio_type):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    result = {}
    for ratio in ratios:
        x = int(left + ((right - left) * ratio_type[ratio][0]))
        y = int(top + (bottom - top) * ratio_type[ratio][1])
        result[ratio] = (x, y)
    return result

# re = get_bottom(788084, ratio_0 ,ratio_types)
# # print(re)