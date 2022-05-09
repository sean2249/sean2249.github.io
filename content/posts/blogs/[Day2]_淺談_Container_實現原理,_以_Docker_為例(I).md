---
title: "[Day2] 淺談 Container 實現原理, 以 Docker 為例(I)"
date: 2022-05-06T17:00:11+08:00
draft: false
categories:
- linkPage
tags:
- kubernetes
- docker
summary: "tags: kubernetes, docker"
---

https://ithelp.ithome.com.tw/articles/10216215

每個 container 都必須遵守，但因這些規範而做的設定，會因不同平台而需獨立設計來描述
Open Container Initiative
- Runtime Spec
- Image Spec

Runtime Spec
- file format
- env consistent
- Support lifecyle on 

ImageSpec
1. layer: file system 
2. image index: image description
3. configuration: application env
