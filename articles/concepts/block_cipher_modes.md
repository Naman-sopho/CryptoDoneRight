---
layout: page1
title: Block Cipher Modes of Operation
type: concepts
update: Last Updated Sat, 17 Aug 2019 21:27:01 -0400
permalink: "articles/concepts/block_cipher_modes.html"
alerts:

further-reading:

related-articles:

warnings:
  - name: Never Use ECB.
    description: "Do NOT use the Electronic Code Book (ECB) mode of operation. This is only for testing!"
    
best_practices:
  - name: Use combined modes of operation.
    description: "Combined modes of operation both encrypt the data and protect it from modifications. Modes, such as GCM or CCM, are almost always a good choice."

---

# Block Cipher

Block ciphers are encryption algorithms that encrypt data in fixed-size chunks. Typically, the size of the chunk, or "block size" is very small (e.g., 16 bytes).

The most basic mode of operation for a block cipher is to just encrypt each chunk serially. An image file that was 16,000 bytes long, for example, would be broken up into 16-byte chunks and each chunk encrypted separately. This mode is known as "Electronic Code Book" mode, or ECB.

# NEVER USE ECB

ECB mode is always a bad idea because of the patterns that emerge. For a given key, AES will always encrypt the same 16 bytes to the same 16 output bytes. So, if the same 16 bytes happen repeatedly in a file, patterns emerge in the output. To visualize this, here is an image of the Linux "Tux" penguin:

![Original Tux](https://upload.wikimedia.org/wikipedia/commons/5/56/Tux.jpg "The Original Tux")

And here is that same image "encrypted" by ECBmode.

![Disguised Tux](https://upload.wikimedia.org/wikipedia/commons/f/f0/Tux_ecb.jpg "Tux in Disguise?!")

Hopefully, it's clear that this isn't very "secret."

There are a number of modes of operation that, if used correctly, will adequately protect data. Three of the more common modes of operation include:

1. Counter Mode (CTR)
1. Cipher-Block-Chaining Mode (CBC)
1. Galois Counter Mode (GCM)

GCM is different from CTR and CBC because it is a "combined" mode of operation. A combined mode of operation provides _both_ confidentiality AND message integrity. That means that not only can the encrypted data not be read, it cannot be undetectably altered without knowledge of the key. Combined modes of operation, when useable, are almost always a better choice than modes like CTR and CBC.

The modes listed on this page are _not_ an exhaustive list. Each mode has its own strength and weaknesses and it is possible to abuse each one of these. For specific guidance on how to safely and correctly configure, refer to algorithm specific pages. For example, in addition to the article on AES, there is also an artcle for AES-CTR, AES-CBC, and AES-GCM.

