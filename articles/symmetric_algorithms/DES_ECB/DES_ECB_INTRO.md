---
layout: page
title: DES ECB
type: symmetric_algorithms
update: Last Updated Fri, 3 May 2019 15:34:00 -0400
permalink: "articles/cryptographic_protocols/DES_ECB_INTRO.html"
alerts:
  - id: 1
    type: danger
    description: This is NOT the recommended mode of operation.
    link: ""
further-reading:

related-articles:

attacks:
  - name: ""
    description: 1. Replay Attacks
    link: ""
  - name: ""
    description: 2. Trial and Error
    link: ""
  - name: ""
    description: 3. Brute Force Attacks
    link: ""
  - name: ""
    description: 4. Cryptanalysis since there is a direct relationship between plaintext and ciphertext
    link: ""
  - name: ""
    description: 5. Insertion of encoded blocks is possibleanalysis called ‘differential-linear’ cryptanalysis can also break DES depending on how many rounds
    link: ""

---
It is the simplest mode of operation. The message is simply divided into blocks and each block is then encrypted separately. It offers a direct encryption scheme because it makes it easier to encrypt each block. It is a deterministic mode of encryption because if the same key is used for two blocks, the ciphertext for both these blocks would be the same.
in DES, a plaintext datablock is directly used as a DES input block. The plaintext and the encrypted ciphertext are all 64 bit in case of DES. It is easier to guess the plaintext in this mode of encryption and this is not at all a recommended mode of operation.
