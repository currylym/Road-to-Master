<!-- TOC -->

- [1. python原理](#1-python%E5%8E%9F%E7%90%86)
  - [1.1. 基本数据结构](#11-%E5%9F%BA%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
    - [1.1.1. set](#111-set)
    - [1.1.2. dict](#112-dict)
  - [1.2. 函数理解](#12-%E5%87%BD%E6%95%B0%E7%90%86%E8%A7%A3)
    - [1.2.1. 函数传值还是传引用?](#121-%E5%87%BD%E6%95%B0%E4%BC%A0%E5%80%BC%E8%BF%98%E6%98%AF%E4%BC%A0%E5%BC%95%E7%94%A8)
  - [1.3. 随机数实现](#13-%E9%9A%8F%E6%9C%BA%E6%95%B0%E5%AE%9E%E7%8E%B0)
  - [1.4. 内部排序](#14-%E5%86%85%E9%83%A8%E6%8E%92%E5%BA%8F)
  - [1.5. 线程/进程/协程](#15-%E7%BA%BF%E7%A8%8B%E8%BF%9B%E7%A8%8B%E5%8D%8F%E7%A8%8B)
  - [1.6. 装饰器](#16-%E8%A3%85%E9%A5%B0%E5%99%A8)
  - [1.7. MAX_VALUE](#17-maxvalue)

<!-- /TOC -->

# 1. python原理

## 1.1. 基本数据结构

### 1.1.1. set

### 1.1.2. dict

## 1.2. 函数理解

### 1.2.1. 函数传值还是传引用?

```
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

## 1.3. 随机数实现

## 1.4. 内部排序

## 1.5. 线程/进程/协程

## 1.6. 装饰器

## 1.7. MAX_VALUE

```
import sys
print(sys.maxsize)
```