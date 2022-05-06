---
title: "Provide Multiple Constructors in Your Python Classes"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- python class
summary: "tags: python class"
---
https://realpython.com/python-multiple-constructors/

- `__new__` object creation
- `__init__` object initialization
- python 沒有直接支援 overloading (文中有寫原因)

[Python function overloading](https://stackoverflow.com/questions/6434482/python-function-overloading): 利用 module::multipledispatch 來實現

- `__call__` 在實體化的直接呼叫

```python=
>>> class Person:
...     def __init__(self, name):
...         self.name = name
...         
...     def __call(self):
...         print(f"I'm {self.name}")

>>> person = Person('kiwi')
>>> person()
I'm kiwi
```

文章接下來都是 classmethod 的介紹，可以參考一下，更可順便跟 staticmethod 做個比較

[`dict.fromkeys(iterable)`](https://docs.python.org/dev/library/stdtypes.html?highlight=strip#dict.fromkeys) !! 在已知 key 的時候可以先設定 default value 產出新的 dictionary


```python=
>>> names = ['Alice', 'Bob', 'Cindy']
>>> bank_accounts = dict.fromkeys(names, 0)
>>> bank_accounts
{'Alice': 0, 'Bob': 0, 'Cindy': 0}
```

還有其他 classmethod 在基本的 datatype，像是 int, float 


datetime 也是一堆 classmethod
```python=
>>> from datetime import date
>>> from time import time

>>> # Standard constructor
>>> date(2022, 1, 13)
datetime.date(2022, 1, 13)

>>> date.today()
datetime.date(2022, 1, 13)

>>> date.fromtimestamp(1642110000)
datetime.date(2022, 1, 13)
>>> date.fromtimestamp(time())
datetime.date(2022, 1, 13)

>>> date.fromordinal(738168)
datetime.date(2022, 1, 13)

>>> date.fromisoformat("2022-01-13")
datetime.date(2022, 1, 13)
```

看到了一個新潮的玩意兒: 在 python3.8 後，新增了 `@singledispatch` / `@singledispatchmethod` 在 functools

感覺實現了 overloading 

```python=
# demo.py

from functools import singledispatchmethod

class DemoClass:
    @singledispatchmethod
    def generic_method(self, arg):
        print(f"Do something with argument of type: {type(arg).__name__}")

    @generic_method.register
    def _(self, arg: int):
        print("Implementation for an int argument...")

    @generic_method.register(str)
    def _(self, arg):
        print("Implementation for a str argument...")
```

利用 `@singledispatchmethod` 做登記，代表此 method 是 default。接下來在用這個 method 當做 decorator 去 register 不同 argument type 的 method，當作 overloading

你可以直接標注格式在 register 內，或是用 type annotation

呼叫的感覺是
```python=
>>> from demo import DemoClass

>>> demo = DemoClass()

>>> demo.generic_method(42)
Implementation for an int argument...

>>> demo.generic_method("Hello, World!")
Implementation for a str argument...

>>> demo.generic_method([1, 2, 3])
Do something with argument of type: list
```


Conclusion from website
- Simulate multiple constructors using optional arguments and type checking
- Write multiple constructors using the built-in @classmethod decorator
- Overload your class constructors using the @singledispatchmethod decorator
