

### 一，property 动态属性

通过添加`@property`装饰器，使方法变成属性被调用。

例子中:定义了私有属性_age,但是用`get_age()`和`set_age()`来获得和设置age略显繁琐，因此使用`@property`使方法变为属性那样操作，而且不影响私有变量的性质。

```python
from datetime import date,datetime
class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0 #添加了私有属性age

    #def get_age(self):
    #    return datetime.now().year - self.birthday.year
    
    #def set_age(self,value):
    #    self._age = value

    @property
    def age(self): #把age（）变成属性描述符
        return datetime.now().year - self.birthday.year

    @age.setter    # 对age这个字段进行设置
    def age(self,value):
        self._age = value

if __name__ == "__main__":
    user = User("bobby",date(year=1990,month=1,day=1))
    user.age = 30  #实际上调用了age.setter修饰的方法 ，即等同于 set_age()
    print(user._age) #直接调用属性
    print(user.age) #实际调用property修饰的age()方法，计算出age

"""
30
29
"""
```





1. *`__getattr__`,` __getattribute__`*
2. *`__getattr__` 就是在查找不到属性的时候调用*。通过重写该方法，可以增加定义的自由度。
3. `__getattribute__`最先被调用的方法。首先会调用这个。因此除非定义框架，不要重写该方法。

```python
from datetime import date
class User:
    def __init__(self,info={}):
        self.info = info

    def __getattr__(self, item): #在查找不到调用的属性时，调用这个魔法函数。比如：输入user.name。
        #没有name属性，调用该方法，作为key传入info，输出bobby
        return self.info[item]

    def __getattribute__(self, item):
        return "bobby"

if __name__ == "__main__":
    user = User(info={"company_name":"imooc","name":"bobby"})
    print(user.test)

"""
bobby
"""
```

如果注释掉 `__getattribute__`方法则因KeyError报错。



```python
class User:
    def __new__(cls, *args, **kwargs):
        print (" in new ")
        return super().__new__(cls)
    def __init__(self, name):
        print (" in init")
        pass
a = int()
#new 是用来控制对象的生成过程， 在对象生成之前
#init是用来完善对象的
#如果new方法不返回对象， 则不会调用init函数
if __name__ == "__main__":
    user = User(name="bobby")

```





```python
from datetime import date, datetime
class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

if __name__ == "__main__":
    user = User("bobby", date(year=1987, month=1, day=1))
    user.age = 30
    print (user._age)
    print(user.age)

```

