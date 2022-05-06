---
title: "同事提出个我从未想过的问题，为什么Kubernetes要'多此一举'推出静态Pod概念？"
date: 2022-05-06T17:00:11+08:00
draft: false
categories:
- linkPage
tags:
- kubernetes
summary: "tags: kubernetes"
---

https://juejin.cn/post/7068954533610651662

正常的 pod 會由 master 管理/指定/分配，但 static-pod 則是綁定在某個 kubelet 上做操作。

- 不能透過 apiserver 管理，只能查詢到
- 重啟部份，則是交由 kubelet 自行恢復，重啟也還是在同一個 node

使用 static-pod 可防止誤刪除，確保核心服務在線，保障應用能運行穩定數量及穩定服務

像是 kubelet 的 static-pod
- 調度 `kube-scheduler`
- 秘書 `kube-apiserver`
- 核心大腦 `kube-controller-manager`
- 數據庫 `etcd`

![](https://i.imgur.com/k4hHXp3.png)

貓咪可愛
