<!-- TOC -->

- [1. python原理](#1-python原理)
    - [1.1. 基本数据结构](#11-基本数据结构)
        - [1.1.1. set](#111-set)
        - [1.1.2. dict](#112-dict)
    - [1.2. 函数理解](#12-函数理解)
        - [1.2.1. 函数传值还是传引用?](#121-函数传值还是传引用)
        - [1.2.2. *args与**kwargs](#122-args与kwargs)
    - [1.3. 随机数实现](#13-随机数实现)
    - [1.4. 内部排序](#14-内部排序)
    - [1.5. 线程/进程/协程](#15-线程进程协程)
    - [1.6. 装饰器](#16-装饰器)
    - [1.7. MAX_VALUE](#17-max_value)
    - [1.8. nonlocal](#18-nonlocal)

<!-- /TOC -->

# 1. python原理

## 1.1. 基本数据结构

### 1.1.1. set

### 1.1.2. dict

## 1.2. 函数理解

### 1.2.1. 函数传值还是传引用?

```python
# 参考https://www.cnblogs.com/shizhengwen/p/6972183.html
# 传对象，看有没有新的赋值操作

# case1
def foo(arg):
    arg = 2
    print(arg)
 
a = 1
foo(a)  # 输出：2
print(a) # 输出：1

# case2
def bar(args):
    args.append(1)
 
b = []
print(b)#　输出：[]
print(id(b)) # 输出：4324106952

bar(b)
print(b) ＃　输出：[1]
print(id(b))  # 输出：4324106952
```

### 1.2.2. *args与**kwargs
>首先明白向python函数传递参数的方式有两种：   
- 位置参数（positional argument）   
- 关键词参数（keyword argument）

>现在再来看\*args与\*\*kwargs的区别，两者都是python中的可变参数。 
\*args表示任何多个无名参数，它本质是一个tuple； 
\*\*kwargs表示关键字参数，它本质上是一个dict； 
并且同时使用*args和\*\*kwargs时，必须*args参数列要在\*\*kwargs前

```python
def fun(*args,**kwargs):
    print('args=', args)
    print('kwargs=',kwargs)
fun(1,2,3,4,A='a',B='b',C='c',D='d')

#输出
#args= (1, 2, 3, 4)
#kwargs= {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
```

## 1.3. 随机数实现

## 1.4. 内部排序

## 1.5. 线程/进程/协程

## 1.6. 装饰器

## 1.7. MAX_VALUE

```python
import sys
print(sys.maxsize)
```

## 1.8. nonlocal

>非局部声明变量指代的已有标识符是最近外面函数的已声明变量，但是不包括全局变量。这个是很重要的，因为绑定的默认行为是首先搜索本地命名空间。nonlocal声明的变量只对局部起作用，离开封装函数，那么该变量就无效。
非局部声明不像全局声明，我们必须在封装函数前面事先声明该变量
非局部声明不能与局部范围的声明冲突

```python
# example
count = 1

def a():
    count = 'a函数里面'  　　#如果不事先声明，那么函数b中的nonlocal就会报错
    def b():
        nonlocal count
        print(count)
        count = 2
    b()
    print(count)

if __name__ == '__main__':
    a()
    print(count)

#输出
#a函数里面
#2
#1
```
