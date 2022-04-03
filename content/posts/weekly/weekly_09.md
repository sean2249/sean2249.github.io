---
title: "Weekly 09"
date: 2022-04-03T14:33:27+08:00
draft: false
categories:
- weekly
tags:
- dev environment
- software engineer
- interview
- python 
- json
- go
summary: "2022/03/27~2022/04/02"
---

- [Link](#link)
  - [Good](#good)
    - [[Dev environment] macOS Tools and Apps for Development in 2022](#dev-environment-macos-tools-and-apps-for-development-in-2022)
    - [[software engineer] 入职一个月我和腾讯大佬都学到了什么](#software-engineer-入职一个月我和腾讯大佬都学到了什么)
    - [[Software engineer,interview] 2022最新：5千字有答案的后端面试题](#software-engineerinterview-2022最新5千字有答案的后端面试题)
    - [[python,json] Processing large JSON files in Python without running out of memory](#pythonjson-processing-large-json-files-in-python-without-running-out-of-memory)
  - [Others](#others)
    - [[go] 1 min guide to Golang development best practices in 2022](#go-1-min-guide-to-golang-development-best-practices-in-2022)


# Link
## Good
### [Dev environment] macOS Tools and Apps for Development in 2022

https://medium.com/@etc088/macos-tools-and-apps-for-development-in-2022-963bd4d0f876

fig Nice!

### [software engineer] 入职一个月我和腾讯大佬都学到了什么


https://juejin.cn/post/6967899063027138590

> 真正区分程序员好坏的不只是对编程语言（工具）的熟悉程度，更多的是设计思想、和业务的契合程度、可扩展性、是否真的考虑到了问题所在。

1. 定義好資料庫結構
2. 量力而行
3. 找到問題關鍵: 拿到需求後，盡可能的抽象，把核心業務梳理出來。前期不會嚴格按照產品規格去寫程式，而是根據核心需求把業務邏輯層的程式碼抽取出來，盡量解耦，然後再梳理產品原型，根據原型去寫接口，使用或者引用他抽象好的業務邏輯層的程式
4. 大膽嘗試，不怕放錯: 若一直使用自己熟悉的技術點，大概率是故步自封，難以進步。沒有誰是的權威的問題，大膽嘗試，不斷在推進項目的過程中優化業務邏輯

### [Software engineer,interview] 2022最新：5千字有答案的后端面试题

https://juejin.cn/post/7076651570993037326

blocking / synchronization
static website
sql

### [python,json] Processing large JSON files in Python without running out of memory

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


## Others
### [go] 1 min guide to Golang development best practices in 2022

https://blog.canopas.com/1-min-guide-to-golang-development-best-practices-in-2022-b50d846fd6c

> copy from StarBugs

使用一分鐘快速了解 Golang 的 Best Practice 🏃🏻 這篇文章想帶讀者用最短的時間快速了解必要的函示庫和重要提示，讓 Golang 開發者天天擁有高效率與簡易的開發人生

- 熟悉如何使用 Go Modules 來管理 Golang 套件相依性
- 使用 Gin 來構建 Web API
- 建立妥適的 Git Repoisotry 結構
- 利用 SQLX 來完成資料庫查詢作業
- 一定要在 API 加上認證機制
- 使用 Microservices 的概念來撰寫 API 功能
- 輸入良好的 Log 來追蹤錯誤或是臭蟲，例如 Zap, Logrus
- 使用 HttpTest 和 asset 來做測試
- 使用 Redigo 來處理跟 Redis 的連線
- 利用 CI/CD 來自動化開發流程
- 讓 pre-commit hooks 幫助省下 commit 前要花費的時間

最近要來學 golang 了啊

