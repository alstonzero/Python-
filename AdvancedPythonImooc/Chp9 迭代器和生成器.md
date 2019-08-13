# Chp9 迭代器和生成器

### 一、Python中的迭代协议

```python
#什么是迭代协议
#迭代器是什么？ 迭代器是访问集合内元素的一种方式， 一般用来遍历数据
#迭代器和以下标的访问方式不一样， 迭代器是不能返回的, 迭代器提供了一种惰性方式数据的方式
#[] list , __iter__

from collections.abc import Iterable, Iterator
a = [1,2]
iter_rator = iter(a)
print (isinstance(a, Iterable))
print (isinstance(iter_rator, Iterator))
```



### 二、什么是迭代器(Iterator)和可迭代对象(Iterable)

```python
from collections.abc import Iterator

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        #真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

if __name__ == "__main__":
    company = Company(["tom", "bob", "jane"])
    my_itor = iter(company)
    # while True:
    #     try:
    #         print (next(my_itor))
    #     except StopIteration:
    #         pass

    # next(my_itor)
    for item in company:
        print (item)
```



### 三、生成器函数的使用

理解生成器才能理解协程

#### 函数里有yield关键字，就是生成器函数

```python
def gen_func():
    yield 1

def func():
    return 1

if __name__ == "__main__":
    gen = gen_func()    
    re = func()        #re:1
    pass

```

gen生成了一个对象。只要调用gen_func()，则返回一个生成器对象。在python编译字节码时产生。

**生成过程:** Python在运行之前会将代码变成字节码，在编译的时候发现了函数里边时yield，所以就会生成一个生成器对象。

#### 生成器对象是可迭代的（实现了迭代器协议）

```python
def gen_func():
    yield 1
    yield 2
    yield 3
    
if __name__ = "__main__":
    gen = gen_func()
    for value in gen:
        print(value)
""
1
2
3
""
```

普通的函数只能有一个return。

但是，生成器对象实现了迭代协议，产生一个值之后，通过`yield`把值返回给调用方，然后调用`next`获得下一个值。



#### 惰性求值/延迟求值

实现斐波那契数列 0 1 1 2 3 5 8 13......



**方法1：**

```python
def fib(index):
    if index <= 2:
        return 1
    elif:
        return fib(index-1)+fib(index-2)
```

缺点：上例只能打印出特定的index所对应的值。看不到中间的过程。



**方法2**

可以进行改进使其返回一个list

```

```



**方法3：**

通过生成器表达式进行改进：代码简单，节省内存

```python
def gen_fib(index):
    n,a,b = 0,0,1
    while n < index:
        yield b
        a,b = b,a+b
        n += 1

for data in gen_fib(10):
    print(data)
```

**与方法1的区别：**

生成器函数会把中间的计算过程中的每一个数据都yield出来。yield出来后，只需要for循环向下继续取得元素。



### 四、Python是如何实现生成器

```python


```



### 五、生成器在UserList中的应用

```python


```



