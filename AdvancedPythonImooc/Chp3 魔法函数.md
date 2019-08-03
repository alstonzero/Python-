## Chp3 魔法函数

### 1， 什么是魔法函数？

魔法函数是python里定义的以双下划线``__``开头和结尾的函数。而且我们不需要去直接调用魔法函数。

**注意点：**

1，魔法函数不属于这个类本身，也不是继承object类的方法，可以理解为独立的存在；

2，当我们在这个类中加入了魔法函数以后，会增强这个类的类型（比如迭代类型，序列类型等），并影响Python语法本身。

3，对于任意一个类都可以添加任意一个（多个）魔法函数 ；

4，一定要使用python提供的魔法函数，自己定义是没有用的。

```Python
class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __getitem__(self,item): #item传进一个index
        return self.employee[item]
    
company = Company(["tom","bob","jane"])
```

比如本例中，当定义了`__getitem__`后，company变成了一个iterable（可迭代类型）。

当用for语句循环company这个对象的时候，解释器寻找是否有`__getitem__`。如果有这个函数，解释器会从头到尾的去尝试。比如从item为0开始一直往后添加直到抛出异常，for循环结束。这实际上是我们的Python语法和魔法函数结合出来的灵活性。