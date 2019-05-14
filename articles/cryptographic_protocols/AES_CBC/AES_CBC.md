---
layout: page
title: AES-CBC
type: cryptographic_protocols
update: Last Updated Thu, 12 Dec 2018 12:00:01 -0400
permalink: "articles/cryptographic_protocols/AES-CBC"
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
Cipher block chaining (CBC) is a mode of operation for a block cipher (one in which a sequence of bits are encrypted as a single unit or block with a cipher key applied to the entire block). Cipher block chaining uses what is known as an initialization vector (IV) of a certain length. One of its key characteristics is that it uses a chaining mechanism that causes the decryption of a block of ciphertext to depend on all the preceding ciphertext blocks. As a result, the entire validity of all preceding blocks is contained in the immediately previous ciphertext block.
