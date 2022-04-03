---
title: "Weekly 06"
date: 2022-03-13T17:45:39+08:00
draft: false
categories:
- weekly
tags:
- grpc
- kubernetes
- incident
- sre
- security
- development
- scrum
- code review
- devops
- system structure
- microservices
- software
- design pattern
- microservices
- kubernetes-toy
- dev enviroment
- docker
- testing
- ci
- kubernetes toy

summary: 2022/03/06 - 2022/03/12
---

- [Link](#link)
  - [Liked](#liked)
    - [[gRPC] gRPC Getting Started](#grpc-grpc-getting-started)
    - [[kubernetes] 一文搞懂容器运行时 Containerd](#kubernetes-一文搞懂容器运行时-containerd)
    - [[incident,sre] Incident severity and priority 101](#incidentsre-incident-severity-and-priority-101)
    - [[kubernetes] 同事提出个我从未想过的问题，为什么Kubernetes要"多此一举"推出静态Pod概念？](#kubernetes-同事提出个我从未想过的问题为什么kubernetes要多此一举推出静态pod概念)
    - [[security] 一次搞懂密碼學中的三兄弟 — Encode、Encrypt 跟 Hash](#security-一次搞懂密碼學中的三兄弟--encodeencrypt-跟-hash)
    - [[development,scrum] Scrum 完成的定義](#developmentscrum-scrum-完成的定義)
    - [[code review] Code Review Guidelines for Data Science Teams](#code-review-code-review-guidelines-for-data-science-teams)
    - [[sre,devops] Infrastructure-as-code 如何改善我們的生活品質？](#sredevops-infrastructure-as-code-如何改善我們的生活品質)
    - [[sre,devops] [好文翻譯] 你在找的是 SRE 還是 DevOps？](#sredevops-好文翻譯-你在找的是-sre-還是-devops)
    - [[sre,devops] Youtube - Class SRE implements DevOps](#sredevops-youtube---class-sre-implements-devops)
  - [Others](#others)
    - [[sre,system structure] Rapid Event Notification System at Netflix](#sresystem-structure-rapid-event-notification-system-at-netflix)
    - [[kubernetes] 如何选择 Containerd 和 Docker](#kubernetes-如何选择-containerd-和-docker)
    - [[software] 曝光一个很多人都不知道的学习网站 - 阿里雲](#software-曝光一个很多人都不知道的学习网站---阿里雲)
    - [[microservices,system structure] Hodor: Detecting and addressing overload in LinkedIn microservices](#microservicessystem-structure-hodor-detecting-and-addressing-overload-in-linkedin-microservices)
    - [[design pattern] Chain of responsibility](#design-pattern-chain-of-responsibility)
    - [[kubernetes-toy] 一个好玩的Go项目，3D界面管理k8s集群，真好玩](#kubernetes-toy-一个好玩的go项目3d界面管理k8s集群真好玩)
    - [[kubernetes,docker] Dockershim 即将被移除？看 SUSE Rancher 的应对之道！](#kubernetesdocker-dockershim-即将被移除看-suse-rancher-的应对之道)
    - [[dev enviroment] Tabby: 再见 Xshell ！这款开源的终端工具逼格更高！](#dev-enviroment-tabby-再见-xshell-这款开源的终端工具逼格更高)
    - [[kubernetes,windows] Rancher Desktop: 一键部署 K8S 环境，10分钟玩转，这款开源神器实在太香了！](#kuberneteswindows-rancher-desktop-一键部署-k8s-环境10分钟玩转这款开源神器实在太香了)
    - [[kubernetes] [Day1] 淺談 Kubernetes 設計原理](#kubernetes-day1-淺談-kubernetes-設計原理)
    - [[kubernetes,docker] [Day2] 淺談 Container 實現原理, 以 Docker 為例(I)](#kubernetesdocker-day2-淺談-container-實現原理-以-docker-為例i)
    - [[devops,ci,testing] 第一次洗程式到 CI 驗證](#devopscitesting-第一次洗程式到-ci-驗證)
    - [[software] Continuous Learning Tips for Software Engineers](#software-continuous-learning-tips-for-software-engineers)
- [Notes](#notes)
- [Waiting read](#waiting-read)

# Link
## Liked

### [gRPC] gRPC Getting Started

https://pjchender.dev/golang/grpc-getting-started/

覺得這篇很棒! 把 grpc 跟 restful 的相關相異之處都提到了

HTTP/2 的使用，同個 tcp 可進行多個請求和回應，壓縮

### [kubernetes] 一文搞懂容器运行时 Containerd

https://www.qikqiak.com/post/containerd-usage/

從出生前的 docker 當道，到出生深耕在 kubernetes 內的故事

Container Runtime Interface - 定義 container 與 kubernetes 進行互動的接口

> 由 google/redhat 推出，目的是為了擺脫 kubernets 必須與特定的容器運行


### [incident,sre] Incident severity and priority 101
https://firehydrant.io/blog/incident-severity-and-priority-101/

就是當 incident 發生時，我們必須立即定義此 incident 的嚴重程度 (severity) 跟優先度 (priority)

有時嚴重程度高，但使用機率低，可能優先度就比較後面一點

反之，也有可能

嚴重程度比較偏向系統面的破損，而優先度則是該破損造成的客戶體驗，使得要不要提前修繕

文中講了關於這兩種程度的 level 定義，還算實用滴啦

### [kubernetes] 同事提出个我从未想过的问题，为什么Kubernetes要"多此一举"推出静态Pod概念？

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

### [security] 一次搞懂密碼學中的三兄弟 — Encode、Encrypt 跟 Hash

https://medium.com/starbugs/what-are-encoding-encrypt-and-hashing-4b03d40e7b0c

### [development,scrum] Scrum 完成的定義

https://vocus.cc/article/5b72cbecfd89780001815d2c

如何定義 scrum 裡的 issue 完成標準，避免每個人心中的完成都不一樣，要等到最後的 sprint review 再掀牌，會炸鍋的


### [code review] Code Review Guidelines for Data Science Teams


https://tdhopper.com/blog/code-review-guidelines


### [sre,devops] Infrastructure-as-code 如何改善我們的生活品質？

https://medium.com/kkstream/infrastructure-as-code-%E5%A6%82%E4%BD%95%E6%94%B9%E5%96%84%E6%88%91%E5%80%91%E7%9A%84%E7%94%9F%E6%B4%BB%E5%93%81%E8%B3%AA-ee11e9d67b71

將建置從 cli 轉移到 code 上，方便管控及追蹤

上 git 後，任何改變都有跡可尋，不再是工程師自己留一下

可避免重覆事件，或者是下錯指令

### [sre,devops] [好文翻譯] 你在找的是 SRE 還是 DevOps？

https://medium.com/kkstream/%E5%A5%BD%E6%96%87%E7%BF%BB%E8%AD%AF-%E4%BD%A0%E5%9C%A8%E6%89%BE%E7%9A%84%E6%98%AF-sre-%E9%82%84%E6%98%AF-devops-2ded43c2852


避免維運團隊一直在救火，最後才發現是開發團隊的 code 發生問題

Develop - Agility
Operation - Stability

1. SRE
```
class SRE implements DevOps
```

2. SLI/SLO/SLA
- Service Level Objectives
    - Define availbity 
    - level availablity
    - plan in case of failure 

- Service Level Indicators (what is up/down)
    - requests latency 
    - bathc throughput 
    - failures per requets
    
SLO upper/lower bound
service much more reliable -> release of features might be slowing down
User unhappy for breaking more often than before if trying to down SLO
    
- Service Level Agreements
    - Business agreemnt between customers associated with SLo
    
SLIs drive SLOs which inform SLAs
![](https://i.imgur.com/X0GnJFP.png)

example
- SLI: 95th percentile latency of homepage requests over past 5 mins < 300ms
- SLO: 95th percentile homepage SLI will succeed 99.9% over trailing yeat
- SLA: service credits if 95th percentile homepage SLI succeeds less than 99.5% over trailing year

SLI - 定義系統運作的指標
SLO - 根據 sli 的指標，定義臨界值或期待值
SLA - 依據 SLO 的定義，與客戶協調服務持續運行的百分比；像是每年或每月的停機時不得低於幾分鐘

3. Risk and Error Budgets

沒有 100% 的服務，任何服務任何模型都有可能犯錯

人也會啊


追求 100% 的 SLA 

99.999% -> 99.999% 使用者根本感覺不清楚，但 SRE 會為了這個努力超級超級久 

計算出可以容忍的「犯錯預算」，一旦這個預算耗盡，才應該開始將重點放在可靠性的改善而非持續開發新功能。

4. Toil 

Toil 
- manual
- repetiive 
- automatable
- tactical
- devoid of long-term value

不是把要做的事轉成腳本，你還是要手動執行


### [sre,devops] Youtube - Class SRE implements DevOps

https://www.youtube.com/playlist?list=PLIivdWyY5sqJrKl7D2u-gmis8h9K66qoj

Google 針對提出的 SRE 概所做的一系列影片


## Others

### [sre,system structure] Rapid Event Notification System at Netflix
https://netflixtechblog.com/rapid-event-notification-system-at-netflix-6deb1d2b57d1

event 推播系統

- 跨平台的通知，電視會時常關機，手機則是一直在線 -> Hybrid push and pull delivery
- 通知的即時性，逾期不發送

### [kubernetes] 如何选择 Containerd 和 Docker

https://cloud.tencent.com/document/product/457/35747


why docker is not stable for production

### [software] 曝光一个很多人都不知道的学习网站 - 阿里雲
https://juejin.cn/post/7069615648120242207

https://help.aliyun.com/

就是從阿里雲的官方文件去學習


https://help.aliyun.com/document_detail/100734.html

像是 Redis 這篇災備方案介紹，就提到了 redis 發生故障時，可能失去的數據一致性及業務可用性

利用不同的服務框架，你可以避免掉的狀況

### [microservices,system structure] Hodor: Detecting and addressing overload in LinkedIn microservices

https://engineering.linkedin.com/blog/2022/hodor--detecting-and-addressing-overload-in-linkedin-microservic

從原本單一的 java application，到現在的超大型服務，流量的控管及限制就是重要的事項! 而 hodor 就是 linkedin 的殺手武器

三個主要元件: 

- overload detectors: 當服務超載時，回報狀況，可同時有多個偵測器，且在 gloabl level 
- load shedder: 決定當服務超載時，要先捨棄哪個流量
- platform-specific adapter to combine the two: 轉化任何相關的 data 到可被 detectors/shedder 所認識的格式

因為 java memory 是交給 gabarge collection 處理，所以我們專注在 CPU 上

在收集 cpu 使用率，我們選擇用 JVM 做為我們效能的收集，可以獲得 latency increases, CPU saturation, GC activity


### [design pattern] Chain of responsibility
https://refactoring.guru/design-patterns/chain-of-responsibility/python/example

查了下 chain of responsibility 的寫法，喜歡這個，有 `set_next` 整個變得很乾淨


### [kubernetes-toy] 一个好玩的Go项目，3D界面管理k8s集群，真好玩

https://juejin.cn/post/7051242364735586317

用 minecraft 來操控 kubernetes

### [kubernetes,docker] Dockershim 即将被移除？看 SUSE Rancher 的应对之道！

https://juejin.cn/post/7072562828384665614

dockershim 預計在 kubernetes 1.24 版移除，而這個版本定於今年 4 月發布

dockershim 算是橋接 CRI-docker 的橋梁，意思即是 docker 更動的話，就必須去修改 dockershim 來符合 CRI，這實在有點麻煩，如此的話，我還不如去用更底層的 containerd

### [dev enviroment] Tabby: 再见 Xshell ！这款开源的终端工具逼格更高！

https://mp.weixin.qq.com/s/vX6Tq30Jnyo4IhLucdVceA

感覺蠻適合用在 windows

### [kubernetes,windows] Rancher Desktop: 一键部署 K8S 环境，10分钟玩转，这款开源神器实在太香了！

https://juejin.cn/post/7070683049049980941

### [kubernetes] [Day1] 淺談 Kubernetes 設計原理

https://ithelp.ithome.com.tw/articles/10215384

k8s 平台維運商，定義多個 interface 供 plugin 連接，避免需要花時間納進去系統

- Container Runtimer Interface: 運算單元 containerd
- Container Network Interface: 平台容器網路連接能力
- Container Storage Interface: 提供儲存能力供容器使用
- Device Plugin: 可掛載各式各樣系統裝置

### [kubernetes,docker] [Day2] 淺談 Container 實現原理, 以 Docker 為例(I)

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

### [devops,ci,testing] 第一次洗程式到 CI 驗證

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

### [software] Continuous Learning Tips for Software Engineers

https://medium.com/@aleydis/continuous-learning-tips-for-software-engineers-4d15f42681aa

Dont stop learning!! Even though u are not a software engineer

# Notes

# Waiting read
https://juejin.cn/post/7072392430103822349