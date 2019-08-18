



# Chp6 深入python的set和dict

### 一、dict的abc继承关系

```python
from collections.abc import Mapping,MutableMapping
```

dict继承了---->MutableMapping---->继承了 Mapping---->继承了Collection。

```python
a ={} #创建一个dict实例
print(isinstance(a,MutableMapping))
```

dict类型a并不是继承了MutableMapping，而是实现了它的魔法函数。所以可以通过isinstance来判断。



### 二、dict的常用方法

#### `clear`:Remove all items from D

```python
a = {"bobby1":{"company":"imooc"},"bobby2":{"company":"imooc2"}}
a.clear()
```

#### `copy`: a shallow copy of D (浅拷贝)

```python
#copy,返回浅拷贝
new_dict = a.copy() 
new_dict["bobby1"]["company"]="immoc3"
```

运行结果显示a的company也变成了imooc3

#### 调用copy包进行深copy

```python
import copy
new_dict = copy.deepcopy(a)
new_dict["bobby1"]["company"]="immoc3"
```

运行结果显示dict a并没有变化

#### `fromkeys`:iterable的对象作为key返回一个new dict

Returns a new dict with keys from **iterable** and values equal to value

```python
#fromkeys
new_list = ["bobby1","bobby2"] #list是一个iterable对象
new_dict = dict.fromkeys(new_list,{"company":"immoc"}) #list作为key传入，value还是value,这里value也是一个dict
```

#### `get`:如果查找的key不存在，则返回之前定义的返回值

如果直接调用一个不存在的key。则返回KeyError.

```python
new_dict["booby"] #
```

如果使用`get`方法，如果没有这个key，则会返回我们定义好的一个值，空字典{}

```Python
value = new_dict.get("bobby",{})
```

由于不存在bobby这个key。结果返回{}

#### `items()`:返回一个key和value当作一个tuple

```python
for key,value in new_dict.items():
    print(key,value)
```

#### `setdefault`:给一个（可能不存在）的key直接赋值

new_dict里面没有bobby这个key，给它设置一个值为imooc

```python
new_dict = dict.setdefalut("bobby","imooc")
```



#### `update`:将两个iterable对象进行合并

1、直接传递一个dict进入update方法。

```python
new_dict.update({"bobby":"imooc"})
```

2、传递一个iterable对象进来

```python
new_dict.update(bobby="imooc")

#还可以一次传递多个值进来
new_dict.update(bobby="imooc",bobby3="imooc")
```

3、list里面放入tuple的形式传入

```python
new_dict.update([("bobby","imooc")])

#多个tuple
new_dict.update([("bobby","imooc")，("bobby3","imooc")])

#tuple里面放入tuple
new_dict.update((("bobby","imooc")))
```

