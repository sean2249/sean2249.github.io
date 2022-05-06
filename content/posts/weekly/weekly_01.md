---
title: "weekly 01"
date: 2022-02-05T15:34:29+08:00
draft: false
summary: 2022/01/24 ~ 2022/01/30
categories:
- weekly
tags:
---

- [website reading](#website-reading)
  - [推薦](#推薦)
    - [[python] Strict python function parameters](#python-strict-python-function-parameters)
    - [[sre] 沒技術系列 — 如何成為一個好的 SRE 工具人](#sre-沒技術系列--如何成為一個好的-sre-工具人)
    - [[system structure] How to scale your web and mobile applications](#system-structure-how-to-scale-your-web-and-mobile-applications)
    - [[system structure] Microservices database management patterns and principles](#system-structure-microservices-database-management-patterns-and-principles)
  - [Others](#others)
    - [[development] 隕石開發](#development-隕石開發)
    - [[python module] python 套件: pipdeptree](#python-module-python-套件-pipdeptree)
    - [[python module] python 套件: billiard](#python-module-python-套件-billiard)
    - [[python] Guiding Design principles](#python-guiding-design-principles)
    - [[docker, minikube] Goodbye docker desktop, hello minikube!](#docker-minikube-goodbye-docker-desktop-hello-minikube)
    - [[docker, moby]【從Docker到Moby】Docker如何將容器平臺變成一門好生意？](#docker-moby從docker到mobydocker如何將容器平臺變成一門好生意)
    - [[moby] MoBy开源项目集](#moby-moby开源项目集)
    - [[web3] The False Promise of Web3](#web3-the-false-promise-of-web3)

# website reading
## 推薦
### [python] Strict python function parameters
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

### [sre] 沒技術系列 — 如何成為一個好的 SRE 工具人
https://medium.com/starbugs/%E6%B2%92%E6%8A%80%E8%A1%93%E7%B3%BB%E5%88%97-%E5%A6%82%E4%BD%95%E6%88%90%E7%82%BA%E4%B8%80%E5%80%8B%E5%A5%BD%E7%9A%84-sre-%E5%B7%A5%E5%85%B7%E4%BA%BA-1d4d20fcadb

- 要不要使用 open source 做為系統而衍生的問題，像是 open source 的社群是否活躍使得未來有 bug 能否快被快速修復
- 選擇 open source
    - Community is good?
    - Paid 

### [system structure] How to scale your web and mobile applications
https://enlear.academy/how-to-scale-your-web-and-mobile-applications-5be74bf99226

- 從最簡單的 web app，因應服務人數的升級及 SLA 的要求，不斷的調整架構
1. Basic design for a web app
    - single app server
    - Database
3. Scaling the app servers: requests to the application server grow. Need for leveling up the CPU capacity.
    - Load balancers for multiple app server
    - Session store: memcached/redis
1. Scaling the database with caching: database crisis for incread requests. store most requested data in the distributed cache system
    - distributed cache system to support database
1. Distributing the database: caching is not enough to reduce the volume of work on your databse -> horional scaling (stored across multiple DB instances)
    - Distributed database system
1. Increasing RESPONSIVENESS: Some mission takes lots of time, and cannot response in time.
    - queuing system

1. we started from the design of a simple Web app
2. we increased the compute capacity by adding more instances and a load balancer
3. we relieved our DB from the extra load by leveraging the caching system
4. we scaled out DB, turning it into a distributed database system
5. we improved the responsiveness of our application using a queuing system

### [system structure] Microservices database management patterns and principles
https://medium.com/design-microservices-architecture-with-patterns/microservices-database-management-patterns-and-principles-9121e25619f1

- Shifting to the monolithic architecture to microservices architecture
- hybrid database selection:
    - catalog: MongoDB
    - Shopping cart: redis
    - Ordering: SQL server
- when interact or sharing data between microservices -> you cant use ACID transactions between distributed systems. That means its challenging to implemnt queries and trasactions that visits to serverl microservices
- Patterns
    - The Database-per-Service pattern 
        - loose coupling of services
        - Provide to evole rapidly and easy to scale applications
        - Each microservices use different database (sql,no-sql,key-value) conected by message broker
    - The API Composition pattern
        - Gateway routing pattern
        - gateway aggregation pattern
        - gateway offloading pattern
    - The CQRS(Command Query Responsibility Segregation) pattern 
        - separate commands(Write) and queires(Read) in order to better perform querying several microservices
    - The Event Sourcing pattern 
        - provide to accumulate events and aggregates them into sequence of events in databses 
    - The Saga pattern 
    - The Shared Database anti-pattern
        - Dont use single databse across microservices
        - Might block microservices due to single-point-of-failure

## Others
### [development] 隕石開發
https://ithelp.ithome.com.tw/articles/10198394

隕石開發，神說什麼就是什麼，神說的就是準則，就是要達到

### [python module] python 套件: pipdeptree
https://github.com/naiquevin/pipdeptree

整理 pip list，將相關的 dependency 縮減，優化 requirements.txt 的閱讀。當然還是推薦用 poetry

### [python module] python 套件: billiard
https://github.com/celery/billiard

若要在 python 上面進行多核心加速，需使用多進程才有辦法做到，常用的一個工具是 multiprocessing 套件，但 multiprocessing 目前在 airflow 上面會有相容性的問題，且 multiprocessing 沒有提供 callback function，供開發者指定一個 process 要停止前可以做的事情 (e.g., 關閉 db connection)。根據 stackoverflow 上面的建議就是使用一個multiprocessing 的延伸工具 - billiard。

### [python] Guiding Design principles

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

### [docker, minikube] Goodbye docker desktop, hello minikube!
https://itnext.io/goodbye-docker-desktop-hello-minikube-3649f2a1c469

hyperkit for macos: toolkit for embedding hypervisor capabilities in your application.

macos 不使用 docker 做為基底，改用 hyperkit 來減輕負擔，以使用 minikube

### [docker, moby]【從Docker到Moby】Docker如何將容器平臺變成一門好生意？
https://www.ithome.com.tw/news/113899

docker -> moby open source project 

### [moby] MoBy开源项目集
https://cloud-atlas.readthedocs.io/zh_CN/latest/docker/moby/introduce_moby.html

- core of docker.
- for the dev
- Hacker 可以自己定制或 patch 自己的 Docker build 
- 系统工程师可以构建一个容器系统
- 架构师可以查看和修改现有的容器系统以适应自己的环境
- 容器爱好者可以实验最新的容器技术
- 开源开发这可以在不同平台查看和测试自己的项目

### [web3] The False Promise of Web3
https://marker.medium.com/the-false-promise-of-web3-7e6c1a00d4be

- web3 is a decentralized version of the internet where platforms and apps are built and owned by users.
- Blockcahin, crypto, NFTs to transfer power back to the internet community
- the infrasctructure of web3 relied on "decentrailized". The truth is, people dont want to run their own servers.

