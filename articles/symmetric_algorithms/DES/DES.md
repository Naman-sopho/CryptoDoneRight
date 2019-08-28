---
layout: page
title: DES
type: symmetric_algorithms
update: Last Updated Fri, 3 May 2019 15:13:00 -0400
permalink: "articles/cryptographic_protocols/DES.html"
alerts:
  - id: 1
    type: danger
    description: THIS IS BAD! IT IS DANGEROUS. DON'T USE IT!
    link: ""
  - id: 2
    type: danger
    description: This is the NOT the recommended standard.
    link: ""
further-reading:

related-articles:

attacks:
  - name: ""
    description: 1. Brute Force attacks are common since the key length is mall for DES (64 bits).
    link: ""
  - name: ""
    description: 2. Differential Cryptanalysis can break full 16-round DES by using 247 chosen plaintext.
    link: ""
  - name: ""
    description: 3. A man-in-the-middle attack requires complexity of 232 to break 6-round DES.
    link: ""
  - name: ""
    description: 4. Linear cryptanalysis can break DES using 243 known plaintext
    link: ""
  - name: ""
    description: 5. A combination of linear and differential cryptanalysis called ‘differential-linear’ cryptanalysis can also break DES depending on how many rounds
    link: ""
  - name: ""
    description: 6. Davies Attack (DA) can break DES with 250 known plaintext.
    link: ""

---
The Data Encryption Standard, or DES for short, is a symmetric-key block cipher designed by IBM and published by the National Institute of Standards and Technology (NIST). The plaintext is broken into blocks of 64-bits and encryption is performed block-wise. This means that the cryptographic key and the algorithm are applied to it together rather than one bit at a time. The encryption process consists of 16 rounds and each block is encrypted using a key to a cipher-text (64-bits) by using permutations and combinations. They key used in DES has 56-bits as a functional key while the rest 8 bits are for parity checking.

DES was actually the first encryption algorithm approved by the US government for public disclosure. It is now insecure due to its small key size -- it is vulnerable to a brute force attack.
