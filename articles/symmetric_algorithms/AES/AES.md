---
layout: page
title: AES
type: symmetric_algorithms
update: Last Updated Thu, 12 Dec 2018 12:00:01 -0400
permalink: "articles/symmetric_algorithms/AES/AES.html"
alerts:
  - id: 1
    type: success
    description: AES is considered a strong symmetric encryption algorithm.
    link: ""
  - id: 2
    type: warning
    description: "AES, like all block ciphers, is not secure without an appropriate and correctly configured mode of operation."
    link: ""
further-reading:

related-articles:

warnings:
  - name: Never Use ECB.
    description: "Do NOT use the Electronic Code Book (ECB) mode of operation. This is only for testing!"
  - name: Do not Re-use Keys.
    description: "As with most symmetric ciphers, it is almost always wrong to re-use the same key for multiple encryption operations."
    
best_practices:
  - name: GCM Mode.
    description: "The GCM mode of operation (typically written AES-GCM) is almost always a very good choice. It both encrypts the data and protects it from modifications."

---
Advanced Encryption Standard, or AES, is a symmetric encryption algorithm. AES is also a block cipher, encrypting data in 128-bit chunks. As there are no known vulnerabilities against the AES cipher, it is considered safe to use so long as a proper mode of operation is chosen and is correctly configured. AES is a common choice to replace obsolete algorithms such as DES. AES is considered a reasonably efficient algorithm in terms of speed and memory requirements and is also a federal government standard in United States as approved by Secretary of Commerce.<br />
<br />
Like most modern symmetric ciphers, AES is often used for "bulk encryption", meaning the encryption and decryption of large amounts of data. Accordingly, AES is used in communication protocols such as TLS and IPSec for encrypting the network traffic, and is also found in file/folder/disk encryption applications as well. <br />
<br />
In terms of configuration, the proper use of AES requires selecting a mode of operation. 
TODO link to mode of operation reading. AES also must be configured with a key size, which can currently be 128 bits (16 bytes), 192 bits (24 bytes), or 256 bits (32 bytes). While 128-bit keys are still in use, 256 bit keys should be used when possible. Even though 128-bit keys are still strong enough, 256-bit keys will last longer against future improvements in computing power including quantum computing.
