---
title: "Mocking a class used in a with statement"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- mock
- testing
summary: "tags: mock, testing"
---
https://stackoverflow.com/questions/54634817/mocking-a-class-used-in-a-with-statement

```python=
with conn.cursor() as cursor:
    cursor.execute('select 1')
    if not cursor.rowcount:
        raise ValueError('No object found')
    result = cursor.fetchone()
```

第一個 return_value 取出 `conn.cursor()` 的回傳
第二個 return_value 則是 with statement 的內建函數 `__enter__` 裡的回傳項 `def __enter__(self)`
```python=
mock = Mock()
mock_cursor = mock.conn.cursor.return_value.__enter__.return_value
mock_cursor.rowcount = 1
mock_cursor.fetchone = ('a',)
```
