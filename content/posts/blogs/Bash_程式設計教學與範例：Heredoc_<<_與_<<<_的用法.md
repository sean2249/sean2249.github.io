---
title: "Bash 程式設計教學與範例：Heredoc << 與 <<< 的用法"
date: 2022-05-06T16:56:30+08:00
draft: false
categories:
- linkPage
tags:
- linux
- shell
summary: "tags: linux, shell"
---
https://officeguide.cc/bash-tutorial-here-document-string/

Here document command 的使用，可以將多行資料寫入指令的參數

```shell=
cat > output.txt << EOF
line1
line2
line3
EOF
```
