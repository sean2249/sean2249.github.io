---
title: "Stop Using Branches for Deploying to Different GitOps Environments"
date: 2022-05-09T03:59:14+08:00
draft: false
categories:
- linkPage
tags:
- helm
- kubernetes
summary: "tags: helm, kubernetes"
---

https://medium.com/containers-101/stop-using-branches-for-deploying-to-different-gitops-environments-7111d0632402

```
> From StarBugs 技術週刊 - 第 130 期
此推薦文章和下篇是同一系列，作者講述很多組織在使用 GitOps 如何在同一個 release 前進到下一個環境是大家一直探討的，因為答案有很多種，所以作者就索性說明哪些我們應該避免：
依環境分 git branches 只適用於 legacy applications（這裡指的是傳統 git-flow），採用 trunk-based 並且用依環境用 feature flag 來控制，application code 和 configuration code 也建議放在不同 repository
前進到下個環境從來不是只有 git merge 這麼簡單，兩次的 merge 都修改同一個地方時有可能會被忽略而 merge 進去了，hotfix 時的 cherry-picks 也得小心使用
依照環境分 branches 不太適合 Helm/Kustomize，因為它們並不會知道 git branches、git merge 或 pull request，因為他們都是靠檔案做環境分類
如果用 branch 來做環境的區隔，很容易在 merge 時出問題，因為從 staging -> uat，但可能 uat 沒有相對應的 database auth；或是 production 需要多個 replica，都需要小心在每個 branch 手動刪減，挺麻煩且危險
```

所以改成用多個 values 檔，比較容易控管，例如：values-staging.yaml, values-uat.yaml, values-prod.yaml

![](https://miro.medium.com/max/794/0*fgWHaGyfbYKZiQ7t.png)
