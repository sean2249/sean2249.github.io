---
title: "街口支付 API 自動化測試解決方案"
date: 2022-05-06T16:56:30+08:00
draft: false
categories:
- linkPage
tags:
- system design
- testing
summary: "tags: system design, testing"
---
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
