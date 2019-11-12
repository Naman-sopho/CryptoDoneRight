---
layout: page1
title: Asymmetric Cryptography
type: concepts
update: Last Updated Sat, 17 Aug 2019 21:27:01 -0400
permalink: "articles/concepts/asymmetric_cryptography.html"
alerts:

further-reading:

related-articles:

warnings:
  - name: Keep Private Keys Private.
    description: The security of asymmetric cryptography is based on the private key never being disclosed. They must be secured and protected with the greatest care.

best_practices:

---

#### Introduction

Asymmetric cryptography is a powerful tool (when used correctly!) that is essential to much of the security of the Internet. Within this family of techniques, the algorithms and the functionality they provide can differ greatly. But the characteristic they all have in common is _key-pairs_. That is, for each of these algorithms, there are two keys: a _public_ key and a _private_ key. For this reason, these approaches are also called "public key cryptography."

In asymmetric operations, a party generates the key pair and (should) keep the private key confidential. Under almost every circumstance conceivable, the private key should not be disclosed. This is different from symmetric cryptography wherein two parties must share the key.

On the other hand, the party with the private key can distribute the public key to any party she chooses. Exactly what can be done with the key-pair depends on the algorithm. Common operations include:

* Digital Signatures
* Key Agreement
* Asymmetric Encryption

#### Digital Signatures

TODO.

#### Key Agreement

TODO.

#### Asymmetric Encryption
TODO.
