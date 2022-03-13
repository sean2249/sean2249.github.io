---
title: "Weekly_02"
date: 2022-02-22T15:12:07+08:00
draft: false
tags:
- weekly
categories:
- weekly
summary: 2022/01/30 ~ 2022/02/12。 街口 api 的測試 / github 開源專案參與
---

- [Website](#website)
  - [Good](#good)
    - [街口支付 API 自動化測試解決方案](#街口支付-api-自動化測試解決方案)
      - [自動化測試程式架構的元件](#自動化測試程式架構的元件)
      - [一些](#一些)
      - [API](#api)
    - [Timeit with the small bits](#timeit-with-the-small-bits)
    - [Why you shuld use a developer font](#why-you-shuld-use-a-developer-font)
    - [Factory method python](#factory-method-python)
    - [What happens when you type in a url in an address bar in a brow](#what-happens-when-you-type-in-a-url-in-an-address-bar-in-a-brow)
    - [別猶豫了，今天就上 Github 參與開源專案吧！](#別猶豫了今天就上-github-參與開源專案吧)
    - [Kubernetes jobs market trends for 2021](#kubernetes-jobs-market-trends-for-2021)
      - [General](#general)
      - [Skill Tool](#skill-tool)
    - [『紅帽』的 Cloud-Native 工作術: 從 Container 到 OpenShift](#紅帽的-cloud-native-工作術-從-container-到-openshift)
  - [Others](#others)
    - [Allure test report](#allure-test-report)
    - [Reclaiming the lost art of Linux server administration](#reclaiming-the-lost-art-of-linux-server-administration)
      - [前言](#前言)
      - [好處](#好處)
      - [Shell script](#shell-script)
      - [Learning path](#learning-path)
    - [Bash 程式設計教學與範例：Heredoc << 與 <<< 的用法](#bash-程式設計教學與範例heredoc--與--的用法)
    - [How to make money with css](#how-to-make-money-with-css)
    - [Making pixel-art with pure css](#making-pixel-art-with-pure-css)
    - [Retrospective and Technical Details on the recent Firefox Outage](#retrospective-and-technical-details-on-the-recent-firefox-outage)
      - [架構](#架構)
      - [結論](#結論)
    - [How to Contribute to Open Source Projects – A Beginner's Guide](#how-to-contribute-to-open-source-projects--a-beginners-guide)
    - [Podman 淺談 - 為何你應該選擇 Podman 而不是 Docker？](#podman-淺談---為何你應該選擇-podman-而不是-docker)
    - ['is' vs '=='](#is-vs-)
- [Notes](#notes)
  - [Postgres](#postgres)
  - [HyperText Transfer Protocol (HTTP)](#hypertext-transfer-protocol-http)
    - [abstract](#abstract)
    - [Content](#content)
      - [Uniform Resources Identifiers, URI](#uniform-resources-identifiers-uri)
      - [Package](#package)
      - [HTTP Message](#http-message)
      - [Header](#header)
      - [HTTP status code](#http-status-code)
      - [HTTP/2 WIN, WIN](#http2-win-win)
  - [EFK log 的時間](#efk-log-的時間)

# Website
## Good 
### 街口支付 API 自動化測試解決方案
https://medium.com/@dopizz/%E8%A1%97%E5%8F%A3%E6%94%AF%E4%BB%98-api-%E8%87%AA%E5%8B%95%E5%8C%96%E6%B8%AC%E8%A9%A6%E8%A7%A3%E6%B1%BA%E6%96%B9%E6%A1%88-ecf9ec0d0209

> “Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization’s communication structure.”

— Melvin E. Conway, 1967

組織結構會反映在程式架構上

#### 自動化測試程式架構的元件
- test: 測試案例執行的 script
- api: 各 services 的 api 請求介面
- test data: 以特定格式儲存的測試資料
- utility: 封裝各種共用方法以提供調用
- report: 產生測試結果的流程及後續應用

#### 一些
- 將 pytest 的 mark 放在測試資料中而非寫死在 script 
- 透過不同環境的 config 做為相對應環境的 `env.py`
- 封裝連接各個資料庫的方式打包成 class，再開始撰寫 SQL 或是透過 ORM 的方式取得資料表內容，加以驗證測試案例的資料流或是設定測資的前置作業
- 設計 query 時需要保持彈性、盡量抽離業務邏輯

#### API 
在 API 的部分我們將其存在另一個 repository，並且作為 Tests 的 submodule 來使用
-> 希望 API 相關的程式碼能夠獨立運作且跨專案來被調用
讓 api 的 unit test, integration test, UI test 都可以使用部分 api 來輔助測試案例的執行

```
.api (submodule)
├── base_api.py
├── configurations
│   ├── default.py
│   ├── test.py
│   └── ...
├── service-A
│   ├── component_A_api.py
│   ├── component_B_api.py
│   ├── constants.py
│   ├── encode.py
│   └── ...
├── service-B
└── ...
```
**Configurations**
讓 api 能夠獨立使用在其他的環境，將相關的 config 參數都放在這裡面，像是 service 的 domain url，或是預設的 timeout 

**Base API**
所有的 component API 都會繼承此類別
- 執行 api 請求
- timeout 限制處理，提供全域的預設閾值，但各 service 可因應其服務的複雜度來客製
- Allure Report

**Component**

**Enocde/Constants**
`encode.py` 存放該 service 用來執行 encode/hash 所用到的演算法，像是 request body 進行加/解密才能夠運算驗證

`constants.py` 則定義了 service 會用到的 enum/map/dataclass 

### Timeit with the small bits
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

### Why you shuld use a developer font
https://dev.to/anthonyjdella/why-you-should-use-a-developer-font-2gio

說明了使用程式開發者的字體的好處
- 快速找到錯字
- 水平垂直的搜尋
- 可更快速的定位符號

該篇作者推: Jetbrains Mono

### Factory method python
https://realpython.com/factory-method-python/

利用工廠模式來抽離實作的複雜度，讓輸出輸入保持統一的格式，中間的工廠可隨意搭配
- 隱藏複雜的實作細節，增加程式易讀性
- Combining similar features under a common interface

User 只需要知道 serialize 的 function 及其資料的格式
- `serialize`
- `_get_serializer` Creator component, 決定要實做哪個
```python=
class SongSerializer:
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)
```
就算未來需要新增格式，也只需要多加一個 if condition

也可以改寫成
```python=
class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)


def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)
```

- Factory method
- Abstract factory method

或是動態載入的方式，利用 register 來新增產品
```python=
# In object_factory.py

class ObjectFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)
```

要生成的 builder，initial 不會載入，直到 `__call__` 的時候
```python=
class SpotifyServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, spotify_client_key, spotify_client_secret, **_ignored):
        if not self._instance:
            access_code = self.authorize(
                spotify_client_key, spotify_client_secret)
            self._instance = SpotifyService(access_code)
        return self._instance

    def authorize(self, key, secret):
        return 'SPOTIFY_ACCESS_CODE'
```


然後 `register_builder` 來將實作放入此 factory
```python=
factory = object_factory.ObjectFactory()
factory.register_builder('SPOTIFY', SpotifyServiceBuilder())
factory.register_builder('PANDORA', PandoraServiceBuilder())
factory.register_builder('LOCAL', create_local_music_service)
```

### What happens when you type in a url in an address bar in a brow
![flowchart](https://i.imgur.com/Yka8dy7.jpg)
https://www.facebook.com/will.fans/posts/5477204855641947

完整的描述從 client 到 server 的過程啊! 

(不過加入了 k8s，感覺就是個更複雜的世界惹)


### 別猶豫了，今天就上 Github 參與開源專案吧！
https://medium.com/starbugs/start-contributing-to-open-source-projects-today-5daa4dda2b3e

最近新來一個同事，之前碩班常在開源專案打滾，聽了他的介紹，也掀起一個想加入的想法 d(･∀･)b

### Kubernetes jobs market trends for 2021
https://kube.careers/report-2021-q4

> from "StarBugs Weekly"

專注在 kubernetes 在 2021 年的相關職缺資訊，過濾了沒有明確的薪資範圍，從中分析該職務所需的技能與其薪資

#### General
- USD 140k-160k/year 最多
- 工作經歷: senior(4-6y) >> Mid-level (2-3y) > Veteran(7+) = Junior (0-1y), 可能與 k8s 屬於較新的技術，但又需要一定的網路基礎有關吧
- 15% 有提到需要 on-call
- 遠端工作: 混合(Remote+Office) > Office only > Remote only


#### Skill Tool
- 證照要求: AWS -> CKA -> GCP -> Azure -> CKAD
- Configuration Management tools: Terraform > Ansible > Puppet
- monitoring stack (只有 23% 提到): Prometheus >> Datadog > NewRelic (Nagios, Thanos 直接被按在地上磨擦)
- 只有一半有提到需要 docker，該篇作者覺得訝異，甚至說該不會大家都轉去 podman 了吧
- Service mesh (Only 5% mention): lstio >> consul

(統整)非 k8s 的技術要求: AWS > Docker > python > go > Terraform > GCP >Azure >Ansible
- Programming languages: Python, Go, shell, and Java.
- Cloud platforms: AWS, GCP, and Azure (in that order).
- Containers: Docker.
- Infrastructure as Code: Terraform.
- Databases: PostgreSQL, Redis, and MySQL.
- Configuration management: Ansible.
- CI/CD: Jenkins.


### 『紅帽』的 Cloud-Native 工作術: 從 Container 到 OpenShift
https://ithelp.ithome.com.tw/users/20130321/ironman/3566

講得蠻廣的，蠻適合對 docker/k8s 想多點了解的人，重點是搭配上 openshift 的平台納入，可更好的帶入企業上的使用

## Others
### Allure test report
http://blog.autoruby.com/2018/05/allure-test-report.html
Allure Framework is a flexible lightweight multi-language test report tool that not only shows a very concise representation of what have been tested in a neat web report form, but allows everyone participating in the development process to extract maximum of useful information from everyday execution of tests.



### Reclaiming the lost art of Linux server administration
https://www.pietrorea.com/2022/01/28/reclaiming-the-lost-art-of-linux-server-administration

#### 前言
現在過多的 cloud，許多 server 的調整設定，像是防火牆、proxy、DNS 等等都被雲端服務給包裝起來，那現在的 developer 是否還需要學習呢？
還是需要的!!!!

自建 linux VPS, 學習當個 linux admin

#### 好處
- 不會受限在 verdoer
- 因不受限制的關係，你可以只安裝所需的軟體即可，進而降低軟體 OS 的負載
- 就算世界變化很大，底層還是不會變的，像是 bash, ssh, nginx/apache, linx

#### Shell script 
- Good on here document

[Google's shell style Guide](https://google.github.io/styleguide/shellguide.html#s1.1-which-shell-to-use)
> If you are writing a script that is more than 100 lines long, or that uses non-straightforward control flow logic, you should rewrite it in a more structured language now. Bear in mind that scripts grow. Rewrite your script early to avoid a more time-consuming rewrite at a later date.

#### Learning path
1. bash - shell script language
2. Python/swift/ruby/javascript
3. MySQL - database

### Bash 程式設計教學與範例：Heredoc << 與 <<< 的用法 
https://officeguide.cc/bash-tutorial-here-document-string/

Here document command 的使用，可以將多行資料寫入指令的參數

```shell=
cat > output.txt << EOF
line1
line2
line3
EOF
```

### How to make money with css
https://nazanin-ashrafi.hashnode.dev/how-to-make-money-with-css

其實可以適用在蠻多地方的啦，像是寫文章寫書做影片，反正就是分享你所知道而別人不知的。
1. Writing articles.
1. Writing an ebook.
1. Video course.
1. Buy me a coffee.
1. Lucian's idea.
1. Making HTML CSS templates.
1. CSS arts :
    1. Selling stickers
    1. Doing art commissions
    1. NFTs
    
### Making pixel-art with pure css
https://pokecoder.hashnode.dev/making-pixel-art-with-pure-css

運用 `box-shadow` 來創作出 pixel-art，再搭配上 `keyframes` 來做顏色的轉變，真有趣！

不過就如文章所提到的，圖像是一個點一個點的刻劃，真滴麻煩

### Retrospective and Technical Details on the recent Firefox Outage
https://hacks.mozilla.org/2022/02/retrospective-and-technical-details-on-the-recent-firefox-outage/

大概就是講 GCP 偷偷升級衝康到 firefox，使得 load balancer 被改成 http/3 載入，其中影響特別是以 Rust service 為主，因為他是用 http/3 來架構，而其中的 header 屬於 case-sensitive，跟 http/1, http/2 的 case-insensitive 不一樣，導到 firefox 前置的 load balancer 無法正常的將系統導流

#### 架構
![structure](https://hacks.mozilla.org/files/2022/01/foxstuck-diagram4-768x409.png)
1. Necko: content-length
2. viaduct:
3. Rust service: Content-Length

#### 結論
- GCP 偷偷升級，好壞壞，好歹通知下讓我們準備個，或許讓我們可以在 staging enviroment 先測試
- 我們 load balancers 的設定是 Automatic (default)，這導致第三方服務平台升級，改變其 default 導致掛點，因此之後會選擇更明確的設定
- 雖然我們無法測試所有元件的組合，但 http 版未的升級會是非常大的議題，未來會更多加著手研究

### How to Contribute to Open Source Projects – A Beginner's Guide
https://www.freecodecamp.org/news/how-to-contribute-to-open-source-projects-beginners-guide/

寫超多，從如何挑選，到你可以做什麼貢獻，到最後的 community/pr 的介紹。根本是 open source contributor 的完整指南


### Podman 淺談 - 為何你應該選擇 Podman 而不是 Docker？
https://ithelp.ithome.com.tw/articles/10238749

2020 年的文章了，不過跟這週的另一篇在講 kubernetes，主要還是提到 docker。

但說真的 docker 問題多多，看我們公司的 kubernetes 大大也都不推崇，就有提到 podman/runc 都取代了

看這篇來說，大概理解 docker 的架構使其有安全性/SLA 的問題

### 'is' vs '=='

```python=
# "is" vs "=="

>>> a = [1, 2, 3]
>>> b = a

>>> a is b
True
>>> a == b
True

>>> c = list(a)

>>> a == c
True
>>> a is c
False

# • "is" expressions evaluate to True if two 
#   variables point to the same object

# • "==" evaluates to True if the objects 
#   referred to by the variables are equal
```


# Notes
## Postgres
- connection Thread-safe / cursor not thread-safe
- Remember to close connection ? should i keep connection?
- passing parameters to sql queries to prevent potential sql injection
- fetch
    - fetchall: get all data in single operation, might have crush issue when temperaory memory isnt enough
    - fetchmany: substitute method to use when using fetchall
    - fetchone:
    
## HyperText Transfer Protocol (HTTP)

### abstract
- 1.1 
    - TCP connection, keep-lived
    - header
- 2
    - 原本只能一個一個傳，但可支援多個
- 3
    - UDP as transition layer
### Content
- on application-layer protocol
- TCP/IP

#### Uniform Resources Identifiers, URI

URI- 更著重在定位資源的資訊

> ldap://dfadf.asdfa
> mailto:s@ex.com
> tel:+1-816-555-1212

#### Package 
- HTTP infromation at HTTP/1 is readable, but would be encapluse in frame at HTTP/2

#### HTTP Message
```
HTTP-message = start-line
               *( header-field CRLF )
               CRLF
               [ message-body ]
```
> carriage return followed by line feed, CRLF
- must have start line ex. `POST /?id=1 HTTP/1.1`
- Header: zero or one+ header field + CRLF
- CRLF- MUST include in message even thought there is no message body.
- Message-body: optional

#### Header
- content-encoding: content compression
**Request Header**
- Host(MUST): 'cause one ip could be bind to many domain(virtual server)
- User-agent
- Cookie: for state
- Authorization: identification on http connect
- Referer: catch previous url, mainly on commercial (不可靠，可被竄改，只會看前一個網頁的 URL)
**Response Header**

#### HTTP status code
- 301/302
    - 301 Moved Permanently
    - 302 Found（Moved Temporarily）
    - 301 會記住，直接過去。302 則每次都會發送
#### HTTP/2 WIN, WIN
- Header compression HPACK algorithm
- 可以將多個訊息合併成 frame
- Server push. When request incoming, server would pack all the related package
- 主要用在 chat，因為需要即時 refresh?

## EFK log 的時間
- 不能用 timestamp，會被當成 number data type
- 沒有 refresh index 時，`datetime.now()` 在 kibana 上面看到的會是正確的地區時間
- 沒有 refresh index 時，`datetime.utcnow()` 在 kibana 上面看到的會是正確的地區時間
    
    