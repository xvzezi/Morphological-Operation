import math

def bitmapToList(bytes, width, height):
    '''
    Get in a bytes sequence, turn it into 2D list
    :param bytes: the bytes of bitmap
    :param width: the width of the image
    :param height: the height of the image
    :return: a 2D list
    '''
    # indeed needed amount of pixels
    amount = math.floor(width * height / 8)
    print((width, height, amount))

    # process it one-by-one
    output = [[0 for i in range(width)] for i in range(height)]
    mask = 1
    loc = 0
    for i in range(0, amount):
        b_pre = bytes[i]
        for j in range(7, -1, -1):
            y = math.floor(loc / width)
            x = loc % width
            output[y][x] = (b_pre >> j) & mask
            loc += 1
    print(loc)
    return output

from PIL import Image
def test_main():
    a = Image.open("D:/lena-binary.bmp")
    b = a.tobytes()
    print((b[0], b[1]))
    c = bitmapToList(b, a.width, a.height)
    for k in c:
        print(k)
    d = [0] * 256 * 256
    for i in range(0, 256 * 256):
        x = i % 256
        y = math.floor(i / 256)
        if c[y][x] == 1:
            d[i] = 255
    ss = a.convert('L')
    ss.frombytes(bytes(d))
    ss.save("D:/askl.png")
