---
title: "Request body + path + query parameters"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- FastAPI
- backend
- python
summary: "tags: FastAPI, backend, python"
---
https://fastapi.tiangolo.com/tutorial/body/#request-body-path-query-parameters

```python=
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

- `{item_id}` 是 path parameter
- `q` query parameter (singular type)
- `item` 則是 pydantic model -> request body

https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter
-> 使用 `Body` 來更完善 request body 的要求及 openapi 的 spec，像是 example

```python=
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
```
多加入 `embed=True`
```json=
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```
-> 變成需要額外加入 `item` 作為 key
```json=
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```
