---
layout: page
title: Mode-GCM
type: symmetric_algorithms
update: Last Updated Thu, 12 Dec 2018 12:00:01 -0400
permalink: "articles/symmetric_algorithms/Mode_GCM/Mode-GCM.html"
alerts:
  - id: 1
    type: success
    description: GCM mode is an authenticated encryption scheme and is often recommended.
    link: ""
further-reading:

related-articles:

best_practices
  - name: Never Reuse Key, IV pairs.
    description: "Never encrypt with the same key and IV pair twice. Use one-time session keys whenever possible."
  - name: Do Not Exceed Data Limits.
    description: "GCM has a data limit of 64 GB. After this much data has been encrypted, the key and/or IV must be changed."
---

Galois/Counter mode (Galois is pronounced "GAL-wah") encryption (“GCM mode”) is a [block cipher mode of operation](/articles/concepts/block_cipher_modes.html) that combines _confidentiality_ *and* _data authentication_. This means that the encrypted data cannot be undetectably altered.

GCM mode builds on the concepts introduced in [CTR mode](/articles/symmetric_algorithms/Mode_CTR/Mode-CTR.html) and CTR mode should be reviewed first in order to understand GCM. As with CTR mode, GCM uses an IV/nonce and encrypts increasing counter values. But GCM extends the CTR operations to include a Message Authentication Code (MAC) calculation as a built-in part of the operation. The MAC, called a "tag" in GCM jargon, is verified during decryption. If it does not match the data must be discarded.

As with CTR mode, the encryption process is can be performed in parallel, but the calculation of the GCM tag can also be calculated in parallel. Thus, AES-GCM is typically faster than AES-CTR combined with a serial MAC calculation like, for example, HMAC.

GCM is most commonly used with AES; AES-GCM typically prefers a 12-byte IV and, as with CTR, this IV must not be reused. Moreover, for any key-IV pair, GCM is limited to encrypting 64 GB.
