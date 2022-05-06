---
title: "Additional responses in OpenAPI"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- FastAPI
summary: "tags: FastAPI"
---
https://fastapi.tiangolo.com/advanced/additional-responses/

```python=
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


app = FastAPI()


@app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
```

`@app.get(..., responses)` 定義 model 時，可以利用 content 的 keyword parameter 來塞入 pydantic model 作為輸出的格式，同時也會顯示在 openapi swagger 上面。

如果不想要那麼麻煩，就寫個 description 來描述該狀態的錯誤 

> 至於 httpexceptions / jsonresponse 不知道有什麼差別 QQ 可能一個是用 raise?
