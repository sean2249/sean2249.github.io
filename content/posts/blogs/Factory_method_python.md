---
title: "Factory method python"
date: 2022-05-06T16:56:30+08:00
draft: false
categories:
- linkPage
tags:
- python
- design pattern
summary: "tags: python, design pattern"
---
https://realpython.com/factory-method-python/

利用工廠模式來抽離實作的複雜度，讓輸出輸入保持統一的格式，中間的工廠可隨意搭配
- 隱藏複雜的實作細節，增加程式易讀性
- Combining similar features under a common interface

User 只需要知道 serialize 的 function 及其資料的格式
- `serialize`
- `_get_serializer` Creator component, 決定要實做哪個
```python=
class SongSerializer:
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)
```
就算未來需要新增格式，也只需要多加一個 if condition

也可以改寫成
```python=
class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)


def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)
```

- Factory method
- Abstract factory method

或是動態載入的方式，利用 register 來新增產品
```python=
# In object_factory.py

class ObjectFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)
```

要生成的 builder，initial 不會載入，直到 `__call__` 的時候
```python=
class SpotifyServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, spotify_client_key, spotify_client_secret, **_ignored):
        if not self._instance:
            access_code = self.authorize(
                spotify_client_key, spotify_client_secret)
            self._instance = SpotifyService(access_code)
        return self._instance

    def authorize(self, key, secret):
        return 'SPOTIFY_ACCESS_CODE'
```


然後 `register_builder` 來將實作放入此 factory
```python=
factory = object_factory.ObjectFactory()
factory.register_builder('SPOTIFY', SpotifyServiceBuilder())
factory.register_builder('PANDORA', PandoraServiceBuilder())
factory.register_builder('LOCAL', create_local_music_service)
```
