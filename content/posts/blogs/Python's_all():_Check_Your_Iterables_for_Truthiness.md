---
title: "Python's all(): Check Your Iterables for Truthiness"
date: 2022-05-06T16:56:33+08:00
draft: false
categories:
- linkPage
tags:
- pytest
- testing
- python
summary: "tags: pytest, testing, python"
---
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
