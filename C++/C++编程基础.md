<!-- TOC -->

- [1. C++编程基础](#1-c%e7%bc%96%e7%a8%8b%e5%9f%ba%e7%a1%80)
  - [1.1. Main函数](#11-main%e5%87%bd%e6%95%b0)
  - [1.2. 基础数据类型](#12-%e5%9f%ba%e7%a1%80%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
  - [1.3. class定义](#13-class%e5%ae%9a%e4%b9%89)
  - [1.4. 输入输出](#14-%e8%be%93%e5%85%a5%e8%be%93%e5%87%ba)
  - [1.5. 命名空间](#15-%e5%91%bd%e5%90%8d%e7%a9%ba%e9%97%b4)
  - [1.6. 对象定义和初始化](#16-%e5%af%b9%e8%b1%a1%e5%ae%9a%e4%b9%89%e5%92%8c%e5%88%9d%e5%a7%8b%e5%8c%96)
  - [1.7. 运算符](#17-%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [1.7.1. 算数运算符](#171-%e7%ae%97%e6%95%b0%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [1.7.2. 条件运算符](#172-%e6%9d%a1%e4%bb%b6%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [1.7.3. 关系运算符](#173-%e5%85%b3%e7%b3%bb%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [1.7.4. 逻辑运算符](#174-%e9%80%bb%e8%be%91%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [1.7.5. 复合赋值运算符](#175-%e5%a4%8d%e5%90%88%e8%b5%8b%e5%80%bc%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [1.7.6. 运算符的优先级](#176-%e8%bf%90%e7%ae%97%e7%ac%a6%e7%9a%84%e4%bc%98%e5%85%88%e7%ba%a7)
  - [1.8. 条件和循环](#18-%e6%9d%a1%e4%bb%b6%e5%92%8c%e5%be%aa%e7%8e%af)
    - [1.8.1. 条件语句](#181-%e6%9d%a1%e4%bb%b6%e8%af%ad%e5%8f%a5)
      - [1.8.1.1. `if-else`](#1811-if-else)
      - [1.8.1.2. `switch`](#1812-switch)
    - [1.8.2. 循环语句](#182-%e5%be%aa%e7%8e%af%e8%af%ad%e5%8f%a5)
      - [1.8.2.1. `while`循环](#1821-while%e5%be%aa%e7%8e%af)
      - [1.8.2.2. `for`循环](#1822-for%e5%be%aa%e7%8e%af)
  - [1.9. 如何使用`array`和`vector`](#19-%e5%a6%82%e4%bd%95%e4%bd%bf%e7%94%a8array%e5%92%8cvector)
    - [1.9.1. 定义`array`](#191-%e5%ae%9a%e4%b9%89array)
    - [1.9.2. 定义`vector`](#192-%e5%ae%9a%e4%b9%89vector)
  - [1.10. 指针（`pointer`）](#110-%e6%8c%87%e9%92%88pointer)
    - [1.10.1. 取址运算符（`&`）](#1101-%e5%8f%96%e5%9d%80%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [1.10.2. 提领运算符（`*`）](#1102-%e6%8f%90%e9%a2%86%e8%bf%90%e7%ae%97%e7%ac%a6)
    - [1.10.3. 初始化空指针](#1103-%e5%88%9d%e5%a7%8b%e5%8c%96%e7%a9%ba%e6%8c%87%e9%92%88)
  - [1.11. 文件读写](#111-%e6%96%87%e4%bb%b6%e8%af%bb%e5%86%99)

<!-- /TOC -->
# 1. C++编程基础

## 1.1. Main函数
> 每个C++程序都是从一个名为`main`的函数开始执行的。
```c++
int main()
{
    // main code
}
```
> 函数是一块独立的代码程序序列，包含四个部分：**返回值类型、函数名称、参数列表和函数体**。

## 1.2. 基础数据类型

- 布尔值（`bool`）
- 字符（`char`）
> 有一些特别的内置字符常量，称为转义字符（`escape sequence`）。

|转义字符|含义|
|:-:|:-:|
|`\n`|换行符|
|`\t`|制表符|
|`\0`|`null`|

- 整数（`int`）
- 浮点数

|类型|含义|
|:-:|:-:|
|`float`|单精度浮点数|
|`double`|双精度浮点数|
|`long double`|长双精度浮点数|

- `const`关键字
> 有一些对象在程序执行过程中不应该变动，为了避免误修改，可以借助关键字`const`。
```c++
const int month_in_year = 12;
```

## 1.3. class定义
> `class`的定义一般分为两部分，分别写在不同的文件中。其中之一是所谓的头文件，用来声明该`class`所提供的各种操作行为（`operation`）。另一个文件，程序代码文件，则包含了这些操作行为的实现内容

> 使用例子：
```c++
#include <iostream>
```

## 1.4. 输入输出

> C++标准的“输入/输出库”名为`iostream`，其中包含了相关的整套`class`，用于支持对终端和文件的输入与输出。

- `cout`
```c++
#include <iostream>
using namespace std;
int main()
{
    cout << "hello world!";
}
```

```c++
#include <iostream>
using namespace std;
int main()
{
    //  多行输出
    cout << "hello world!"
         << "curry"
         << "\n";
}
```

- `cin`
```c++
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string user_name;
    cin >> user_name;
    cout << user_name;
}
```

## 1.5. 命名空间

> 所谓命名空间是一种将库名称封装起来的方法。通过这种方法，可以避免和应用程序发生命名冲突的问题（所谓**命名冲突**是指在应用程序中两个不同“实体”具有相同名称，导致程序无法区分两者。命名冲突发生时，程序必须等到命名冲突获得解析（`resolve`）之后才得以继续执行）。

```c++
using namespace std; // 这是最简单的方案
```

## 1.6. 对象定义和初始化
- 用赋值运算符`=`初始化
```c++
int num = 0;
```

- 构造函数语法（`constructor syntax`）
```c++
// 需要多个参数初始化对象时
#include <complex>
complex<double> purei(0,7); // 虚部和实部均为double类型
```
> 注：出现与`complex`之后的尖括号，表示`complex`是一个`template class`（模版类）。

## 1.7. 运算符

### 1.7.1. 算数运算符

|需要注意的运算符|含义|
|:-:|:-:|
|`/`|除法运算（商）|
|`%`|取余数|

### 1.7.2. 条件运算符
```c++
expr ? <cmd1> : <cmd2>;
// expr为真执行cmd1，否则执行cmd2
```

### 1.7.3. 关系运算符

|关系运算符|含义|
|:-:|:-:|
|`==`|相等|
|`!=`|不等|
|`<`|小于|
|`>`|大于|
|`<=`|小于等于|
|`>=`|大于等于|

### 1.7.4. 逻辑运算符

|逻辑运算符|含义|
|:-:|:-:|
|`||`|`OR`|
|`&&`|`AND`|
|`!`|`NOT`|

### 1.7.5. 复合赋值运算符
- `+=,-=,*=,\=,%=`
- 递增/递减运算符`++,--`。有前置和后置两种形式，前置形式中先执行递增或递减操作。

### 1.7.6. 运算符的优先级
- 逻辑运算符`NOT`
- 算数运算符（`/,%,*`）
- 算数运算符（`+,-`）
- 关系运算符（`>,<,>=,<=`）
- 关系运算符（`==,!=`）
- 逻辑运算符`AND`
- 逻辑运算符`OR`
- 赋值运算符

## 1.8. 条件和循环

### 1.8.1. 条件语句

#### 1.8.1.1. `if-else`
```c++
#include <iostream>
using namespace std;
int main()
{
    int num;
    cin >> num;
    if (num == 1)
        cout << "num=" << num << "\n";
    else
    if (num == 2)
        cout << "num=" << num << "\n";
    else
    if (num == 3)
        cout << "num=" << num << "\n";
    else
        cout << "num not in {1,2,3}";
}
```

#### 1.8.1.2. `switch`
```c++
#include <iostream>
using namespace std;
int main()
{
    int num;
    cin >> num;
    switch (num)
    {
        case 1:
            cout << "num=" << num << "\n";
            break;
        case 2:
            cout << "num=" << num << "\n";
            break;
        case 3:
            cout << "num=" << num << "\n";
            break;
        default:
            cout << "num not in {1,2,3}" << "\n";
            break;
    }   
}
```
> 当某个标签和`switch`表达式吻合时，该case标签之后的所有case标签也都会被执行，除非明确使用`break`来结束执行。

### 1.8.2. 循环语句

#### 1.8.2.1. `while`循环

```c++
while (cmd)
{
    // break 直接结束循环
    // continue 直接开始下一次循环
}
```

#### 1.8.2.2. `for`循环
```c++
for ( init-statement ; condition ; expression )
    statement
// init-statement会在循环开始前被执行一次。
// condition用于循环控制，其值会在每次循环迭代之前被计算出来。如果condition为true，statement就会被执行。
// expression会在每次循环结束之后被求值。
```

## 1.9. 如何使用`array`和`vector`

> C++允许我们以内置的`array`（数组）类型或标准库提供的`vector`类型来定义容器。操作通过下标索引即可。
>> *在C++ 中容器被定义为：在数据存储上，有一种对象类型，它可以持有其它对象或指向其它对象的指针，这种对象类型就叫做容器。*

### 1.9.1. 定义`array`
> 要定义`array`，我们必须指定`array`的**元素类型**，还得给予其一个**名称**，并指定其**尺度大小**。
```c++
const int seq_len = 3;
int seq[ seq_size ]; //元素的初始值为0

// 也可直接指定初始值
int seq[ seq_size ] = { 1, 3, 5 };
```
>> **注意**：初始化列表内的元素个数，不能超过`array`的大小。如果小于`array`的大小，其余元素会被初始化为0.此外，也可以让编译器根据初值的数量，自行计算出`array`的大小。

### 1.9.2. 定义`vector`
> 定义`vector`必须要先包含`vector`头文件。`vector`是个`class template`，初始化写法如下。
```c++
#include <vector>
const int seq_size = 3;
vector<int> seq( seq_size )

// 可以借助array初始化vector
int seq[ seq_size ] = { 1, 3, 5 };
vector<int> seq_v( seq, seq+seq_size )
```
> `vector`和`array`存在一些差异，`vector`知道自己的大小是多少。调用`seq_v.size()`即可。

## 1.10. 指针（`pointer`）

> 指针内含某特定类型对象的内存地址。当我们要定义某个特定类型指针时，必须在类型名称之后加上`*`号。
>> 指针为程序引入了一层间接性，我们可以直接操作指针，而不在直接操作对象。指针可以增加程序的弹性，同时也增加了操作复杂度。指针既可以让我们操作指针包含的内存地址，也可以让我们操作指针所指的对象值。
```c++
int ival = 1024;
int *pi; // pi是int类型对象的指针
&ival; // 计算ival的内存地址
int *pi = &ival; // 初始化指针
*pi // 访问指针所指的对象（dereference）
```

### 1.10.1. 取址运算符（`&`）
### 1.10.2. 提领运算符（`*`）
> 访问指针所指的对象。在提领之前应该判断指针是否为空。
```c++
if ( !pi )
{
    // statement
}
```

### 1.10.3. 初始化空指针
> 一个未指向任何对象的指针，其地址值为0。有时候我们称之为`null`指针。
```c++
int *pi = 0;
```

## 1.11. 文件读写