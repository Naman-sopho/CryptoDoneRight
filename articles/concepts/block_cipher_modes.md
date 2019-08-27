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

# Introduction: Block Ciphers

There are many encryption algorithms that encrypt data in fixed-size chunks called "blocks." Because they encrypt one block at a time, they are called "block ciphers." One of the most well-known block ciphers is [AES](/articles/symmetric_algorithms/AES/AES.html).

The size of a block is relatively small. AES's block size, for example, is just 16 bytes.

# Modes of Operation

The mode of operation for a block cipher is the way in which it encrypts data larger than its block size.

The most basic mode of operation for a block cipher is to just encrypt each chunk serially. For example, to encrypt an image file that was 16,000 bytes long using this approach with AES, one would first break up the file into 1,000 16-byte blocks and then encrypt each block using AES. This mode is known as "Electronic Code Book" mode, or ECB.

# WARNING! NEVER USE ECB

You should *NEVER* use ECB. The only exception is to test if a cipher is working correctly using something like, for example, a Known Answer Test.

The reason ECB is so terrible is because when encrypting one chunk at a time, patterns emerge. For a given key, AES will always encrypt the same 16 bytes to the same 16 output bytes. So, if the same 16 bytes happen repeatedly in a file, patterns emerge in the output. To visualize this, here is an image of the Linux "Tux" penguin:

![Original Tux](https://upload.wikimedia.org/wikipedia/commons/5/56/Tux.jpg "The Original Tux")

And here is that same image "encrypted" by ECB mode.

![Disguised Tux](https://upload.wikimedia.org/wikipedia/commons/f/f0/Tux_ecb.jpg "Tux in Disguise?!")

Hopefully, it's clear that this isn't very "secret."

_[Source: Wikipedia "Block cipher mode of operation"]_

# Commonly-Used Modes of Operation

There are a number of modes of operation that, if used correctly, will adequately protect data. Here are some modes of operation that can be safely used if used correctly:

1. Galois Counter Mode (GCM)
1. Counter Mode (CTR)
1. Cipher-Block-Chaining Mode (CBC)

These modes of operation are not limited to any specific cipher but rather can be applied to the common block ciphers in use today such as AES, Twofish, and Serpent. They are also used with legacy ciphers (that are no longer safe and should not be used) such as DES. The common naming scheme is to use the name of the cipher followed by the name of the mode of operation like, for example, AES-CBC, Twofish-GCM, etc.

GCM is different from CTR and CBC because it is a "combined" mode of operation. A combined mode of operation provides _both_ confidentiality AND message integrity. That means that not only can the encrypted data not be read, it cannot be undetectably altered without knowledge of the key. Combined modes of operation, when usable, are almost always a better choice than modes like CTR and CBC.

