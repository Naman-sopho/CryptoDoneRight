---
layout: view_all
title: Developer Quickstarts
permalink: /quickstarts/dev
---
<div class="container">
  <div style="padding: 4%">
    {% for b in site.pages %}
    <div class="item">
      {% if b.layout == "quickstart" and b.qtype == "dev" %}
        <li><font size="4"><strong><a href="{{b.url}}">{{b.type}}</a></strong></font></li>
      {% endif %}
    </div>
    {% endfor %}
  </div>
</div>
