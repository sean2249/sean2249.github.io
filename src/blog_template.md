---
title: {{ article.title }}
date: {{ cur_time }}
draft: false
categories:
- weekly
- linkPage
tags:
{% for tag in article.tags -%}
- {{ tag }}
{%- endfor %}
---
{{ article.content }}