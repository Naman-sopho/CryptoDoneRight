---
layout: view_all
title: Articles
permalink: /view_all.html
---
<div class="row" style="margin-bottom:40px">
  <div class="col-sm-6">
    <h2> Standards </h2>
    {% include standards_list.html %}
  </div>
  <div class="col-sm-6">
    <h2> Guides </h2>
    <ul>
      <li><font size="4"><strong><a href="https://github.com/jhu-information-security-institute/CryptoDoneRight/blob/master/CONTRIBUTING-template.md">Contribution Guide</a></strong></font></li>
      <li><font size="4"><strong><a href="https://github.com/jhu-information-security-institute/CryptoDoneRight/blob/master/.github/ISSUE_TEMPLATE/pull_request_template.md">Pull Request Guide</a></strong></font></li>
      <li><font size="4"><strong><a href="https://github.com/jhu-information-security-institute/CryptoDoneRight/blob/master/.github/ISSUE_TEMPLATE/issue_template.md">Issue Template Guide</a></strong></font></li>
      <li><font size="4"><strong><a href="/flaw-categories.html">Generic Steps for Understanding Flaws</a></strong></font></li>
    </ul>
  </div>
  <div class="col-sm-6">
    <h2> Crypto Concepts </h2>
    {% include concepts_list.html %}
  </div>
  <div class="col-sm-6">
    <h2> Hashing Algorithms </h2>
    {% include hashing_list.html %}
  </div>
  <div class=" col-sm-6 ">
    <h2> Cryptographic protocols </h2>
    {% include crypto_list.html %}
  </div>
  <div class="col-sm-6">
    <h2> Symmetric Algorithms </h2>
    {% include symmetric_list.html %}
  </div>
  <div class="col-sm-6">
    <h2> Asymmetric Algorithms </h2>
    {% include asymmetric_list.html %}
  </div>
</div>
