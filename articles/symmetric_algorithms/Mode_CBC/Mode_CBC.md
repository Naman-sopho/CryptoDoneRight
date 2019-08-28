---
layout: page
title: Mode: CBC
type: symmetric_algorithms
update: Last Updated Thu, 12 Dec 2018 12:00:01 -0400
permalink: "articles/symmetric_algorithms/Mode_CBC/Mode-CBC.html"
alerts:
  - id: 1
    type: warning
    description: While not broken, CBC has enough ways of being misused that many cryptographers are moving away from it. CTR is often seen as better, and combined modes of operations, such as GCM, are preferred.
    link: ""
further-reading:

related-articles:

warnings:
  - name: Never Reuse Key, IV pairs.
    description: "Never encrypt with the same key and IV pair twice. Use one-time session keys whenever possible, never encrypt with the same key twice, just to be safe."
  - name: CBC is Vulnerable to Alteration.
    description: "Unless a Message Authentication Code (MAC) is used, data encrypted by CBC can often be modified by attackers in ways that leak information."
    
---

Cipher block chaining (CBC) is a [block cipher mode of operation](/articles/concepts/block_cipher_modes.html). Used correctly, CBC enables a block cipher, such as AES, to provide confidentiality over data larger than the block size.

To overcome the problem of patterns emerging in ciphertext output as a result of individually and separately encrypting each block of plaintext, CBC mixes the output of each encrypted block with the input to the next block. That is, after a block is encrypted, the encrypted block is XORed with the next input block before encipherment. This creates a "chain" between the encryption of the first bits to the last.