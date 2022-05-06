---
title: "events: startup - shutdown"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- FastAPI
- backend
summary: "tags: FastAPI, backend"
---
https://fastapi.tiangolo.com/advanced/events/

```python=
@app.on_event('startup')
async def startup_event():
    ...
```
在 application 正式運行前執行 (可以多個 startup event，requests 會等全部的 startup event 結束後才會開始接收)，像是連接 database 產生初始資料

```python=
@app.on_event('shutdown')
def shutdown_event():
    with open('log.txt', mode='a') as log:
        log.write('Application shutdown')
```
在 application 被關閉後，可以做點像是清理 cache 或寫入紀錄。  
上面的例子，是將關閉資訊寫入檔案，利用 `open()` 不支援 async/await，所有是使用 `def` 而不是 `async def`
