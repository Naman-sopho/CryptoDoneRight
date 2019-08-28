---
layout: page
title: "Mode: CBC"
type: symmetric_algorithms
update: Last Updated Tues, 27 Aug 2019 12:00:01 -0400
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
    description: "Never encrypt with the same key and IV pair twice. Use one-time session keys whenever possible."
  - name: IV's must be random.
    description: "Some modes of operation can use non-repeating, but non-random numbers (such as a counter) as IVs. This is NOT the case for CBC. The IV must be random."
  - name: CBC is Vulnerable to Alteration.
    description: "Unless a Message Authentication Code (MAC) is used, data encrypted by CBC can often be modified by attackers in ways that leak information."
  - name: Encrypt-then-MAC
    description: "When using a MAC with CBC, make sure to finish the CBC encryption first, then MAC the ciphertext. Do not MAC the plaintext and then encrypt."

---

Cipher block chaining (CBC) is a [block cipher mode of operation](/articles/concepts/block_cipher_modes.html). Used correctly, CBC enables a block cipher, such as AES, to provide confidentiality over data larger than the block size.

To overcome the problem of patterns emerging in ciphertext output as a result of individually and separately encrypting each block of plaintext, CBC mixes the output of each encrypted block with the input to the next block. That is, after a block is encrypted, the encrypted block is XORed with the next input block before encipherment. This creates a "chain" between the encryption of the first block all the way to the last. In fact, if you change just one bit in the first block, the entire output will change.

The first block is also XORed with a _random_ Initialization Vector (IV) before encryption. The IV prevents an attacker from deterministically mapping inputs to outputs. For example, if CBC encryption (using whatever block cipher) was used without an IV for file encryption, and if the key was used for each file, an attacker could tell if the first blocks of files were the same. After all, if the plaintext is the same, and the key is the same, the output is the same. The use of a random, unique IV ensures that the ciphertext is always unique, even for the same inputs.
