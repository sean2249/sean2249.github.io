---
title: "Dockershim 即将被移除？看 SUSE Rancher 的应对之道！"
date: 2022-05-06T17:00:11+08:00
draft: false
categories:
- linkPage
tags:
- kubernetes
- docker
summary: "tags: kubernetes, docker"
---

https://juejin.cn/post/7072562828384665614

dockershim 預計在 kubernetes 1.24 版移除，而這個版本定於今年 4 月發布

dockershim 算是橋接 CRI-docker 的橋梁，意思即是 docker 更動的話，就必須去修改 dockershim 來符合 CRI，這實在有點麻煩，如此的話，我還不如去用更底層的 containerd
