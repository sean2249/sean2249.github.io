---
title: "Commit only part of a file in git"
date: 2022-05-06T16:59:32+08:00
draft: false
categories:
- linkPage
tags:
- git
summary: "tags: git"
---
https://stackoverflow.com/questions/1085162/commit-only-part-of-a-file-in-git

`git add` 預設會將檔案有修改的地方都加入到 staging area，但有時會想分開成兩個 commit 上傳，或是針對另一個修改的地方做回復

`git add --patch <filename>` 可以讓 git 針對每一塊修改的地方，讓你選擇要作為 commit 還是放棄作為 commit

而這篇就是在說明選項的全名是什麼XDDD 因為 git 裡面寫的是縮寫

