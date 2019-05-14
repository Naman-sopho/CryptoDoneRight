---
layout: page
title: AES-GCM
type: cryptographic_protocols
update: Last Updated Thu, 12 Dev 2018 12:00:01 -0400
permalink: "articles/cryptographic_protocols/AES-GCM.html"
alerts:
  - id: 1
    type: success
    description: This is currently one of the two recommended modes of operation.
    link: ""
further-reading:

related-articles:

attacks:
---
GCM mode stands for Galois/Counter mode. GCM operates quite differently from CTR or CBC modes. GCM combines the mathematical properties of Galois field multiplication with the counter mode of operation for block ciphers. AES GCM has been designed to work in parallel (just like CTR mode) and is therefore fast and its security has been proven. . A safe length of key size for AES in GCM mode is only a 128bit key as compared to AES-CBC mode which typically requires a 256bit key.

Additionally, AES-GCM incorporates the authentication checks for datainto the cipher natively. This would have to be generated using a mechanicsm such as a MAC.
