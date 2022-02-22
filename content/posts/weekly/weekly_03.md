---
title: "Weekly_03"
date: 2022-02-22T15:08:04+08:00
draft: false
categories:
- weekly
tags:
- weekly
summary: 2022/02/13 ~ 2022/02/19
---
- [Link](#link)
  - [Good](#good)
  - [Others](#others)
    - [Python's all(): Check Your Iterables for Truthiness](#pythons-all-check-your-iterables-for-truthiness)
    - [你知道的 JavaScript 知識都有可能是錯的](#你知道的-javascript-知識都有可能是錯的)
    - [前端的设计模式系列-责任链模式](#前端的设计模式系列-责任链模式)
- [Notes](#notes)
  - [Pytest with statement](#pytest-with-statement)
  - [Memory Leak](#memory-leak)
    - [Good tool](#good-tool)
    - [How to examine](#how-to-examine)
    - [Flask vs Fastapi](#flask-vs-fastapi)
    - [Cgroup](#cgroup)
    - [Capture signal](#capture-signal)
- [Waiting read link](#waiting-read-link)

# Link
## Good

## Others
### Python's all(): Check Your Iterables for Truthiness
https://realpython.com/python-all/

[Why does all() return True if the iterable is empty?]( https://blog.carlmjohnson.net/post/2020/python-square-of-opposition/)

- Inherently negative constants, like None and False
- Numeric types with a zero value, like 0, 0.0, 0j, Decimal("0"), and Fraction(0, 1)
- Empty sequences and collections, like "", (), [], {}, set(), and range(0)
- Objects that implement .__bool__() with a return value of False or .__len__() with a return value of 0

```python=
>>> all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: all() takes exactly one argument (0 given)
>> all([])
True
>> all({})
True
>> all([None])
False
```

Pass dictionary - Key 

```python=
>> all({0: 'zero'})
False
```

`all()` vs `and` 的比較! 好酷

`all()` 一定會回傳 True/False
`and` 則回傳其中一個運算元


```python=
>>> all(["Hello!", 42, {}])
False
>>> "Hello!" and 42 and {}
{}

>>> all([1, 2, 3])
True
>>> 1 and 2 and 3
3

>>> all([0, 1, 2, 3])
False
>>> 0 and 1 and 2 and 3
0

>>> all([5 > 2, 1 == 1])
True
>>> 5 > 2 and 1 == 1
True
```

可在多個 condition 做整理，重覆運用設定的 condition 
```python=
>>> def is_integer(x):
...     return isinstance(x, int)
...

>>> def is_between(a=0, b=100):
...     return lambda x: a <= x <= b
...

>>> def is_even(x):
...     return x % 2 == 0
...

>>> validation_conditions = (
...     is_integer,
...     is_between(0, 100),
...     is_even,
... )

>>> for x in (4.2, -42, 142, 43, 42):
...     print(f"Is {x} valid?", end=" ")
...     print(all(condition(x) for condition in validation_conditions))
...
Is 4.2 valid? False
Is -42 valid? False
Is 142 valid? False
Is 43 valid? False
Is 42 valid? True
```

### 你知道的 JavaScript 知識都有可能是錯的
> From StarBugs weekly #119
https://blog.huli.tw/2022/01/30/how-to-validate-javascript-knowledge/?fbclid=IwAR17M-W6YRBGF01YI0DaFNmY1_mYRIJQxcKcXBagl5U3R9T6khmTHlngCSg

在 javascript 上的雷要如何去排除，要如何獲得較正確的知識，這篇介紹了 ECMAScript 的 script，通過他可理清先前認知上其實是錯誤的知識


### 前端的设计模式系列-责任链模式
https://juejin.cn/post/7060851296491798535

**責任鏈**
感覺像是 linked list，每個節點都設有 `setNext` 到下一個處理，如何該節點有錯或結果，則提早斷掉回傳結果
```python=
class ItemParent:
    def start(self):
        is_ok = self.run()
        if is_ok and :
            if self.next is not None:
                return self.next.run()
            return {'state': 'Finished'}
            
        return {'state': "early break"}
    def setNext(self, next_item):
        self.next = next_item
class ItemA(ItemParent):
    def run(self):
        print('itema')
        return True
    
class ItemB(ItemParent):
    def run(self):
        print('itemb')
        return True
        
if __name__ == '__main__':
    a = ItemA()
    b = ItemB()
    a.setNext(b)
    
    a.setNext(b)
```
# Notes
## Pytest with statement
https://stackoverflow.com/questions/54634817/mocking-a-class-used-in-a-with-statement

```python=
with temp.func() as f:
    f.method()
```

```python=
moc = Mock()
mock_temp = moc.func.return_value.__enter__.return_value
mock_temp.method.return_value = 'HELLO'
```

## Memory Leak
- Bad usage: cyclic reference, global 
- Not good on `traceback` sys.exc_info
- Overwirte `__del__` might have problem on GC

### Good tool
- `tracemalloc` to snapshot

### How to examine
- GC have unreachable/uncollectable problem -> 'cause have bad code structure
- Process monitor required to mointor information on log
    - `process.memory_info().rss/1024 ** 2`
- OCP console web UI?

user is not familiar with deployment tool, eg. k8s/gunicorn/process/memory, what could DE promote this to DA team?

### Flask vs Fastapi
- FastAPI take lots of memory?


### Cgroup

### Capture signal
- Output log if SIGTERM? 
- but what happended if graceful shutdown timeout
- sigkill

gunicorn has sigterm
fastapi could be


# Waiting read link
https://www.bogotobogo.com/Linux/linux_process_and_signals.php
 https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E5%BB%BA%E6%A8%A1%E8%AF%AD%E8%A8%80

