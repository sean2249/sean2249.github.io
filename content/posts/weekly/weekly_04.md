---
title: "weekly 04"
date: 2022-03-02T19:24:34+08:00
draft: false
categories:
- weekly
tags:
summary: 2022/02/20 ~ 2022/02/26; 只 git add 部份的 file changed/軟體工程師的閱讀書單/kubernetes 的元件簡易介紹/Reverse emoji in python is not what u think
---

這周把電腦的所有 tab 清空!!!! 

- [Link](#link)
  - [Good](#good)
    - [[git] Commit only part of a file in git](#git-commit-only-part-of-a-file-in-git)
    - [[python] Which string formatting method should you use](#python-which-string-formatting-method-should-you-use)
      - [1. 使用 %](#1-使用-)
      - [2. 使用 format](#2-使用-format)
      - [3. 使用 f-string](#3-使用-f-string)
      - [4. 使用 Template (極少見)](#4-使用-template-極少見)
    - [[FastAPI] 官方提供的 fastapi 專案架構](#fastapi-官方提供的-fastapi-專案架構)
    - [[software] Software Engineer roadmap via books](#software-software-engineer-roadmap-via-books)
      - [1. 心法](#1-心法)
      - [2. 基礎](#2-基礎)
      - [3. 進階](#3-進階)
      - [4. 反覆閱讀](#4-反覆閱讀)
    - [[Pytest] Useful pytest command line options](#pytest-useful-pytest-command-line-options)
    - [[python class] Provide Multiple Constructors in Your Python Classes](#python-class-provide-multiple-constructors-in-your-python-classes)
    - [[kubernetes] A guide to Kubernetes architecture](#kubernetes-a-guide-to-kubernetes-architecture)
    - [[python string,encoding] Why Can’t You Reverse a String With a Flag Emoji?](#python-stringencoding-why-cant-you-reverse-a-string-with-a-flag-emoji)
  - [Others](#others)
    - [[python] What does '# noqa' mean in Python comments](#python-what-does--noqa-mean-in-python-comments)
    - [[mock,testing] Mocking a class used in a with statement](#mocktesting-mocking-a-class-used-in-a-with-statement)
    - [[python,postgresql] psycopg2 where in statement parameters](#pythonpostgresql-psycopg2-where-in-statement-parameters)
    - [[kubernetes,cgroups] 第一千零一篇的 cgroups 介紹](#kubernetescgroups-第一千零一篇的-cgroups-介紹)
    - [[FastAPI,backend] events: startup - shutdown](#fastapibackend-events-startup---shutdown)
    - [[FastAPI,backend,python] Request body + path + query parameters](#fastapibackendpython-request-body--path--query-parameters)
    - [[FastAPI] `Body` with multiple `examples`](#fastapi-body-with-multiple-examples)
    - [[FastAPI,middleware] middleware](#fastapimiddleware-middleware)
    - [[design pattern] Wiki 上面的 design pattern](#design-pattern-wiki-上面的-design-pattern)
    - [[system structure] UML](#system-structure-uml)
    - [[psycopg2] Sqlstate exception classes](#psycopg2-sqlstate-exception-classes)
    - [[re] Regular expression 取出](#re-regular-expression-取出)
    - [[Mock] setting return values and attributes](#mock-setting-return-values-and-attributes)
      - [set function return value](#set-function-return-value)
      - [Set module return value](#set-module-return-value)
      - [set attribute value](#set-attribute-value)
      - [use class instance](#use-class-instance)
    - [[FastAPI] Additional responses in OpenAPI](#fastapi-additional-responses-in-openapi)

# Link
## Good
### [git] Commit only part of a file in git 
https://stackoverflow.com/questions/1085162/commit-only-part-of-a-file-in-git

`git add` 預設會將檔案有修改的地方都加入到 staging area，但有時會想分開成兩個 commit 上傳，或是針對另一個修改的地方做回復

`git add --patch <filename>` 可以讓 git 針對每一塊修改的地方，讓你選擇要作為 commit 還是放棄作為 commit

而這篇就是在說明選項的全名是什麼XDDD 因為 git 裡面寫的是縮寫


### [python] Which string formatting method should you use
https://realpython.com/python-string-formatting/#which-string-formatting-method-should-you-use

python string format 有四種
#### 1. 使用 %
從 C 的 prinft 導入過來的
```python=
>>> name = 'bob'
>>> 'hello %s' % name
hello bob
```

#### 2. 使用 format
這應該是 python3.5 前很常用的方法，不過很慢
```python=
>>> name = 'bob'
>>> 'hello {}'.format(name)
hello bob
```

#### 3. 使用 f-string
python3.6 導入，唯一推薦
```python=
>>> name = 'bob'
>>> f'hello {name}'
hello bob
```

#### 4. 使用 Template (極少見)
需要額外 import 
```python=
>>> from string import Template
>>> t = Template('hello $name')
>>> t.substitue(name=name)
hello bob
```

整體速度，印象中是 f-string > % > format > Template
Template 的好處在於可以給 user 定義句子，其他就沒了
正常上除了你的 python 小於 3.6，不然都一律推 f-string

### [FastAPI] 官方提供的 fastapi 專案架構
https://github.com/tiangolo/full-stack-fastapi-postgresql

包含了前端 Vue，後端 Fastapi，Database Postgres


### [software] Software Engineer roadmap via books
https://medium.com/@iamjwr/software-engineer-roadmap-via-books-a6aabdc2589c

#### 1. 心法
1. The Passionate Programmer
2. Building a career in software

#### 2. 基礎
- Elements of Computing Systems
- You Don’t Know JS

#### 3. 進階
- Grokking Algorithms
- Design Patterns
- Test-Driven Development by Example 
- Clean Code

#### 4. 反覆閱讀
- Explain the Cloud Like I’m 10
- System Design Interview
- Designing Data-Intensive Applications 
- Domain-Driven Development Distilled 

### [Pytest] Useful pytest command line options
https://www.thedigitalcatonline.com/blog/2018/07/05/useful-pytest-command-line-options/

主要是介紹 pytest skip 的功能


簡單的 skip，只要加上 decorator 即可
```python=
@pytest.mark.skip
def test_a():
    ...
```

加入 reason，使 pytest 運行到此 test 會多印些資訊
```python=
@pytest.mark.skip(reason='I want to skip')
def test_b():
    ...
```

加入條件判斷
```python=
@pytest.mark.skipif(os.environ['AWS_REGION'] == 'us-west-2', reason='I want to skip')
def test_b():
    ...
```

標籤 test，可指定要跑跟不跑的
```python=
@pytest.mark.slow
def test_slow():
    ...
```

下面指令會只運行有標註為 `slow` 的 test
```shell=
$ pytest -m slow
```

或是你不想運行 slow 
```shell=
$ pytest -m 'not slow'
```

或是更華麗的，slow or fast 都跑
```shell=
$ pytest -m 'slow or fast'
```

上面都是針對 test function 來做，下面則是不同的方式 skip


跑到一半 skip
```python=
def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")
```

載入 module 時，skip 整個 module
```python=
import sys
import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)
```

### [python class] Provide Multiple Constructors in Your Python Classes
https://realpython.com/python-multiple-constructors/

- `__new__` object creation
- `__init__` object initialization
- python 沒有直接支援 overloading (文中有寫原因)

[Python function overloading](https://stackoverflow.com/questions/6434482/python-function-overloading): 利用 module::multipledispatch 來實現

- `__call__` 在實體化的直接呼叫

```python=
>>> class Person:
...     def __init__(self, name):
...         self.name = name
...         
...     def __call(self):
...         print(f"I'm {self.name}")

>>> person = Person('kiwi')
>>> person()
I'm kiwi
```

文章接下來都是 classmethod 的介紹，可以參考一下，更可順便跟 staticmethod 做個比較

[`dict.fromkeys(iterable)`](https://docs.python.org/dev/library/stdtypes.html?highlight=strip#dict.fromkeys) !! 在已知 key 的時候可以先設定 default value 產出新的 dictionary


```python=
>>> names = ['Alice', 'Bob', 'Cindy']
>>> bank_accounts = dict.fromkeys(names, 0)
>>> bank_accounts
{'Alice': 0, 'Bob': 0, 'Cindy': 0}
```

還有其他 classmethod 在基本的 datatype，像是 int, float 


datetime 也是一堆 classmethod
```python=
>>> from datetime import date
>>> from time import time

>>> # Standard constructor
>>> date(2022, 1, 13)
datetime.date(2022, 1, 13)

>>> date.today()
datetime.date(2022, 1, 13)

>>> date.fromtimestamp(1642110000)
datetime.date(2022, 1, 13)
>>> date.fromtimestamp(time())
datetime.date(2022, 1, 13)

>>> date.fromordinal(738168)
datetime.date(2022, 1, 13)

>>> date.fromisoformat("2022-01-13")
datetime.date(2022, 1, 13)
```

看到了一個新潮的玩意兒: 在 python3.8 後，新增了 `@singledispatch` / `@singledispatchmethod` 在 functools

感覺實現了 overloading 

```python=
# demo.py

from functools import singledispatchmethod

class DemoClass:
    @singledispatchmethod
    def generic_method(self, arg):
        print(f"Do something with argument of type: {type(arg).__name__}")

    @generic_method.register
    def _(self, arg: int):
        print("Implementation for an int argument...")

    @generic_method.register(str)
    def _(self, arg):
        print("Implementation for a str argument...")
```

利用 `@singledispatchmethod` 做登記，代表此 method 是 default。接下來在用這個 method 當做 decorator 去 register 不同 argument type 的 method，當作 overloading

你可以直接標注格式在 register 內，或是用 type annotation

呼叫的感覺是
```python=
>>> from demo import DemoClass

>>> demo = DemoClass()

>>> demo.generic_method(42)
Implementation for an int argument...

>>> demo.generic_method("Hello, World!")
Implementation for a str argument...

>>> demo.generic_method([1, 2, 3])
Do something with argument of type: list
```


Conclusion from website
- Simulate multiple constructors using optional arguments and type checking
- Write multiple constructors using the built-in @classmethod decorator
- Overload your class constructors using the @singledispatchmethod decorator

### [kubernetes] A guide to Kubernetes architecture
https://opensource.com/article/22/2/kubernetes-architecture?utm_medium=Email&utm_campaign=weekly&sc_cid=7013a000002qKBKAA2

介紹 kubernetes 元件的架構，從中可以理解其核心，散落的 node，及如何優化調較對的方向

如果我一開始能看到這篇就省了很多路了，不過也有可能走了那些路，我才看得懂這篇 ヽ(✿ﾟ▽ﾟ)ノ

### [python string,encoding] Why Can’t You Reverse a String With a Flag Emoji?
https://davidamos.dev/why-cant-you-reverse-a-flag-emoji/

從 "🇺🇸"[::-1] 的結果，反推到 unicode 在 python 的實作

```python=
>>> "🇺🇸"[::-1]
🇸🇺
```

從上面的例子可發現 us flag 不是你想像中的單一字元，而是兩個字元合在一起。

接下來我們嘗試用 encode 的方式得到原生的 unicode，來避掉可能是不同編碼方式的錯誤 (ascii, utf-8, big5)

```python
>>> list("🇺🇸".encode())
[240, 159, 135, 186, 240, 159, 135, 184]
>>> # ^^^^^^^^^^^^^^---Code point for 🇺
>>> #                ^^^^^^^^^^^^^^^^^^---Code point for 🇸

>>> # The code points get swapped!
>>> list("🇺🇸"[::-1].encode())
[240, 159, 135, 184, 240, 159, 135, 186]
>>> # ^^^^^^^^^^^^^^---Code point for 🇸
>>> #                ^^^^^^^^^^^^^^^^^^---Code point for 🇺
```

成功的 encode 了，發現 us flag 總共分出了八個字元，四個為一組，才組成了 :us:。而在 reverse 中，是以一組為單位做 reverse，因此才導致 us -> su，而此 su 沒有辦法解析成 emoji 的格式，所以才跑出原生的兩個字

同理與中文字相同，中文的每個字也是多個字元為一組，但因為沒有像 emoji 一樣另外再轉一層查詢做圖片，所以才沒遇問題。

最後附上文中作者的整理
- Strings of symbols get converted to sequences of integers by a character encoding, usually UTF-8.
- Some characters are encoded as a single 8-bit integer by UTF-8, and others require two, three, or four 8-bit integers.
- Some symbols, such as flag emojis, are not directly encoded by Unicode. Instead, they are renders of sequences of Unicode characters and may or may not be supported by every platform.

內文還有講到更多 bits 的


## Others

### [python] What does '# noqa' mean in Python comments 
https://stackoverflow.com/questions/45346575/what-does-noqa-mean-in-python-comments

noqa = NO-QA -> no quality assurance

linter 不會檢查這行 code 喔~ 像是 flake8

### [mock,testing] Mocking a class used in a with statement
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

### [python,postgresql] psycopg2 where in statement parameters
https://stackoverflow.com/questions/28117576/python-psycopg2-where-in-statement

```python=
data = ('UK', 'France')

sql = 'SELECT * FROM countries WHERE country in %s'
cur.execute(sql, (data,))
```

1. 使用 tuple 來傳遞 parameters
2. 使用 `in %s` 不能用括號 `in (%s)` ，系統會以為 `(('UK', 'France'),)`

### [kubernetes,cgroups] 第一千零一篇的 cgroups 介紹
https://medium.com/starbugs/%E7%AC%AC%E4%B8%80%E5%8D%83%E9%9B%B6%E4%B8%80%E7%AF%87%E7%9A%84-cgroups-%E4%BB%8B%E7%B4%B9-a1c5005be88c

對這個沒有很熟，但稍微強迫自己吸收點 (但下面就看不太懂了 ٩(ŏ﹏ŏ、)۶
- 可限制控制隔離 process 所使用到的系統資源，例如 CPU, memory, Disk I/O, Network...等
- Resource limiting, Prioritization, Accounting, Control
- 2006 process containers -> 2007 cgroups v1 -> 2016 cgroups v2
- cgroups 沒有 API/library 的操作方式，是透過 Linux Virtual File System 實作，可像檔案系統一樣，透過新增修改刪除資料夾檔案來設定
- 請使用 systemd unit 來管理 cgroup，身為 linux distribution 預設的系統管理服務，也是大家熟悉習慣的，請使用它! 


### [FastAPI,backend] events: startup - shutdown
https://fastapi.tiangolo.com/advanced/events/

```python=
@app.on_event('startup')
async def startup_event():
    ...
```
在 application 正式運行前執行 (可以多個 startup event，requests 會等全部的 startup event 結束後才會開始接收)，像是連接 database 產生初始資料

```python=
@app.on_event('shutdown')
def shutdown_event():
    with open('log.txt', mode='a') as log:
        log.write('Application shutdown')
```
在 application 被關閉後，可以做點像是清理 cache 或寫入紀錄。  
上面的例子，是將關閉資訊寫入檔案，利用 `open()` 不支援 async/await，所有是使用 `def` 而不是 `async def`

### [FastAPI,backend,python] Request body + path + query parameters
https://fastapi.tiangolo.com/tutorial/body/#request-body-path-query-parameters

```python=
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

- `{item_id}` 是 path parameter
- `q` query parameter (singular type)
- `item` 則是 pydantic model -> request body

https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter
-> 使用 `Body` 來更完善 request body 的要求及 openapi 的 spec，像是 example

```python=
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
```
多加入 `embed=True`
```json=
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```
-> 變成需要額外加入 `item` 作為 key
```json=
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

### [FastAPI] `Body` with multiple `examples`
https://fastapi.tiangolo.com/tutorial/schema-extra-example/#body-with-multiple-examples

fastapi 的 example 讓你可以在 swagger 上面，有些預設的 request body/parameter 可以選擇及參考~ 很方便

這邊講的 examples 不是單純指 body，還可以用在
- Path()
- Query()
- Header()
- Cookie()
- Body()
- Form()
- File()

單一的 example: `example=<你想要呈現的例子>` 
```python=
@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
```

多個 examples，你可以定義更多的資訊，甚至還有下拉選單!!
- summary: 下拉選單的選項名稱
- description: 更詳細的描述，支援 markdown
- value: 要當作 example 的值
- externalValues: alternative to value, a URL pointing to the example. Although this might not be supported by as many tools as value.

```python=
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
```

### [FastAPI,middleware] middleware
https://fastapi.tiangolo.com/tutorial/middleware/

你可以客製自己的 middleware 

```python=
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

```


### [design pattern] Wiki 上面的 design pattern
https://en.wikipedia.org/wiki/Software_design_pattern#Classification_and_list

發現 wiki 上面的還蠻完整的椰

### [system structure] UML
https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E5%BB%BA%E6%A8%A1%E8%AF%AD%E8%A8%80

描述軟體專案架構

- class diagram https://zh.wikipedia.org/wiki/%E9%A1%9E%E5%88%A5%E5%9C%96
- sequence diagram https://zh.wikipedia.org/wiki/%E6%97%B6%E5%BA%8F%E5%9B%BE
- use case diagram https://zh.wikipedia.org/wiki/%E7%94%A8%E4%BE%8B%E5%9B%BE

### [psycopg2] Sqlstate exception classes
https://www.psycopg.org/docs/errors.html#sqlstate-exception-classes

### [re] Regular expression 取出

```python=
import re

match = re.match(r'[name|id]: [0-9]{1,5}', text)
if not match:
    print('no match')
else:
    end = match.span()[1]
    
```


### [Mock] setting return values and attributes
#### set function return value
```python=
>>> mock = Mock()
>>>mock.return_value = 5
>>> mock()
5
```

#### Set module return value
```python=
>>> mock = Mock()
>>> mock.method.return_value = 5
>>> mock.method()
5
```

#### set attribute value
```python=
>>> mock = Mock()
>>> mock.x = 5
>>> mock.x
5
```

#### use class instance

1. 實體化
```python=
>>> mock = Mock()
>>> cursor = mock.connect.cursor.return_value
```

```python=
cursor = connect.cursor()
```

2. 針對實體化的物件
```python=
>>> mock = Mock()
>>> cursor = mock.connect.cursor.return_value
>>> cursor.execute.return_value = ['foo']
>>> cursor.rowcount = 3
```

```python=
>>> cursor = connect.cursor()
>>> cursor.execute('select 1')
['foo']
>>> cursor.rowcount
3
```

### [FastAPI] Additional responses in OpenAPI 
https://fastapi.tiangolo.com/advanced/additional-responses/

```python=
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


app = FastAPI()


@app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
```

`@app.get(..., responses)` 定義 model 時，可以利用 content 的 keyword parameter 來塞入 pydantic model 作為輸出的格式，同時也會顯示在 openapi swagger 上面。

如果不想要那麼麻煩，就寫個 description 來描述該狀態的錯誤 

> 至於 httpexceptions / jsonresponse 不知道有什麼差別 QQ 可能一個是用 raise?
> 