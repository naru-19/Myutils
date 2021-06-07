# Myutils

If you already have narutils and want to use updated narutils,please "pip uninstall narutils".

```
pip install git+https://github.com/naru-19/Myutils
```


## 1.decoration tool





*sample.py*

```python
from narutils import *
decopri_title("naru","narudayo")
print("")
print("")
decopri("narudayo!")
```

*output*

```
                                 naru :narudayo                                 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                   narudayo!                                   
--------------------------------------------------------------------------------
```

## 2.graph tool
*sample.py*

```python
x=[1,2,3]
y=[2,3,4]
savegraph(x=x,y=y,title="test",xlabel="x",ylabel="y",filepath="./",overwrite=False)
```

*output*

(saved as ./test.png)



![test](https://user-images.githubusercontent.com/61283753/119245185-2c7e9c80-bbb2-11eb-8686-8b0d8c484dbd.png)



|   argument    |                         description                          |
| :-----------: | :----------------------------------------------------------: |
|      x,y      |                             x,y                              |
|     title     |                         graph title                          |
| xlabel,ylabel |                  x-axis label,y-axis label                   |
|   filepath    |                   filepath for save figure                   |
|   overwrite   | If there is a same name file,<br> you can over write it when overwrite=True |


## 3.make random color

*sample.py*
```python
from narutils import *
decopri("norm=True")
col=randcol(15,True)
display(col)
decopri("norm=False")
col=randcol(15,False)
display(col)
```

*output*

```
--------------------------------------------------------------------------------
                                   norm=True                                   
--------------------------------------------------------------------------------
array([[0.23529412, 0.54901961, 0.17647059],
       [0.56862745, 0.21568627, 0.60784314],
       [0.47058824, 0.41176471, 0.43137255],
       [0.98039216, 0.47058824, 0.37254902],
       [1.        , 0.2745098 , 0.90196078],
       [0.58823529, 0.19607843, 0.23529412],
       [0.78431373, 0.29411765, 0.15686275],
       [0.03921569, 0.31372549, 0.03921569],
       [0.33333333, 0.74509804, 0.1372549 ],
       [0.94117647, 0.76470588, 0.1372549 ],
       [0.66666667, 0.54901961, 0.35294118],
       [0.58823529, 0.1372549 , 0.88235294],
       [0.09803922, 0.01960784, 0.05882353],
       [0.07843137, 0.68627451, 0.21568627],
       [0.35294118, 0.        , 0.70588235]])
--------------------------------------------------------------------------------
                                   norm=False                                   
--------------------------------------------------------------------------------
array([[160,  15,  80],
       [155, 105,  40],
       [ 35,  25, 200],
       [ 65,  75, 105],
       [ 45,  40,  95],
       [115,  85,  15],
       [115, 170, 230],
       [155, 245,  35],
       [125,   5, 205],
       [185,  95,  60],
       [ 95,  15,  30],
       [ 65, 200, 100],
       [175, 255,  85],
       [ 30, 185, 165],
       [ 45,  15, 155]])
```


## 4.rgb to hex

*sample.py*
```python
from narutils import *

rgb=[255,255,255]
hex=rgb2hex(rgb)
print(hex)

rgb=[180,200,25]
hex=rgb2hex(rgb)
print(hex)

```

*output*

```
ffffff
b4c819
```

## 5.makedir

*sample.py*
```python
from narutils import *
paths="./test1/test2/test3"
makedir(paths)
```
*output*

![スクリーンショット 2021-06-07 18 23 43](https://user-images.githubusercontent.com/61283753/120993109-32819980-c7be-11eb-9892-4c0ac44cf2b4.png)




