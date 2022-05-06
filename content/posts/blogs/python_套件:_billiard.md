---
title: "python 套件: billiard"
date: 2022-05-06T16:56:29+08:00
draft: false
categories:
- linkPage
tags:
- python module
summary: "tags: python module"
---
https://github.com/celery/billiard

若要在 python 上面進行多核心加速，需使用多進程才有辦法做到，常用的一個工具是 multiprocessing 套件，但 multiprocessing 目前在 airflow 上面會有相容性的問題，且 multiprocessing 沒有提供 callback function，供開發者指定一個 process 要停止前可以做的事情 (e.g., 關閉 db connection)。根據 stackoverflow 上面的建議就是使用一個multiprocessing 的延伸工具 - billiard。
