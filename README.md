# Myutils

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
