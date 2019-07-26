

# CHP2 函数式编程

## Python中的高阶函数 



## 1，python把函数作为参数

在2.1小节中，我们讲了高阶函数的概念，并编写了一个简单的高阶函数：

```python
def add(x, y, f):
    return f(x) + f(y)
```

如果传入abs作为参数f的值：

```
add(-5, 9, abs)
```

根据函数的定义，函数执行的代码实际上是：

```
abs(-5) + abs(9)
```

由于参数 x, y 和 f 都可以任意传入，如果 f 传入其他函数，就可以得到不同的返回值。



### 任务

利用add(x,y,f)函数，计算：

![](http://img.mukewang.com/54c8a43b00013a9900930027.png)



```python
import math

def add(x, y, f):
    return f(x) + f(y)

print(add(25, 9, math.sqrt))
```



## 2，python中map()函数

**map()**是 Python 内置的高阶函数，它接收一个**函数 f** 和一个 **list**，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。

例如，对于list [1, 2, 3, 4, 5, 6, 7, 8, 9]

如果希望把list的每个元素都作平方，就可以用map()函数：

[![img](http://img.mukewang.com/54c8a7e40001327303410245.png)](http://img.mukewang.com/54c8a7e40001327303410245.png)

因此，我们只需要传入函数f(x)=x*x，就可以利用map()函数完成这个计算：

```
def f(x):
    return x*x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
```

**输出结果：**

```
[1, 4, 9, 10, 25, 36, 49, 64, 81]
```

**注意：**map()函数不改变原有的 list，而是返回一个新的 list。

利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。

由于list包含的元素可以是任何类型，因此，map() 不仅仅可以处理只包含数值的 list，事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。

### 任务

假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用**map()**函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：

输入：['adam', 'LISA', 'barT']
输出：['Adam', 'Lisa', 'Bart']

```python
def format_name(s):
    return s.capitalize()

print map(format_name, ['adam', 'LISA', 'barT'])
```



## 3，python中reduce()函数

**reduce()**接收**一个函数 f，一个list**，但行为和 map()不同，**reduce()传入的函数 f 必须接收两个参数**，reduce()对list的每个元素反复调用函数f，并返回最终结果值。

例如，编写一个f函数，接收x和y，返回x和y的和：

```python
def f(x, y):
    return x + y
```

调用 **reduce(f, [1, 3, 5, 7, 9])**时，reduce函数将做如下计算：

```
先计算头两个元素：f(1, 3)，结果为4；
再把结果和第3个元素计算：f(4, 5)，结果为9；
再把结果和第4个元素计算：f(9, 7)，结果为16；
再把结果和第5个元素计算：f(16, 9)，结果为25；
由于没有更多的元素了，计算结束，返回结果25。
```

上述计算实际上是对 list 的所有元素求和。虽然Python内置了求和函数sum()，但是，利用reduce()求和也很简单。

**reduce()还可以接收第3个可选参数，作为计算的初始值。**如果把初始值设为100，计算：

```
reduce(f, [1, 3, 5, 7, 9], 100)
```

结果将变为125，因为第一轮计算是：

计算初始值和第一个元素：**f(100, 1)**，结果为**101**。

### 任务

Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：

输入：[2, 4, 5, 7, 12]
输出：2*4*5*7*12的结果

```python
def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])
```



## 4，python中filter()函数

**filter()**函数接收一个**函数 f** 和一个**list**，**传入的函数f()**返回值为 **True或 False**，**filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。**

例如，要从一个list [1, 4, 6, 7, 9, 12, 17]中删除偶数，保留奇数，首先，要编写一个判断奇数的函数：

```Python
def is_odd(x):
    return x % 2 == 1
```

然后，利用filter()过滤掉偶数：

```
filter(is_odd, [1, 4, 6, 7, 9, 12, 17])
```

**结果：**[1, 7, 9, 17]

利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串：

```
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
```

**结果：**['test', 'str', 'END']

**注意:** s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。

当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，如下：

```
a = '     123'
a.strip()
```

**结果：** '123'

```
a='\t\t123\r\n'
a.strip()
```

**结果：**'123'

### 任务

请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

```python
import math

def is_sqr(x):
    if (math.sqrt(x))%1==0:
        return x

print filter(is_sqr, range(1, 101))
```

