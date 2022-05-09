---
title: "Weekly 11"
date: 2022-05-09T11:56:42+08:00
draft: false
categories:
- weekly
tags:
summary: "2022/04/24~2022/04/30"
---
- [Good](#good)
  - [[helm,kubernetes] Stop Using Branches for Deploying to Different GitOps Environments](#helmkubernetes-stop-using-branches-for-deploying-to-different-gitops-environments)
  - [[kubernetes,kubernetes plugin] Extend kubernetes Official Document](#kuberneteskubernetes-plugin-extend-kubernetes-official-document)
  - [[Design pattern] 中文的 design pattern 介紹!](#design-pattern-中文的-design-pattern-介紹)
  - [[Blog,Syntax beautify] Carbon: Create and share beautiful images of your source code.](#blogsyntax-beautify-carbon-create-and-share-beautiful-images-of-your-source-code)
  - [[Regular expression] Regular expression 展示他的判斷流程](#regular-expression-regular-expression-展示他的判斷流程)
- [Others](#others)
  - [[Nginx,Caddy,load balance] Migrate Nginx to Caddy](#nginxcaddyload-balance-migrate-nginx-to-caddy)

# Good
## [helm,kubernetes] Stop Using Branches for Deploying to Different GitOps Environments

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

## [kubernetes,kubernetes plugin] Extend kubernetes Official Document
Link: https://kubernetes.io/docs/concepts/extend-kubernetes/

Content:
![](https://d33wubrfki0l68.cloudfront.net/4829fda030a067042b836cebf29de0505b7fae5e/c5ea4/docs/concepts/extend-kubernetes/extension-points.png)


Krew is a tool that makes it easy to use kubectl plugins
https://github.com/kubernetes-sigs/krew

## [Design pattern] 中文的 design pattern 介紹!

https://refactoringguru.cn/design-patterns/catalog

裡面涵蓋超多種的 design pattern，想學!

## [Blog,Syntax beautify] Carbon: Create and share beautiful images of your source code.

https://carbon.now.sh/

把你的 code 裝飾得美美的，然後輸出成圖片~~
很適合用在 medium 上面，因為 medium 沒有支援 code syntax highlight

## [Regular expression] Regular expression 展示他的判斷流程

https://jex.im/regulex/#!flags=&re=%5E(a%7Cb)*%3F%24

# Others
## [Nginx,Caddy,load balance] Migrate Nginx to Caddy

Official website: https://caddyserver.com/

https://blog.wu-boy.com/2017/11/migrate-nginx-to-caddy/

https://juejin.cn/post/7085519712901136392
- 对比Nginx复杂的配置，其独创的Caddyfile配置非常简单；
- 可以通过其提供的Admin API实现动态修改配置；
- 默认支持自动化HTTPS配置，能自动申请HTTPS证书并进行配置；
- 能够扩展到数以万计的站点；
- 可以在任意地方执行，没有额外的依赖；
- 采用Go语言编写，内存安全更有保证。


Nginx 設定複雜複雜，聽說這個痕好用
用的語言是 golang

