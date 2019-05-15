---
layout: page
title: DES CBC
type: cryptographic_protocols
update: Last Updated Fri, 3 May 2019 16:53:00 -0400
permalink: "articles/cryptographic_protocols/DES_CBC_INTRO.html"
alerts:
  - id: 1
    type: danger
    description: This is NOT the recommended mode of operation.
    link: ""
further-reading:

related-articles:

disadvantages:
  - name: ""
    description: 1. Parallel encryption is not possible since it is dependent on the previous ciphertext
    link: ""
  - name: ""
    description: 2. Error of transmission gets propagated due to the blovks getting changed
    link: ""
  - name: ""
    description: 3. Message needs to be padded to multiple cipher block sizes
    link: ""
  - name: ""
    description: 4. Decryption corrupts the first block
    link: ""

---
In this mode of operation, the first block is XORed with an initialization vector and the output is then encrypted using the key and the DES algorithm. In the case of DES, both initialization vector and the plaintext are 64 bits each.
This method as suggested by its name, is a block chaining method in a way that each time the plaintext is XORed with the previous ciphertext and then encrypted using the key and DES encryption method. This chaining continues till all the blocks are encrypted.
Similar steps are followed for the decryption and an initialization vector which is pre-decided is used at the start of the decryption process.
It has a good authentication mechanism and is better than DES ECB because it has an extra layer of security by using the previous ciphertext along with the key and the plaintext. It is also more resistant to cryptanalysis than ECB but is still a not recommended mode of operation.
