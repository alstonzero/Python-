# Python定制类

首先定义一个Student类，打印一个实例

```python
class Student(object):
    def __init__(self,name):
        self.name = name
print(Student('Michael'))

​```
<__main__.Student object at 0x0000000005CA3E48>
​```
```

得到一个字符串类型的地址

### 1，Python如何把任意变量变成str?

因为任何数据类型的实例都有一个特殊方法 

```python
__str__()
```

当我们print()打印一个list时，调用了

```python
list=[1,2,3,4,5]
print(list.__str__())
```

同样，当我们print()打印Student实例的时候，同样调用了Student实例的`__str__()`方法

```python
print(Student('Michael').__str__())
```



### 2，python中 `__str__`和`__repr__`

如果要把一个类的实例变成 **str**，就需要实现特殊方法__str__()：

```python
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
```

现在，在交互式命令行下用 **print** 试试：

```python
>>> p = Person('Bob', 'male')
>>> print p
(Person: Bob, male)
```

但是，如果直接敲变量 **p**：

```
>>> p
<main.Person object at 0x10c941890>
```

似乎__str__() 不会被调用。

因为 Python 定义了**`__str__()`**和**`__repr__()`**两种方法，`__str__()`用于显示给用户，而**`__repr__()`**用于显示给开发人员。

有一个偷懒的定义`__repr__`的方法：

```python
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__
```

### 任务

请给**Student** 类定义**__str__**和**__repr__**方法，使得能打印出<Student: name, gender, score>：

```python
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %d)'%(self.name,self.gender,self.score)

s = Student('Bob', 'male', 88)
print (s)
```

### 3，python中 __cmp__

对 **int**、**str** 等内置数据类型排序时，Python的 **sorted()** 按照默认的比较函数 **cmp** 排序，但是，如果对一组 **Student** 类的实例排序时，就必须提供我们自己的特殊方法 __cmp__()：

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0
```

上述 Student 类实现了__cmp__()方法，**__cmp__**用实例自身**self**和传入的实例 **s** 进行比较，如果 **self** 应该排在前面，就返回 -1，如果 **s** 应该排在前面，就返回1，如果两者相当，返回 0。

Student类实现了按name进行排序：

```python
>>> L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
>>> print sorted(L)
[(Alice: 77), (Bob: 88), (Tim: 99)]
```

**注意**: 如果list不仅仅包含 Student 类，则 __cmp__ 可能会报错：

```
L = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']
print sorted(L)
```

请思考如何解决。

### 任务

请修改 **Student** 的 **__cmp__** 方法，让它按照分数从高到底排序，分数相同的按名字排序。

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score <s.score:
            return 1
        elif self.score > s.score:
            return -1
        else:
            if self.name < s.name:
                return -1
            elif self.name > s.name:
                return 1
            else:
                return 0

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print( sorted(L))
```



###  4，python中 __len__

如果一个类表现得像一个list，要获取有多少个元素，就得用` __len()__ `函数。

要让 **`__len()__`** 函数工作正常，类必须提供一个特殊方法`__len__()`，它返回元素的个数。

例如，我们写一个 Students 类，把名字传进去：

```Python
class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
```

只要正确实现了**`__len__()`**方法，就可以用**len()**函数返回**Students**实例的“长度”：

```Python
>>> ss = Students('Bob', 'Alice', 'Tim')
>>> print len(ss)
3
```

 

### 任务

斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。

请编写一个**Fib类**，Fib(10)表示数列的前10个元素，**print Fib(10)** 可以打印出数列的前 10 个元素，**len(Fib(10))**可以正确返回数列的个数10。

```Python
class Fib(object):
#非递归方法完成Fib
    def __init__(self, num):
        self.num = num
        self.res = []
        n = self.num 
        a,b = 0,1
        while n>0:
            self.res.append(a)
            a,b = b,a+b
            n-=1
    
    def __str__(self):
        return str(self.res)
        

    def __len__(self):
        return len(self.res)

f = Fib(10)
print( f)
print( len(f))
```



### 5，python中数学运算

Python 提供的基本数据类型 **int、float** 可以做整数和浮点的四则运算以及乘方等运算。

但是，四则运算不局限于int和float，还可以是有理数、矩阵等。

要表示有理数，可以用一个**Rational类**来表示：

```python
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
```

p、q 都是整数，表示有理数 p/q。

如果要让**Rational进行+运算**，需要正确实现`__add__`：

```python
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __str__(self):
        return '%s/%s' % (self.p, self.q)
    __repr__ = __str__
```

现在可以试试有理数加法：

```pythond
>>> r1 = Rational(1, 3)
>>> r2 = Rational(1, 2)
>>> print r1 + r2
5/6
```

### 任务

**Rational类**虽然可以做加法，但无法做减法、乘方和除法，请继续完善Rational类，实现四则运算。

**提示：**
减法运算：`__sub__`
乘法运算：`__mul__`
除法运算：`__div__`

```python
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        if self.p < self.q:
            k = self.p
        else:
            k = self.q
        for x in range(k, 0, -1):
            if self.p%x==0 and self.q%x == 0:
                self.p = self.p / x
                self.q = self.q / x
                break
        return '%s/%s' % (self.p, self.q)

    __repr__ = __str__
        

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
```



### 6，python中类型转换

**Rational**类实现了有理数运算，但是，如果要把结果转为 **int** 或 **float** 怎么办？

考察整数和浮点数的转换：

```python
>>> int(12.34)
12
>>> float(12)
12.0
```

如果要把 **Rational** 转为 **int**，应该使用：

```python
r = Rational(12, 5)
n = int(r)
```

要让**int()**函数正常工作，只需要实现特殊方法__int__():

```python
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
```

**结果如下：**

```python
>>> print int(Rational(7, 2))
3
>>> print int(Rational(1, 3))
0
```

同理，要让**float()**函数正常工作，只需要实现特殊方法**__float__()**。

### 任务

请继续完善Rational，使之可以转型为float。

```python
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p * 1.0 / self.q

print float(Rational(7, 2))
print float(Rational(1, 3))
```



### 7，python中 @property

考察 **Student** 类：

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
```

当我们想要修改一个 **Student** 的 **scroe** 属性时，可以这么写：

```python
s = Student('Bob', 59)
s.score = 60
```

但是也可以这么写：

```python
s.score = 1000
```

显然，直接给属性赋值无法检查分数的有效性。

如果利用两个方法：

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
```

这样一来，**s.set_score(1000)** 就会报错。

这种使用 **get/set** 方法来封装对一个属性的访问在许多面向对象编程的语言中都很常见。

但是写 **s.get_score()** 和 **s.set_score()** 没有直接写 **s.score** 来得直接。

有没有两全其美的方法？----有。

因为Python支持高阶函数，在函数式编程中我们介绍了装饰器函数，可以用装饰器函数把 **get/set** 方法“装饰”成属性调用：

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
```

**注意:** 第一个score(self)是get方法，用@property装饰，第二个score(self, score)是set方法，用@score.setter装饰，@score.setter是前一个@property装饰后的副产品。

现在，就可以像使用属性一样设置score了：

```python
>>> s = Student('Bob', 59)
>>> s.score = 60
>>> print s.score
60
>>> s.score = 1000
Traceback (most recent call last):
  ...
ValueError: invalid score
```

说明对 **score** 赋值实际调用的是 **set方法**。

### 任务

如果没有定义**set方法**，就不能对“属性”赋值，这时，就可以创建一个只读“属性”。

请给**Student**类加一个**grade**属性，根据 **score** 计算 A（>=80）、B、C（<60）。

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
        
    @property    
    def grade(self):
        if self.__score > 80:
            grade = 'A'
        elif self.__score < 60:
            grade = 'C'
        else:
            grade = 'B'
        return grade

s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade
```

### 8，python中 `__slots__`

由于Python是动态语言，任何实例在运行期都可以动态地添加属性。

如果要限制添加的属性，例如，**Student**类只允许添加 **name、gender**和**score** 这3个属性，就可以利用Python的一个特殊的**`__slots__`**来实现。

顾名思义，**`__slots__`**是指一个类允许的属性列表：

```python
class Student(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score
```

现在，对实例进行操作：

```python
>>> s = Student('Bob', 'male', 59)
>>> s.name = 'Tim' # OK
>>> s.score = 99 # OK
>>> s.grade = 'A'
Traceback (most recent call last):
  ...
AttributeError: 'Student' object has no attribute 'grade'
```

**`__slots__`**的目的是限制当前类所能拥有的属性，如果不需要添加任意动态的属性，使用**`__slots__`**也能节省内存。

### 任务

假设**Person**类通过**`__slots__`**定义了**name**和**gender**，请在派生类**Student**中通过**`__slots__`**继续添加**score**的定义，使**Student**类可以实现**name、gender**和**score** 3个属性。

### 9，python中 `__call__`

在Python中，函数其实是一个对象：

```python
>>> f = abs
>>> f.__name__
'abs'
>>> f(-123)
123
```

由于 **f** 可以被调用，所以，**f** 被称为可调用对象。

所有的函数都是可调用对象。

一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法**`__call__()`**。

我们把 **Person** 类变成一个可调用对象：

```python
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend
```

现在可以对 **Person** 实例直接调用：

```python
>>> p = Person('Bob', 'male')
>>> p('Tim')
My name is Bob...
My friend is Tim...
```

单看 **p('Tim')** 你无法确定 **p** 是一个函数还是一个类实例，所以，在Python中，函数也是对象，对象和函数的区别并不显著。

### 任务

改进一下前面定义的斐波那契数列：

```
class Fib(object):
    ???
```

请加一个__call__方法，让调用更简单：

```python
>>> f = Fib()
>>> print f(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```