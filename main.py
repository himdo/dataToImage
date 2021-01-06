import numpy as np
from PIL import Image


def dataToImage(data, imagePath):
    module = len(data)%3
    paddingNeeded = 0
    dataEncode = data.encode()
    if module != 0:
        if module == 1:
            paddingNeeded = 2
        elif module == 2:
            paddingNeeded = 1
    for i in range(paddingNeeded):
        dataEncode = bytearray(b'\x00') + dataEncode

    array = np.zeros([ (int)(len(dataEncode)/3), 1, 3], dtype=np.uint8)

    for i in range((int) (len(dataEncode)/3)):
        array[i] = [dataEncode[i*3], dataEncode[i*3+1], dataEncode[i*3+2]]

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
data='1859477846165465464asda8977432112bjjkadasdadq13459xcvm,xcchu'
dataToImage(data, imagePath)

imageToData(imagePath)