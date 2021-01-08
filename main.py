import numpy as np
from PIL import Image
import math

def dataToImage(data, imagePath):
    module = len(data)%3
    paddingNeeded = 0
    dataEncode = data.encode()
    if module != 0:
        if module == 1:
            paddingNeeded = 2
        elif module == 2:
            paddingNeeded = 1
    for _ in range(paddingNeeded):
        dataEncode = bytearray(b'\x00') + dataEncode

    oneThirdSize = (int)(len(dataEncode)/3)
    sqrtSize = (int) (np.ceil(math.sqrt(oneThirdSize)))

    pixelsNeeded = (int)(sqrtSize*sqrtSize)

    diffPixelCount = (int) (pixelsNeeded - oneThirdSize)
    for i in range((int)(diffPixelCount)):
        dataEncode = bytearray(b'\x00') + bytearray(b'\x00') + bytearray(b'\x00') + dataEncode
        
    array = np.zeros([sqrtSize, sqrtSize, 3], dtype=np.uint8)
    for y in range(sqrtSize):
        for x in range(sqrtSize):
            array[y][x] = [dataEncode[(x*3)+(y*sqrtSize*3)], dataEncode[(x*3+1)+(y*sqrtSize*3)], dataEncode[(x*3+2)+(y*sqrtSize*3)]]

    arrayRemove = 0
    for y in range(sqrtSize):
        removeRow = True
        for x in range(sqrtSize):
            emptyArray = [0,0,0]
            if list(array[y][x]) != emptyArray:
                removeRow = False
                break
        if removeRow:
            arrayRemove = arrayRemove + 1
        else:
            break
    array = array[arrayRemove:]

    img = Image.fromarray(array)
    img.save(imagePath)


def imageToData(imagePath):
    img = list(Image.open(imagePath).getdata())

    encodedData = b''
    for imgData in img:
        encodedData = encodedData+bytearray(imgData)
    toRemove = 0
    
    for i in encodedData:
        if (i == 0): 
            toRemove = toRemove + 1
        else:
            break
    encodedData = encodedData[toRemove:]
    decoded=(encodedData).decode('utf-8')
    print(decoded)
    return decoded

imagePath = 'testrgb.png'
data='''a'''
dataToImage(data, imagePath)

imageToData(imagePath)