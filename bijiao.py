from PIL import Image,ImageEnhance,ImageFilter
import os

# 获取灰度值
def getGray(image_file):
    tmpls = []
    for h in range(0, image_file.size[1]):  # h
        for w in range(0, image_file.size[0]):  # w
            tmpls.append(image_file.getpixel((w, h)))
    return tmpls

# 获取平均灰度值
def getAvg(ls):
    # sum求和， len个数
    return sum(ls)/len(ls)

# 比较100个字符有几个字符相同
def getMH(a,b):
    dist = 0
    for i in range(0, len(a)):
        if a[i] == b[i]:
            dist += 1
    return (dist/len(a))*100

# 获得图片相似度
def getImgHash(pic):
    # 输入图像
    image_file = Image.open(pic)
    # 将图片缩小为12×12px
    image_file = image_file.resize((12, 12))
    # L为黑白模式
    image_file = image_file.convert("L")
    # 获取灰度，放到数组中
    Grayls = getGray(image_file)
    # 获取灰度平均值
    avg = getAvg(Grayls)
    # 接收1或0
    bitls = ''

    for h in range(1, image_file.size[1]-1):
        for w in range(1,image_file.size[0]-1):
            # 像素大于平均值的记为1，小于的记为0
            if image_file.getpixel((w,h)) >= avg:
                bitls = bitls + '1'
            else:
                bitls = bitls + '0'
    return bitls

#基准图片
a = getImgHash(".//base_photo//ji.jpg")
files = os.listdir(".//test_photo")
for file in files:
    b = getImgHash(".//test_photo//" + str(file))
    compare = getMH(a, b)
    print(file, u'相似度', str(compare) + '%')