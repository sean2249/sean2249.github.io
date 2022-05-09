---
title: "Migrate Nginx to Caddy"
date: 2022-05-09T03:59:14+08:00
draft: false
categories:
- linkPage
tags:
- nginx
- caddy
- load balance
summary: "tags: nginx, caddy, load balance"
---

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
