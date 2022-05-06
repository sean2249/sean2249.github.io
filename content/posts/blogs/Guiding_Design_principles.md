---
title: "Guiding Design principles"
date: 2022-05-06T16:56:29+08:00
draft: false
categories:
- linkPage
tags:
- python
summary: "tags: python"
---

https://nsls-ii.github.io/scientific-python-cookiecutter/guiding-design-principles.html
- Refactor 是必要的，準備好 Version Control, testing, lint 作為重構的安全網
- io 隔離
- duck typing treats objects based on what they can do, not based on what type they are.
- stop writing class. Class is hard to extend and maintain. Try to use dictionary and numpy.array as input to work within multiple functions
- complexity is always conserved
    - `def func(data, cut=False, copy=False)` -> `def func(data, option={})` would confused people what the key that could satisfy the options. 
    - Bring keyword-argument restriction for function hinting to imporve potential confused about the arguement like Boolean 
    `func(123, False, False)` -> `func(123, cut=False, copy=False)`
- write for readability
