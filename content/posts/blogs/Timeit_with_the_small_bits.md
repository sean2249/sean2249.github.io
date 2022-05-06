---
title: "Timeit with the small bits"
date: 2022-05-06T16:56:30+08:00
draft: false
categories:
- linkPage
tags:
- python
summary: "tags: python"
---
```python=
'"-".join(str(n) for n in range(100))
```
0.341266

```python=
'"-".join([str(n) for n in range(100)])
```
o.29963

```python=
'"-".join(map(str, range(100)))', number=10000 
```
0.245814
