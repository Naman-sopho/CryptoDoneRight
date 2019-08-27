---
layout: page
title: GCM
type: Guide
update: Last Updated Thu, 12 Dec 2018 12:00:01 -0400
permalink: "articles/concepts/block_cipher_modes/GCM.html"

further-reading:

related-articles:

attacks:
---

# GCM Overview

Galois Counter Mode, or GCM, is a [Block Cipher Mode of Operation](/articles/concepts/block_cipher_modes.html). To understand how GCM works you should first understand [Couter Mode (CTR)](/articles/concepts/block_cipher_modes/CTR.html). At its core, GCM uses most of the CTR mode concepts and construction. Thus, GCM imports many of the strengths and weaknesses of CTR.

However, GCM is a _combined_ mode of operation that provides data authenticity as well as the usual confidentiality. Unlike both CBC and CTR, the GCM encrypted data _cannot be undetectably altered_. GCM produces a Message Authentication Code (MAC) called a "tag" as part of the encryption operation. The authentication tag is subsequently verrified as part of the decryption operation.
