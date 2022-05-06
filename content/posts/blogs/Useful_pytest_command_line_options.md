---
title: "Useful pytest command line options"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- Pytest
summary: "tags: Pytest"
---
https://www.thedigitalcatonline.com/blog/2018/07/05/useful-pytest-command-line-options/

主要是介紹 pytest skip 的功能


簡單的 skip，只要加上 decorator 即可
```python=
@pytest.mark.skip
def test_a():
    ...
```

加入 reason，使 pytest 運行到此 test 會多印些資訊
```python=
@pytest.mark.skip(reason='I want to skip')
def test_b():
    ...
```

加入條件判斷
```python=
@pytest.mark.skipif(os.environ['AWS_REGION'] == 'us-west-2', reason='I want to skip')
def test_b():
    ...
```

標籤 test，可指定要跑跟不跑的
```python=
@pytest.mark.slow
def test_slow():
    ...
```

下面指令會只運行有標註為 `slow` 的 test
```shell=
$ pytest -m slow
```

或是你不想運行 slow 
```shell=
$ pytest -m 'not slow'
```

或是更華麗的，slow or fast 都跑
```shell=
$ pytest -m 'slow or fast'
```

上面都是針對 test function 來做，下面則是不同的方式 skip


跑到一半 skip
```python=
def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")
```

載入 module 時，skip 整個 module
```python=
import sys
import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)
```
