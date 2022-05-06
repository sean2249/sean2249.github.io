---
title: "Regular expression 取出"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- re
summary: "tags: re"
---

```python=
import re

match = re.match(r'[name|id]: [0-9]{1,5}', text)
if not match:
    print('no match')
else:
    end = match.span()[1]
    
```

