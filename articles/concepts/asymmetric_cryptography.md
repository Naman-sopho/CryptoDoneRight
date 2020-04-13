---
layout: page1
title: Asymmetric Cryptography
type: concepts
update: Last Updated Fri,  6 Dec 2019 04:01:43 +0000
permalink: /articles/concepts/asymmetric_cryptography.html
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

<br>
#### Digital Signatures

You can think of a digital signature similarly as a regular signature -- typically someone signs a document with their unique identity in order to "agree" (or validate, etc.) with the information contained in the document at the time of signing.

A digital signature is similar. It provides **integrity**, **authenticity**, and **non-repudiation**.

The steps in signature generation and verification are as follows:
1. The signer hashes the data she wants to sign.
2. She generates a signature with a signature algorithm using her _private_ key and the hash she generated.
3. The signer sends (or publishes, etc.) the data and the signature, as well as her _public_ key.
4. A verifier receives the data and the signature.
5. The verifier generates a hash of the data.
6. The verifier provides the signature verification algorithm with the signature she received as well as the sender's _public_ key, which produces the hash of the data that the signer originally signed.
7. The verifier can compare the hash she generated herself of the data she received with the hash that the signer signed to see if they are equal. If they are, the data has not been corrupted. If they aren't, the data that she received is not the same as the data that the signer signed.

* As we can see from the steps above, if the data has changed at all during transmission the hash will change (remember, small changes in the plaintext can cause major changes in the hash output). This property is how cryptographic signatures provide **integrity**.
* A little bit more nuanced from the steps above, cryptographic signatures also provide **authenticity**. By using a certain public key to verify the signature, you can be sure that the corresponding private key was used during signature generation.
* **Non-repudiation** is an interesting property that means that the signer cannot deny signing the message.

#### Key Agreement

TODO.

#### Asymmetric Encryption
TODO.
