from PIL import Image
from morOp.bitmap import bitmapToList

class MorOp:
    def __init__(self, bitmap, width, height):
        self.bitmap = bitmap
        self.width = width
        self.height = height
        self.bin = bitmapToList(bitmap, width, height)

    def dilation(self, ele_struct):
        # element structure analysis
        es_width = len(ele_struct[0])
        es_height = len(ele_struct)

        # loop definition
        h_begin = 0
        h_end = self.height - es_height + 1
        w_begin = 0
        w_end = self.width - es_width + 1
        kl_bin = [[0 for i in range(self.width)] for i in range(self.height)]
        for i in range(h_begin, h_end):
            for j in range(w_begin, w_end):
                hash = 0
                for m in range(0, es_height):
                    for n in range(0, es_width):
                        hash += self.bin[i + m][j + n] & ele_struct[m][n]
                if hash > 0:
                    kl_bin[int(i + es_height / 2)][int(j + es_width / 2)] = 1

        sbin = [0] * self.height * self.width
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.bin[i][j] == 1 or kl_bin[i][j] == 1:
                    sbin[i * self.width + j] = 255
        return sbin

    def erosion(self, ele_struct):
        # element structure analysis
        es_width = len(ele_struct[0])
        es_height = len(ele_struct)
        num = 0
        for i in range(0, es_height):
            for j in range(0, es_width):
                if ele_struct[i][j] == 1:
                    num += 1

        # loop definition
        h_begin = 0
        h_end = self.height - es_height + 1
        w_begin = 0
        w_end = self.width - es_width + 1
        kl_bin = [[0 for i in range(self.width)] for i in range(self.height)]
        for i in range(h_begin, h_end):
            for j in range(w_begin, w_end):
                hash = 0
                for m in range(0, es_height):
                    for n in range(0, es_width):
                        hash += self.bin[i + m][j + n] & ele_struct[m][n]
                if hash == num:
                    kl_bin[int(i + es_height / 2)][int(j + es_width / 2)] = 1

        sbin = [0] * self.height * self.width
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.bin[i][j] == 1 and kl_bin[i][j] == 1:
                    sbin[i * self.width + j] = 255
        return sbin


def test_main():
    img = Image.open("D:/lena-binary.bmp")
    bitmap = img.tobytes()
    mp = MorOp(bitmap, img.width, img.height)
    es = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    # re = mp.dilation(es)
    re = mp.erosion(es)
    ss = img.convert('L')
    ss.frombytes(bytes(re))
    ss.save("D:/result2.png")

test_main()
