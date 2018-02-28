from PIL import Image
import os
import time


def trim1(path, imgName):
    im = Image.open(path + imgName)
    width = im.size[0]
    height = im.size[1]
    maxLeft = width // 2 - 1
    maxRight = maxLeft + 1
    maxTop = height // 2 - 1
    maxBottom = maxTop + 1

    for w in range(width):
        for h in range(height):
            if h > maxTop and h < maxBottom and w > maxLeft and w < maxRight:
                continue
            if im.getpixel((w, h))[3] == 0:
                if h == 0:
                    if im.getpixel((w, h + 1))[3] != 0:
                        maxTop = h
                elif h == (height - 1):
                    if im.getpixel((w, h - 1))[3] != 0:
                        maxBottom = h
                else:
                    if im.getpixel((w, h + 1))[3] != 0:
                        if h <= maxTop:
                            maxTop = h
                    if im.getpixel((w, h - 1))[3] != 0:
                        if h >= maxBottom:
                            maxBottom = h
                if w == 0:
                    if im.getpixel((w + 1, h))[3] != 0:
                        maxLeft = w
                elif w == (width - 1):
                    if im.getpixel((w - 1, h))[3] != 0:
                        maxRight = w
                else:
                    if im.getpixel((w + 1, h))[3] != 0:
                        if w <= maxLeft:
                            maxLeft = w
                    if im.getpixel((w - 1, h))[3] != 0:
                        if w >= maxRight:
                            maxRight = w

    if (width - 1 - maxRight - maxLeft) > 0:
        trimWidth = maxLeft + 1
    else:
        trimWidth = width - maxRight
    box = (trimWidth, maxTop + 1, width - trimWidth, maxBottom)
    region = im.crop(box)
    region.save(imgName, 'PNG')


def trim2(path, imgName):
    im = Image.open(os.path.join(path, imgName))
    width, height = im.size
    cropWidth = cropTop = cropBottom = -1
    for i in range(width):
        for j in range(height):
            if cropWidth == -1:
                if im.getpixel((i, j))[3] != 0 or im.getpixel(
                    (width - 1 - i, j))[3] != 0:
                    cropWidth = i
            if cropTop == -1:
                if im.getpixel((j, i))[3] != 0:
                    cropTop = i
            if cropBottom == -1:
                if im.getpixel((j, height - 1 - i))[3] != 0:
                    cropBottom = i
            if cropWidth != -1 and cropTop != -1 and cropBottom != -1:
                break

    box = (cropWidth, cropTop, width - cropWidth, height - cropBottom)
    region = im.crop(box)
    region.save(imgName, 'PNG')


if __name__ == '__main__':
    path = 'D:/temp/'
    imgNames = os.listdir(path)
    for imgName in imgNames:
        if os.path.isdir(os.path.join(
                path, imgName)) or os.path.splitext(imgName)[1] != '.png':
            continue
        trim2(path, imgName)