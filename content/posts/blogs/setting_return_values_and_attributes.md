---
title: "setting return values and attributes"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- Mock
summary: "tags: Mock"
---
#### set function return value
```python=
>>> mock = Mock()
>>>mock.return_value = 5
>>> mock()
5
```

#### Set module return value
```python=
>>> mock = Mock()
>>> mock.method.return_value = 5
>>> mock.method()
5
```

#### set attribute value
```python=
>>> mock = Mock()
>>> mock.x = 5
>>> mock.x
5
```

#### use class instance

1. 實體化
```python=
>>> mock = Mock()
>>> cursor = mock.connect.cursor.return_value
```

```python=
cursor = connect.cursor()
```

2. 針對實體化的物件
```python=
>>> mock = Mock()
>>> cursor = mock.connect.cursor.return_value
>>> cursor.execute.return_value = ['foo']
>>> cursor.rowcount = 3
```

```python=
>>> cursor = connect.cursor()
>>> cursor.execute('select 1')
['foo']
>>> cursor.rowcount
3
```
