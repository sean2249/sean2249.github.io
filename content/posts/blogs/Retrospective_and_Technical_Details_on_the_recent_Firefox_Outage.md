---
title: "Retrospective and Technical Details on the recent Firefox Outage"
date: 2022-05-06T16:56:30+08:00
draft: false
categories:
- linkPage
tags:
- sre
summary: "tags: sre"
---
https://hacks.mozilla.org/2022/02/retrospective-and-technical-details-on-the-recent-firefox-outage/

大概就是講 GCP 偷偷升級衝康到 firefox，使得 load balancer 被改成 http/3 載入，其中影響特別是以 Rust service 為主，因為他是用 http/3 來架構，而其中的 header 屬於 case-sensitive，跟 http/1, http/2 的 case-insensitive 不一樣，導到 firefox 前置的 load balancer 無法正常的將系統導流

#### 架構
![structure](https://hacks.mozilla.org/files/2022/01/foxstuck-diagram4-768x409.png)
1. Necko: content-length
2. viaduct:
3. Rust service: Content-Length

#### 結論
- GCP 偷偷升級，好壞壞，好歹通知下讓我們準備個，或許讓我們可以在 staging enviroment 先測試
- 我們 load balancers 的設定是 Automatic (default)，這導致第三方服務平台升級，改變其 default 導致掛點，因此之後會選擇更明確的設定
- 雖然我們無法測試所有元件的組合，但 http 版未的升級會是非常大的議題，未來會更多加著手研究
