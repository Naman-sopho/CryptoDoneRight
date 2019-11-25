---
layout: view_all
title: Manager Quickstarts
permalink: /quickstarts/manager.html
---
<div class="container">
  <div style="padding: 4%">
    {% for b in site.pages %}
    <div class="item">
      {% if b.layout == "quickstart" and b.qtype == "manager" %}
        <li><font size="4"><strong><a href="{{b.url}}">{{b.type}}</a></strong></font></li>
      {% endif %}
    </div>
    {% endfor %}
  </div>
</div>
