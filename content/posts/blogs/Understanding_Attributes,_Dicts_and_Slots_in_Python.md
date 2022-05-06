---
title: "Understanding Attributes, Dicts and Slots in Python"
date: 2022-05-06T16:59:54+08:00
draft: false
categories:
- linkPage
tags:
- Python
summary: "tags: Python"
---

https://bas.codes/posts/python-dict-slots

**預備知識**

class attribute/instance attribute 跟 `__dict__` 的關聯

- class attribute 在 class 的 `__dict_-` 裡面
- instance attribute 在 class 實體化後 instance 裡的 `__dict__` 內
- class attribute 是被每個 instance 共享

下面就是將 instance attribute 與 class attribute 連動在一起

```python=
class Borg:
    _shared = {}
    def __init__(self):
        self.__dict__ = self._shared
```

可以 read/set instance attribute 來改變 class attribute

而且我們可以讀取 `<instance>.value` 來取得 instance 的 `__dict__` 的值，但反過來如果是 `<class>.value` 就不行

```python=
>>> borg_1 = Borg()
>>> borg_2 = Borg()
>>> 
>>> borg_1.value = 42
>>> borg_2.value 
42
```

文章最後是提到 attribute 的記憶體使用量

利用 `__slots__` 來 overwrite `__dict__` 的預設

因為是使用 `__dict__` 的 dictionary，會佔較大的記憶體空間，所以蓋掉用比較小的 data type，或許可以協助釋放更多空間

