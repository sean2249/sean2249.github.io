---
title: "第一千零一篇的 cgroups 介紹"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- kubernetes
- cgroups
summary: "tags: kubernetes, cgroups"
---
https://medium.com/starbugs/%E7%AC%AC%E4%B8%80%E5%8D%83%E9%9B%B6%E4%B8%80%E7%AF%87%E7%9A%84-cgroups-%E4%BB%8B%E7%B4%B9-a1c5005be88c

對這個沒有很熟，但稍微強迫自己吸收點 (但下面就看不太懂了 ٩(ŏ﹏ŏ、)۶
- 可限制控制隔離 process 所使用到的系統資源，例如 CPU, memory, Disk I/O, Network...等
- Resource limiting, Prioritization, Accounting, Control
- 2006 process containers -> 2007 cgroups v1 -> 2016 cgroups v2
- cgroups 沒有 API/library 的操作方式，是透過 Linux Virtual File System 實作，可像檔案系統一樣，透過新增修改刪除資料夾檔案來設定
- 請使用 systemd unit 來管理 cgroup，身為 linux distribution 預設的系統管理服務，也是大家熟悉習慣的，請使用它! 

