---
title: "Strict python function parameters"
date: 2022-05-06T16:56:29+08:00
draft: false
categories:
- linkPage
tags:
- python
summary: "tags: python"
---
https://sethmlarson.dev/blog/strict-python-function-parameters

強制性的 function parameters 輸入，之前只有 keyword-arguemnt 的強制，但在 python3.8 後，引入了 positional-argument 的強制 `def process_data(data, /, *, encoding='utf-8')` 裡面的 `/` 代表之前的 argument 都必須用 positional 的方式塞入，並且還要符合順序．當然還是可以用 keyword-argument 混用

```python
def process_data(data1, data2, /, data3)
# OK: process_data(1, 2, data3=3)
# no: process_data(1, data2=2, data3=3)

def process_data(data1, data2, /, data3, *, data4=4)
# OK: process_data(1, 2, data3=3)
# no: process_data(1, data2=2, data3=3)
# ok: process_data(1, 2, data3=3)
# ok: process_data(1, 2, 3, data4=4)
# no: process_data(1, 2, 3, 4)
```
