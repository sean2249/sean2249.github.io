---
title: "Hodor: Detecting and addressing overload in LinkedIn microservices"
date: 2022-05-06T17:00:11+08:00
draft: false
categories:
- linkPage
tags:
- microservices
- system structure
summary: "tags: microservices, system structure"
---

https://engineering.linkedin.com/blog/2022/hodor--detecting-and-addressing-overload-in-linkedin-microservic

從原本單一的 java application，到現在的超大型服務，流量的控管及限制就是重要的事項! 而 hodor 就是 linkedin 的殺手武器

三個主要元件: 

- overload detectors: 當服務超載時，回報狀況，可同時有多個偵測器，且在 gloabl level 
- load shedder: 決定當服務超載時，要先捨棄哪個流量
- platform-specific adapter to combine the two: 轉化任何相關的 data 到可被 detectors/shedder 所認識的格式

因為 java memory 是交給 gabarge collection 處理，所以我們專注在 CPU 上

在收集 cpu 使用率，我們選擇用 JVM 做為我們效能的收集，可以獲得 latency increases, CPU saturation, GC activity

