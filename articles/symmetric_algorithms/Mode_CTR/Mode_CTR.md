---
layout: page
title: "Mode: CTR"
type: symmetric_algorithms
update: Last Updated Tues, 27 Aug 2019 12:00:01 -0400
permalink: /articles/symmetric_algorithms/Mode_CTR/Mode-CTR.html
alerts:
  - id: 1
    type: success
    description: CTR is a good choice for a mode of operation when better, authenticated modes like GCM cannot be used.
further-reading:

related-articles:

warnings:
  - name: Never Reuse Key, IV pairs.
    description: "Never encrypt with the same key and IV pair twice. Use one-time session keys whenever possible."
  - name: CTR is Vulnerable to Alteration.
    description: "Unless a Message Authentication Code (MAC) is used, data encrypted by CTR can be easily modified by attackers."
---

Counter-mode encryption (“CTR mode”) is a [block cipher mode of operation](/articles/concepts/block_cipher_modes.html) that was introduced by Diffie and Hellman as early as 1979. CTR effectively converts a block cipher that encrypts a block at a time into a stream cipher that encrypts a byte at a time.

Perhaps unintuitively, in CTR mode, a block cipher is _not_ used to directly encrypt the plaintext. Instead, an increasing counter of values is encrypted to produce a _key stream_. Conceptually, the block cipher is used to encrypt 0 (represented as a block-size of zeros), then used to encrypt 1, then 2, and so forth. To produce the ciphertext, the keystream is XORed with the plaintext.

The same keystream must never be reused to encrypt to different plaintexts. Accordingly, the counter does not actually start at 0; instead, the IV is used as a unique starting point. Because the IV does not have to be random, it is called a nonce.

CTR has a significant advantage over CBC in terms of performance because encryption and decryption can be parallelized. In CBC mode, one block must be encrypted before the next can be. But in CTR mode, the predictable counter values can be encrypted independent of each other enabling trivial parallelization. Unfortunately, this advantage can be lost in practice if a serialized Message Authentication Code (MAC) is used to prevent alteration of the ciphertext.

CTR mode is notoriously easy to alter and should not be used without a MAC under almost any circumstances.
