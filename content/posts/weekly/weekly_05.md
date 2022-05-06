---
title: "weekly 05"
date: 2022-03-11T10:20:09+08:00
draft: false
categories:
- weekly
tags:
summary: 2022/02/27 ~ 2022/03/05; 前端的頁面展現的過程 ; 訂單未成立後的 message queue ; DNS 是什麼
---

- [Link](#link)
  - [Liked](#liked)
    - [[Frontend] 从URL输入到页面展现到底发生什么？](#frontend-从url输入到页面展现到底发生什么)
    - [[Frontend] 从输入URL开始建立前端知识体系](#frontend-从输入url开始建立前端知识体系)
    - [[System structure] 面試官問：生成訂單30分鐘未支付，則自動取消，該怎麼實現？](#system-structure-面試官問生成訂單30分鐘未支付則自動取消該怎麼實現)
    - [[system structure] 一份热乎乎的字节面试真题](#system-structure-一份热乎乎的字节面试真题)
  - [Others](#others)
    - [[Message Queue] RabbitMQ與Kafka選型對比](#message-queue-rabbitmq與kafka選型對比)
    - [[Python] Understanding Attributes, Dicts and Slots in Python](#python-understanding-attributes-dicts-and-slots-in-python)
    - [[Network] 字节面试被虐后，是时候搞懂 DNS 了](#network-字节面试被虐后是时候搞懂-dns-了)
    - [[Design Pattern] Decorator 裝飾者模式](#design-pattern-decorator-裝飾者模式)

# Link
## Liked
### [Frontend] 从URL输入到页面展现到底发生什么？
https://juejin.cn/post/6844903784229896199

主要是前端 rendering 的部份

想要知道瀏覽器到底做了什麼 ლ(╹◡╹ლ)

### [Frontend] 从输入URL开始建立前端知识体系

https://juejin.cn/post/6935232082482298911

上面是科普等級的，這則連結就是教學文了


### [System structure] 面試官問：生成訂單30分鐘未支付，則自動取消，該怎麼實現？
https://juejin.cn/post/7068837416714371102

關於延時任務，要如何去實作

- 程式裡面，時間環
- redis
- rabbitMQ 延時隊列


```
b'' -> b'{}'
```


### [system structure] 一份热乎乎的字节面试真题

https://juejin.cn/post/7064357766294405128#heading-29

裡面好多種面試題目，特別是短時間巨大流量的情境題，像是演唱會門票之類的

## Others

### [Message Queue] RabbitMQ與Kafka選型對比

https://iter01.com/534319.html

暴力的理解
RabbitMQ 小專案
Kafka 大專案

### [Python] Understanding Attributes, Dicts and Slots in Python

https://bas.codes/posts/python-dict-slots

**預備知識**

class attribute/instance attribute 跟 `__dict__` 的關聯

- class attribute 在 class 的 `__dict_-` 裡面
- instance attribute 在 class 實體化後 instance 裡的 `__dict__` 內
- class attribute 是被每個 instance 共享

下面就是將 instance attribute 與 class attribute 連動在一起

```python=
class Borg:
    _shared = {}
    def __init__(self):
        self.__dict__ = self._shared
```

可以 read/set instance attribute 來改變 class attribute

而且我們可以讀取 `<instance>.value` 來取得 instance 的 `__dict__` 的值，但反過來如果是 `<class>.value` 就不行

```python=
>>> borg_1 = Borg()
>>> borg_2 = Borg()
>>> 
>>> borg_1.value = 42
>>> borg_2.value 
42
```

文章最後是提到 attribute 的記憶體使用量

利用 `__slots__` 來 overwrite `__dict__` 的預設

因為是使用 `__dict__` 的 dictionary，會佔較大的記憶體空間，所以蓋掉用比較小的 data type，或許可以協助釋放更多空間


### [Network] 字节面试被虐后，是时候搞懂 DNS 了

https://juejin.cn/post/6990344840181940261

dns 的遞迴查詢與迭代查詢

### [Design Pattern] Decorator 裝飾者模式

https://ithelp.ithome.com.tw/articles/10218692

Decorator / Chain of Responsibility / Strategy / Composite 如何區分
