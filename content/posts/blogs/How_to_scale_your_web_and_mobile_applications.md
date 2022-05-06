---
title: "How to scale your web and mobile applications"
date: 2022-05-06T16:56:29+08:00
draft: false
categories:
- linkPage
tags:
- system structure
summary: "tags: system structure"
---
https://enlear.academy/how-to-scale-your-web-and-mobile-applications-5be74bf99226

- 從最簡單的 web app，因應服務人數的升級及 SLA 的要求，不斷的調整架構
1. Basic design for a web app
    - single app server
    - Database
3. Scaling the app servers: requests to the application server grow. Need for leveling up the CPU capacity.
    - Load balancers for multiple app server
    - Session store: memcached/redis
1. Scaling the database with caching: database crisis for incread requests. store most requested data in the distributed cache system
    - distributed cache system to support database
1. Distributing the database: caching is not enough to reduce the volume of work on your databse -> horional scaling (stored across multiple DB instances)
    - Distributed database system
1. Increasing RESPONSIVENESS: Some mission takes lots of time, and cannot response in time.
    - queuing system

1. we started from the design of a simple Web app
2. we increased the compute capacity by adding more instances and a load balancer
3. we relieved our DB from the extra load by leveraging the caching system
4. we scaled out DB, turning it into a distributed database system
5. we improved the responsiveness of our application using a queuing system
