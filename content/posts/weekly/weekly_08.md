---
title: "Weekly 08"
date: 2022-04-03T14:31:10+08:00
draft: false
categories:
- weekly
tags:
- kubernetes
- docker
- rancker
- efk
summary: "2022/03/20-2022/03/26"
---

- [Link](#link)
  - [Liked](#liked)
    - [[kubernetes] 原来 k8s pod也有生命周期？](#kubernetes-原来-k8s-pod也有生命周期)
    - [[docker] A better alternative for Docker Desktop?](#docker-a-better-alternative-for-docker-desktop)
    - [[Docker] The differences between Docker, containerd, CRI-O and runc](#docker-the-differences-between-docker-containerd-cri-o-and-runc)
  - [Others](#others)
    - [[kubernetes,rancher] [Rancher 系列文] - 介紹 Rancher](#kubernetesrancher-rancher-系列文---介紹-rancher)
    - [[kubernetes,efk] Deploy efk stack with helm3 in kubernetes](#kubernetesefk-deploy-efk-stack-with-helm3-in-kubernetes)
- [Notes](#notes)
- [Waiting to read](#waiting-to-read)
- [Meeting](#meeting)
  - [[Talk] 高併發](#talk-高併發)

# Link
## Liked

### [kubernetes] 原来 k8s pod也有生命周期？

https://juejin.cn/post/7072997050576699400

pod 的 postStart, preStop

### [docker] A better alternative for Docker Desktop?

https://medium.com/@oribenhur/a-better-alternative-for-docker-desktop-3e8fa38d618

因為在非 linux 下，需要額外的 linux backend，雖然說目前 QEMU 已經幫助很多，但在處理 heavy task 還是會有問題

> QEMU（quick emulator）是一款由法布里斯·贝拉（Fabrice Bellard）等人编写的免费的可执行硬件虚拟化的（hardware virtualization）开源托管虚拟机（VMM）。

![](https://i.imgur.com/QlQaAaY.png)


### [Docker] The differences between Docker, containerd, CRI-O and runc

https://www.tutorialworks.com/difference-docker-containerd-runc-crio-oci/

## Others

### [kubernetes,rancher] [Rancher 系列文] - 介紹 Rancher

https://www.hwchiu.com/rancher-2.html

Rancher 是一個 Kubernetes 管理平台，希望能夠讓團隊用更簡單及有效率的方式去管理各式各樣的 Kubernetes 叢集，其支援幾種不同方式

- Rancher 自行維護的 Kubernetes 版本，Rancher Kubernetes Engine(RKE)
- 各大公有雲所提供的 Kubernetes 服務，如 AKS, EKS 以及 GKE
- 任何使用者自己創建的 Kubernetes 叢集


### [kubernetes,efk] Deploy efk stack with helm3 in kubernetes

https://kamrul.dev/deploy-efk-stack-with-helm-3-in-kubernetes/

what is metalLB? is it required for setting?

# Notes

# Waiting to read

# Meeting 

## [Talk] 高併發

> 用 淘寶的雙 11 做範例

`<Google SRE>`
What is stable?
要有監控 不然什麼都抓不到

金字塔
1. monitoring 
2. incident response
3. postmortem/root cause analysis 
4. testing + release procedures 
5. capacity planning 
6. development 
7. product

found problem
with problem, has improvement method
without potential issues, need testing and release procedure
? what is cacpacity training 容量規劃


實際保障方法
業務活動 策略!!! 要在的依開始 planning 就先行
沒有這個規畫，拉高拉低都不對呢 

How to do load balance?
DNS load balance? use this for different region (asia, ameraica, europe)

multiple IDC for load balance

at single IDC?
limit

Different action
- browser only -> could we limit this
- Store item in cart? where to save this information

Service downgrade
- could we stop some service if not in required on this event
- 客戶部分 金流 購物車 必備!
- 商家部分 如何避免超額 商家活動(發紅包)

database selection
- 集群 高可用 分片/分庫
- Not centralized database, Distributed database
- Problem:
    - how to get global account analysis if sharding 
    - how to ensure logic (stored procedure), sql logic as service. difficult to switch database 
    
**沙盤推演**

**System & Biz profiling**
資金損失影響是說跟商家客戶的 SLA 損失

強弱依賴節點的判斷 
強連結影響很大!! 抓起來認真監控
包含系統跟業務
強跟弱的判斷 應該是根據數據判斷

數據是監控來的，可能是金流的損失


biz profiling
- When (業務時常)
- how much (預估體量): 1-9x 平常，若是超過則是為突發需要額外設計，但這種狀況通常是事前可以預見且短暫不是常態


**monitoring**
black-box/white-box

white-box(aplication level): java used -> jbm garbage collection monitor
with application detailed


- System-level
    - cpu/memory 
- application -level 
    - OOM, YGC, FGC
- Application middleware
    - DBS
- Biz-level
    - QPS
    
DE cannot combine all the above monitor. All this stuff is seperate on multiple platform

Level, threshold, notify method, report

資損
- hardware
- 商譽 (app 的負評增加量)


**incident response** 緊急/前置預案梳理
應急方案
如果採用備用的 VM，會不會有佈版本的時間
這樣搭配這個時間，業務面該做什麼手段避免空窗

遇到事情的止血 root cause analysis 的素材

異常演練!!!!! 雖然當初只是為了應付 ISMS
設計這個，避免盲目
像是 3台 VM，直接關一台

異地備援 database 很難做捏，沒有摳摳

機器 log 水位紀錄

可以做的止血策略
- 入口限流: 下流強依賴負載被打滿，可以透過地區暴力分
- 下流降級: 弱依賴不可用
- 單點失敗移除
- 切換: 資料庫 master/slave 的切換，若是 application 沒有針對這個做，還是會掛點


