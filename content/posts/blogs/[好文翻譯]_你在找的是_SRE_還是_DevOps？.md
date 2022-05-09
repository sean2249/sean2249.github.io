---
title: "[好文翻譯] 你在找的是 SRE 還是 DevOps？"
date: 2022-05-06T17:00:11+08:00
draft: false
categories:
- linkPage
tags:
- sre
- devops
summary: "tags: sre, devops"
---

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

