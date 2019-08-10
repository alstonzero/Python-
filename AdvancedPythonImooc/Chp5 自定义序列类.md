# Chp5 自定义序列类

### 一、Python中的序列分类



### 二、python中序列类型的abc继承关系



```python
from collections import abc

a =[1,2]
c = a+[3,4]

print(c)

"""
[1, 2, 3, 4]
"""
```

就地加

```python
#就地加
a+=(3,4)
a.extend(range(3))
print(a)

"""
[1, 2, 3, 4, 0, 1, 2]
"""
```



```python
a.append((1,2))
print(a)

"""
[1, 2, (1, 2)]
"""
```

**extend()和append()的不同：**extend()通过for循环一个iterable对象，把元素加入；而append()是把数组变为一个值直接加入，而不是进行迭代。



### 四、实现可切片的对象

```python
import numbers

class Group:
    #支持切片操作
    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item,slice):#如果item是切片类型（例如 1:3:1）
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=self.staffs) 
        elif isinstance(item,numbers.Integral):#如果item是一个整数类型。
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return Flase

staffs = ["bobby1", "imooc", "bobby2", "bobby3"]
group = Group(company_name="imooc", group_name="user", staffs=staffs)
sub_group = group[:3] #传入切片类型的item
sub_group2 = group[1] #传入整数类型的item
```





```python
#模式[start:end:step]
"""
    其中，第一个数字start表示切片开始位置，默认为0；
    第二个数字end表示切片截止（但不包含）位置（默认为列表长度）；
    第三个数字step表示切片的步长（默认为1）。
    当start为0时可以省略，当end为列表长度时可以省略，
    当step为1时可以省略，并且省略步长时可以同时省略最后一个冒号。
    另外，当step为负整数时，表示反向切片，这时start应该比end的值要大才行。
"""
aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print (aList[::])  # 返回包含原列表中所有元素的新列表
print (aList[::-1])  # 返回包含原列表中所有元素的逆序列表
print (aList[::2])  # 隔一个取一个，获取偶数位置的元素
print (aList[1::2])  # 隔一个取一个，获取奇数位置的元素
print (aList[3:6])  # 指定切片的开始和结束位置
aList[0:100]  # 切片结束位置大于列表长度时，从列表尾部截断
aList[100:]  # 切片开始位置大于列表长度时，返回空列表

aList[len(aList):] = [9]  # 在列表尾部增加元素
aList[:0] = [1, 2]  # 在列表头部插入元素
aList[3:3] = [4]  # 在列表中间位置插入元素
aList[:3] = [1, 2]  # 替换列表元素，等号两边的列表长度相等
aList[3:] = [4, 5, 6]  # 等号两边的列表长度也可以不相等
aList[::2] = [0] * 3  # 隔一个修改一个
print (aList)
aList[::2] = ['a', 'b', 'c']  # 隔一个修改一个
aList[::2] = [1,2]  # 左侧切片不连续，等号两边列表长度必须相等
aList[:3] = []  # 删除列表中前3个元素

del aList[:3]  # 切片元素连续
del aList[::2]  # 切片元素不连续，隔一个删一个
```



### 五、bisect维护已排序序列



```python
import bisect
from collections import deque

#用来处理已排序的序列，用来维持已排序的序列， 升序
#二分查找
inter_list = deque()
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)

print(bisect.bisect_left(inter_list, 3))
#学习成绩
print(inter_list)
```





### 六、我们什么时候不该使用列表

array和list的一个重要区别就是array只能存放指定的数据类型

```python
#array ,deque
import array

my_array = array.array("i") #生成array需要指明类型。这里指定了int类型。所以my_array只能存放int类型元素
my_array.append(1)
my_array.append("abc")
print(my_array)

"""
TypeError: an integer is required (got type str)
"""
```



### 七、列表推导式、生成器表达式、字典推导式

```python
#用简介的方式去遍历可迭代对象生成需要格式的列表
int_list = [1,2,3,4,5]

qu_list = [item * item for item in int_list]
print (type(qu_list))
int_list = [1,2,-3,4,5]

qu_list = [item if item > 0 else abs(item) for item in int_list]

#笛卡尔积
int_list1 = [1,2]
int_list2 = [3,4]

qu_list = [(first, second) for first in int_list1 for second in int_list2]

my_dict = {
    "key1":"bobby1",
    "key2":"bobby2"
}

#交换一个dict的key和value
# qu_list = [(key, value) for key, value in my_dict.items()]
#
# qu_list2 = list(((key, value) for key, value in my_dict.items()))
#
# for item in qu_list2:
#     print (item)

int_list = [1,2,3,4,5]

def process_item(item):
    return str(item)

int_dict = {process_item(item):item for item in int_list}
#列表生成式，第一：能用尽量用， 因为效率高
print (int_dict)
```


