---
title: "[Day1] 淺談 Kubernetes 設計原理"
date: 2022-05-06T17:00:11+08:00
draft: false
categories:
- linkPage
tags:
- kubernetes
summary: "tags: kubernetes"
---

https://ithelp.ithome.com.tw/articles/10215384

k8s 平台維運商，定義多個 interface 供 plugin 連接，避免需要花時間納進去系統

- Container Runtimer Interface: 運算單元 containerd
- Container Network Interface: 平台容器網路連接能力
- Container Storage Interface: 提供儲存能力供容器使用
- Device Plugin: 可掛載各式各樣系統裝置
