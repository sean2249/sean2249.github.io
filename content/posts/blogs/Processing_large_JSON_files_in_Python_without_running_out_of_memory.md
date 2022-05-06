---
title: "Processing large JSON files in Python without running out of memory"
date: 2022-05-06T17:02:33+08:00
draft: false
categories:
- linkPage
tags:
- python
- json
summary: "tags: python, json"
---

https://pythonspeed.com/articles/json-memory-streaming/

json 載入時
1. 將檔案載入到 memory 
2. Decode bytes 成 unicode string

超過 24MB 以上就會塞爆啦

```python=
>>> import sys
>>> s = "a" * 1000
>>> len(s)
1000
>>> sys.getsizeof(s)
1049

>>> s2 = "❄" + "a" * 999
>>> len(s2)
1000
>>> sys.getsizeof(s2)
2074

>>> s3 = "💵" + "a" * 999
>>> len(s3)
1000
>>> sys.getsizeof(s3)
4076
```

雖然字串長度都一樣，但因為非 ascii 所以佔用的 bytes 會較大


