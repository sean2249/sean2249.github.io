---
title: "psycopg2 where in statement parameters"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- python
- postgresql
summary: "tags: python, postgresql"
---
https://stackoverflow.com/questions/28117576/python-psycopg2-where-in-statement

```python=
data = ('UK', 'France')

sql = 'SELECT * FROM countries WHERE country in %s'
cur.execute(sql, (data,))
```

1. 使用 tuple 來傳遞 parameters
2. 使用 `in %s` 不能用括號 `in (%s)` ，系統會以為 `(('UK', 'France'),)`
