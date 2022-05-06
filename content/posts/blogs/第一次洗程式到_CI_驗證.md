---
title: "第一次洗程式到 CI 驗證"
date: 2022-05-06T17:00:11+08:00
draft: false
categories:
- linkPage
tags:
- devops
- ci
- testing
summary: "tags: devops, ci, testing"
---

https://ithelp.ithome.com.tw/articles/10184841

**當沒有 CI 的時候**
舉實際遇到的幾個反例：

- 前端人員程式寫好後不做驗證，因為他認為後端沒完成，不能驗證
- 後端人員程式寫好後不做驗證，因為他說測試人員測過就好
- 測試人員測完發現有問題卻不修改，因為修改時間過長，老闆決定從業務面 workaround ，先上再說

這個反例，簡單來說就是：
- 開發人員不願幫程式做健檢
- 測試人員健檢又不完整
- 程式在健檢不完整的情況都發現有病了，老闆又硬要程式帶病上陣
