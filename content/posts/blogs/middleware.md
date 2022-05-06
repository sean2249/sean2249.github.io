---
title: "middleware"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- FastAPI
- middleware
summary: "tags: FastAPI, middleware"
---
https://fastapi.tiangolo.com/tutorial/middleware/

你可以客製自己的 middleware 

```python=
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

```

