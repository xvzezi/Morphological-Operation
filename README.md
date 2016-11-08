# Morphological Operation
Author : 许泽资 5140379068
## Introduction
 - 本代码中实现了Morphological Operation的基本操作dilation 与erosion
 - Dilation. 构造```MorOp```对象，传入bitmap，构造二维数组再调用dilation方法  
 就可以传出一个bytes对象，可以用来构造新的图像。新的图像类型必须是  
 L类型，调用方法的时候，必须传入一个二维数组，表述了element structure  
 1表示白色，0表示黑色。
 - erosion. 同上。

## Python Evironment
```Python
python3
pip install Pillow
```

## Implementation Detail
 > ```MorOp```类的构造器需要传入三个对象，第一个是bitmap，是由bytes构成的，每一位描述一个像素点。  
 构造器同时调用```bitmap.bimapToList()```，可以将bitmap转化为二维数组，方便利用。后面在调用  
 dilation与erosion方法时，就可以获取一个一维数组，利用bytes()强制转化就可以了。

 >在调用```dilation()```或者```erosion()```时，需要传入一个二维的element sturcture。其中1代表白色，0  
 代表黑色。内部，通过低效的双重循环，一点一点判断。通过位操作，可以尽量减低效率消耗，提升  
 效率。

## Code Detail
bitmap.py 
```Python
def bitmapToList(bytes, width, height):
    '''
    Get in a bytes sequence, turn it into 2D list
    :param bytes: the bytes of bitmap
    :param width: the width of the image
    :param height: the height of the image
    :return: a 2D list
    '''
```

MorOp.py 
```Python
class MorOp:
    def __init__(self, bitmap, width, height):
        return 
    
     def dilation(self, ele_struct):
        return 

     def erosion(self, ele_struct):
        return 

```