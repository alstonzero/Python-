# Chp4 深入类和对象

### 一、鸭子类型和多态

#### 1，什么是鸭子类型(duck typing)：

当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。

在鸭子类型中，关注点在于**对象的行为，能作什么**；而不是关注对象所属的类型。

#### 先看例子1

**鸭子类型在不使用继承的情况下使用了多态。**

```python
class Cat(object):
    def say(self):
        print("i am a cat")

class Dog(object):
    def say(self):
        print("i am a dog")
class Duck(object):
    def say(self):
        print("i am a duck")

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()
```

Cat ,Dog,Duck这三个类共同实现了同一个方法say()。在animal_list中不同的类，而这些类都有一个共同的say()方法，通过调用say()方法，就实现了多态。而不是像Java那样，继承父类，并重写父类方法。

**什么是鸭子类型？**所有的类或者所有的对象都实现了一个共同的方法，这个方法名要一样。因此这些类都可以归为一种类型。

#### 再看例子2

```Python
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob", "jane"])

a = ["bobby1", "bobby2"]
b = ["bobby2", "bobby"]
name_tuple = ["bobby3", "bobby4"]
name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")
a.extend()
print(a)
```

extend()方法中可以传入一个可迭代对象(iterable)。不需要传入的对象是具体的list或tuple或者set。因此，我们自己实现一个可迭代的类，同样也可以传进extend()方法。

实际上，extend()方法调用的是被传入对象的迭代器。当Company类实现了`__getitem__`方法后，它就变成了一个可迭代的对象。因此可以被extend()调用。

`__getitem__`方法并不需要继承某个类来实现，我们可以把这个函数塞到任何一个对象当中，并不需要这个对象有什么前置条件。

Python的魔法函数也充分地利用了鸭子类型，在Python中的很多内置对象中，通过写入不同的魔法函数（这些魔法函数会被Python解释器本身识别）对Python类型进行分组。比如集合、序列相关，迭代相关，with上下文管理器等。因此我们也可以通过实现与某内置类相同的魔法函数，使自定义的类拥有与其相同的功能。

#### 鸭子类型+魔法函数 构成了Python语言的基础

**鸭子类型贯穿Python设计的始终。一个class类有什么特性?属于什么类型? 是看这个类实现了什么魔法函数**

Python不是通过继承某个类或者某个“接口”来具有某些特性，而是通过实现指定的魔法函数，来使这个类成为指定的某种类型。

#### Duck Typing的总结:

1. python 不支持多态， 因为 python 不用支持多态，python 崇尚鸭子类型。
2. 当看到一只鸟走起来像鸭子，游泳像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子。
3. 鸭子类型和 python 协议（魔法函数）结合起来理解比较容易， 如一个类实现了迭代协议则该类则是迭代类型

### 二、抽象基类(abc模块)

Python中抽象基类可以理解为Java中的接口。Java中只能继承一个类，但是可以继承多个接口，接口不能实例化。同样Python中的**抽象基类同样也不能实例化。**

**注意**：Python是动态语言，动态语言是没有变量的类型的。所以动态语言少了编译时检查错误的环境。

