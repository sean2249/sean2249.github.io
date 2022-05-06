---
title: "Which string formatting method should you use"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- python
summary: "tags: python"
---
https://realpython.com/python-string-formatting/#which-string-formatting-method-should-you-use

python string format 有四種
#### 1. 使用 %
從 C 的 prinft 導入過來的
```python=
>>> name = 'bob'
>>> 'hello %s' % name
hello bob
```

#### 2. 使用 format
這應該是 python3.5 前很常用的方法，不過很慢
```python=
>>> name = 'bob'
>>> 'hello {}'.format(name)
hello bob
```

#### 3. 使用 f-string
python3.6 導入，唯一推薦
```python=
>>> name = 'bob'
>>> f'hello {name}'
hello bob
```

#### 4. 使用 Template (極少見)
需要額外 import 
```python=
>>> from string import Template
>>> t = Template('hello $name')
>>> t.substitue(name=name)
hello bob
```

整體速度，印象中是 f-string > % > format > Template
Template 的好處在於可以給 user 定義句子，其他就沒了
正常上除了你的 python 小於 3.6，不然都一律推 f-string
