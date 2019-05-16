---
layout: page
title: AES-CTR
type: symmetric_algorithms
update: Last Updated Thu, 12 Dec 2018 12:00:01 -0400
permalink: "articles/cryptographic_protocols/AES-CTR.html"
alerts:
  - id: 1
    type: success
    description: This is currently one of the two recommended modes of operation.
    link: ""
  - id: 2
    type: warning
    description: Configuration is vital. A misconfigured safe protocol is ultimately unsafe.
    link: ""
further-reading:

related-articles:

attacks:
---
Counter-mode encryption (“CTR mode”) was introduced by Diffie and Hellman already in 1979.CTR mode has significant efficiency advantages over the standard encryption
modes without weakening the security. In particular its tight security has been proven.  CTR mode is well suited to operate on a multi-processor machine where blocks can be encrypted in parallel.
