---
title: "Why Canât You Reverse a String With a Flag Emoji?"
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

å¾ "ðºð¸"[::-1] ççµæï¼åæ¨å° unicode å¨ python çå¯¦ä½

```python=
>>> "ðºð¸"[::-1]
ð¸ðº
```

å¾ä¸é¢çä¾å­å¯ç¼ç¾ us flag ä¸æ¯ä½ æ³åä¸­çå®ä¸å­åï¼èæ¯å©åå­ååå¨ä¸èµ·ã

æ¥ä¸ä¾æååè©¦ç¨ encode çæ¹å¼å¾å°åçç unicodeï¼ä¾é¿æå¯è½æ¯ä¸åç·¨ç¢¼æ¹å¼çé¯èª¤ (ascii, utf-8, big5)

```python
>>> list("ðºð¸".encode())
[240, 159, 135, 186, 240, 159, 135, 184]
>>> # ^^^^^^^^^^^^^^---Code point for ðº
>>> #                ^^^^^^^^^^^^^^^^^^---Code point for ð¸

>>> # The code points get swapped!
>>> list("ðºð¸"[::-1].encode())
[240, 159, 135, 184, 240, 159, 135, 186]
>>> # ^^^^^^^^^^^^^^---Code point for ð¸
>>> #                ^^^^^^^^^^^^^^^^^^---Code point for ðº
```

æåç encode äºï¼ç¼ç¾ us flag ç¸½å±ååºäºå«åå­åï¼ååçºä¸çµï¼æçµæäº :us:ãèå¨ reverse ä¸­ï¼æ¯ä»¥ä¸çµçºå®ä½å reverseï¼å æ­¤æå°è´ us -> suï¼èæ­¤ su æ²æè¾¦æ³è§£ææ emoji çæ ¼å¼ï¼æä»¥æè·åºåççå©åå­

åçèä¸­æå­ç¸åï¼ä¸­æçæ¯åå­ä¹æ¯å¤åå­åçºä¸çµï¼ä½å çºæ²æå emoji ä¸æ¨£å¦å¤åè½ä¸å±¤æ¥è©¢ååçï¼æä»¥ææ²éåé¡ã

æå¾éä¸æä¸­ä½èçæ´ç
- Strings of symbols get converted to sequences of integers by a character encoding, usually UTF-8.
- Some characters are encoded as a single 8-bit integer by UTF-8, and others require two, three, or four 8-bit integers.
- Some symbols, such as flag emojis, are not directly encoded by Unicode. Instead, they are renders of sequences of Unicode characters and may or may not be supported by every platform.

å§æéæè¬å°æ´å¤ bits ç


## Others
