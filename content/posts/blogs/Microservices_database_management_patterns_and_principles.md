---
title: "Microservices database management patterns and principles"
date: 2022-05-06T16:56:29+08:00
draft: false
categories:
- linkPage
tags:
- system structure
summary: "tags: system structure"
---
https://medium.com/design-microservices-architecture-with-patterns/microservices-database-management-patterns-and-principles-9121e25619f1

- Shifting to the monolithic architecture to microservices architecture
- hybrid database selection:
    - catalog: MongoDB
    - Shopping cart: redis
    - Ordering: SQL server
- when interact or sharing data between microservices -> you cant use ACID transactions between distributed systems. That means its challenging to implemnt queries and trasactions that visits to serverl microservices
- Patterns
    - The Database-per-Service pattern 
        - loose coupling of services
        - Provide to evole rapidly and easy to scale applications
        - Each microservices use different database (sql,no-sql,key-value) conected by message broker
    - The API Composition pattern
        - Gateway routing pattern
        - gateway aggregation pattern
        - gateway offloading pattern
    - The CQRS(Command Query Responsibility Segregation) pattern 
        - separate commands(Write) and queires(Read) in order to better perform querying several microservices
    - The Event Sourcing pattern 
        - provide to accumulate events and aggregates them into sequence of events in databses 
    - The Saga pattern 
    - The Shared Database anti-pattern
        - Dont use single databse across microservices
        - Might block microservices due to single-point-of-failure

