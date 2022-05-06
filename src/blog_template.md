---
title: {{ article.title }}
date: {{ cur_time }}
draft: false
categories:
- linkPage
tags:
{% for tag in article.tags -%}
- {{ tag }}
{%- endfor %}
summary: "tags: {{ article.tags|join(', ') }}"
---
{{ article.content }}