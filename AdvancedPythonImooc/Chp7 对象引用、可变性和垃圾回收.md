# Chp7 对象引用、可变性和垃圾回收



### 一、Python中的变量是什么---”便利贴“

Python中的变量类似于Java中的引用式变量，最好理解为附加在对象上的标注。

**Python和Java中变量的本质不一样：** 

在Java中声明一个变量的时候首先需要声明这个变量的类型（比如：int，String）声明了这个类后，虚拟机就会在内存中给它申请一个空间，这个空间的大小和变量的类型相关。

**Python的变量实质上是一个指针**，这个指针指向int类型或者String类型，这个指针本身的大小是固定的，与指向的对象（int，String等）所占内存的大小无关。因此，只需要找到这个指针，这个指针就会去内存中找到(int或者String)对象。我们也可以把Python变量理解为一个**便利贴**，既可以贴在int对象也可以贴在String对象上面。

#### 例1：

```python
a = 1     #step 1
a = "abc" # step 2
```

#1，首先在内存中声明了一个int类型的对象1，然后把a贴在对象1上面。

#2，由于变量a本身是一个便利贴，因此也可以贴在String类型的对象abc上。

**过程:** 先生成对象，然后把便利贴a，贴在对象上面。变量a的大小是固定的，且a没有类型。



#### 例2：

```Python
a = [1,2,3]
b = a
b.append(4)
print(a)

"""
[1,2,3,4]
"""
```

通过对b进行修改，a也同样发生了变化。

**本质上：a和b贴在同一个list对象[1,2,3]上。**

#### 例3：通过`id()`和`is`来进一步证明。

```python
print(id(a),id(b)) #分别打印a，b所指向的对象的id
print(a is b)

"""


"""
```

id(a)与id(b)相等，`a is b`结果为True，进一步证明了a与b所指向的对象相同。



### 二，==和is的区别

**`=`用来判断值是否相等，内部调用了`__eq__`这个魔法函数**

**`is`用来判断两个对象的id是否相等，即判断是否是同一个对象。**

#### 例1：分别给a和b赋值一个list

```python
a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
print(a is b)
print(id(a),id(b))

"""
True
Flase
39724040 39724616
"""
```

1，a与b的值时相等的

2，a和b分别指向两个不同的对象。

通过使用`=`赋值符号，分别给a和b进行赋值，而不是指向一个对象时，Python会重新声明一个对象。



#### 例2：对于小整数和小字符串的inter机制

```python
a = 1
b = 1
print(a is b)
print（id(a),id(b)）

"""
True

"""

```

**Python内部有一个inter机制:** 当声明一定范围内的小整数或小字符串时，会建立全局唯一的一个对象。当再次遇到这个对象时，则直接指向之前创建的全局的这个对象，不会再创建新的对象。



#### 例3： 确认实例化对象所属的类

`isinstance()`和`type() is`

```python
class People:
    pass

person = People()

#if isinstance(person,People):
if type(people) is People:
    print("yes")
```



### 三、`del`语句和垃圾回收

#### Python中垃圾回收采用的是 引用计数器

**当del某一个变量时，并不回收这个变量指向的对象，只有当计数器减到0的时候，才会回收对象。**

```python
a = object（）
b = a
#当前引用计数器为2
del a #将引用计数器减一
print(b)
print(a)
```

结果:

object b可以被打印出，而a返回name 'a' not defined。

证明了`del`只是删除了变量a，并没有删除对象object。



#### Python解释器回收对象实质是调用该对象的 `__del__`魔法函数

因此当我们希望某对象被垃圾回收时，释放某些资源，我们就可以重载`__del__`魔法函数

```python
class A:
    def __del__(self):
        pass #可以在这里实现我们自己的逻辑
```



### 四、一个经典的参数错误

#### 尽量不要在类的属性中传入可修改的类型，如list,dict

```python
def add(a,b):
    a += b  #就地将a修改
    return a

class Company:
    def __init__(self,name,staffs=[]):
        self.name = name
        self.staffs = staffs
    def add(self,staff_name):  #新员工入职
        self.staffs.append(staff_name)
    def remove(self,staff_name):
        self.staffs.remove(staff_name)


if __name__ == "__main__":
    com1 = Company("com1",["bobby1","bobby2"])
    com1.add("bobby3")
    com1.remove("bobby1")
    print(com1.staffs)
    
    #com2和com3这两个实例没有传入list进去
    com2 = Company("com2") 
    com2.add("bobby")
    print(com2.staffs)
    
    com3 = Company("com3")
    com3.add("bobby5")
    print(com2.staffs)
    print(com3.staffs)
    
    print(com2.staffs is com3.staffs)
    
    a = 1
    b = 2
    c = add(a,b)
    print(c)
    print(a,b)
    
    a = [1,2]
    b = [3,4]
    
    print(c)
    print(a,b)
    

```

结果：

com2.staffs 和 com3.staffs的结果相同。

**原因分析:**

1，类的属性中传入的list是可变对象

2，在实例化com2和com3过程中都没有传入list，这两个实例使用的都是默认的list。因此，com2和com3共用了同一个默认的list，所以com2和com3的staffs_list是一样的。

同样也可以通过`Company.__init__.__defaults`来获得默认的list，结果与com2和com3的staffs list相同。而com1在实例化时传入了自己的list，因此不会指向默认的这个list。

#### 当传入list或dict这种可以被修改的类型进入函数中，一定要注意可能随时被修改。因此可用来排查错误。

