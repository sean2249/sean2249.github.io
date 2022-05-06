---
title: "`Body` with multiple `examples`"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- FastAPI
summary: "tags: FastAPI"
---
https://fastapi.tiangolo.com/tutorial/schema-extra-example/#body-with-multiple-examples

fastapi 的 example 讓你可以在 swagger 上面，有些預設的 request body/parameter 可以選擇及參考~ 很方便

這邊講的 examples 不是單純指 body，還可以用在
- Path()
- Query()
- Header()
- Cookie()
- Body()
- Form()
- File()

單一的 example: `example=<你想要呈現的例子>` 
```python=
@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
```

多個 examples，你可以定義更多的資訊，甚至還有下拉選單!!
- summary: 下拉選單的選項名稱
- description: 更詳細的描述，支援 markdown
- value: 要當作 example 的值
- externalValues: alternative to value, a URL pointing to the example. Although this might not be supported by as many tools as value.

```python=
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
```
