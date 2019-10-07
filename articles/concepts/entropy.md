---
layout: page1
title: Entropy
type: concepts
update: Last Updated Mon, 7 Oct 2019 21:27:01 -0400
permalink: "articles/concepts/entropy.html"
alerts:

further-reading:

related-articles:

best_practices:
  - name: Use a hardware random number generator.
  - name: Test your Entropy
    description: NIST SP800-90B provides assessment tools.


---

In cryptography, entropy is the measure of randomness. Random values are very important in cryptography because we want to make our keys and encrypted messages difficult to attack. For example, keys should be hard to guess and messages should be hard to distinguish between.

Random values are used in many tasks in cryptography, including key generation, nonces and initialization vectors, padding schemes, digital signatures, etc.

#### Where does entropy come from?

Some typical sources of entropy in a system include keyboard strokes or mouse movements, system time, clock cycles, /proc PIDs, /dev names, interrupts, drivers info, and disk requests.
