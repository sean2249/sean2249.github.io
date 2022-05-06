---
title: "Why Can’t You Reverse a String With a Flag Emoji?"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- python string
- encoding
summary: "tags: python string, encoding"
---
https://davidamos.dev/why-cant-you-reverse-a-flag-emoji/

從 "🇺🇸"[::-1] 的結果，反推到 unicode 在 python 的實作

```python=
>>> "🇺🇸"[::-1]
🇸🇺
```

從上面的例子可發現 us flag 不是你想像中的單一字元，而是兩個字元合在一起。

接下來我們嘗試用 encode 的方式得到原生的 unicode，來避掉可能是不同編碼方式的錯誤 (ascii, utf-8, big5)

```python
>>> list("🇺🇸".encode())
[240, 159, 135, 186, 240, 159, 135, 184]
>>> # ^^^^^^^^^^^^^^---Code point for 🇺
>>> #                ^^^^^^^^^^^^^^^^^^---Code point for 🇸

>>> # The code points get swapped!
>>> list("🇺🇸"[::-1].encode())
[240, 159, 135, 184, 240, 159, 135, 186]
>>> # ^^^^^^^^^^^^^^---Code point for 🇸
>>> #                ^^^^^^^^^^^^^^^^^^---Code point for 🇺
```

成功的 encode 了，發現 us flag 總共分出了八個字元，四個為一組，才組成了 :us:。而在 reverse 中，是以一組為單位做 reverse，因此才導致 us -> su，而此 su 沒有辦法解析成 emoji 的格式，所以才跑出原生的兩個字

同理與中文字相同，中文的每個字也是多個字元為一組，但因為沒有像 emoji 一樣另外再轉一層查詢做圖片，所以才沒遇問題。

最後附上文中作者的整理
- Strings of symbols get converted to sequences of integers by a character encoding, usually UTF-8.
- Some characters are encoded as a single 8-bit integer by UTF-8, and others require two, three, or four 8-bit integers.
- Some symbols, such as flag emojis, are not directly encoded by Unicode. Instead, they are renders of sequences of Unicode characters and may or may not be supported by every platform.

內文還有講到更多 bits 的


## Others
