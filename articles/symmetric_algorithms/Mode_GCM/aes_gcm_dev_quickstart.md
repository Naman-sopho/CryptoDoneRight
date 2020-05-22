---
layout: quickstart
title: "Developer's QuickStart"
type: AES-GCM
qtype: dev
upper-link: /articles/symmetric_algorithms/mode_gcm/mode_gcm.html
image: /static_files/common/NewDevLogo.png
note: "Are you a developer? Get started with crucial implementation details above."
col: col-md-4 col-sm-4 col-xs-4 infoBlocks
alerts:

further-reading:

related-articles:

attacks:
---
<p id="gcmintro">

  <h2> <img src="/static_files/common/configuration.jpg " style="width:110px;height:100px;" /> AES GCM Mode </h2>


<strong>Why GCM Mode:</strong> <br />
Considered a safe and efficient method of operation. It is a very popular choice for authenticated encryption <a href="https://crypto.stackexchange.com/questions/12178/why-should-i-use-authenticated-encryption-instead-of-just-encryption">MAC</a>.
There are no other advantages from a security standpoint (as long as all modes of operation are configured as per the best practice). <br /><br />

Additonal Reading: <a href="https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/"> Matthew Green: How to choose authenticated encryption? </a><br /><br />

<strong>How it works:</strong><br />
<ul>
 <li><a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">Galois/Counter Mode</a></li>
 <li><a href="https://crypto.stackexchange.com/questions/12178/why-should-i-use-authenticated-encryption-instead-of-just-encryption">Difference between AES CBC and GCM.</a>. </li>
</ul><br />

<strong>Where is it commonly used:</strong><br />
GCM is used in many of the SSL/TLS cipher suites. It has various other applications as listed on this <a href="https://en.wikipedia.org/wiki/AES_implementations#Python"> wiki page. </a><br /> <br />

<strong>How to use GCM: </strong>
<ul>
<li>aes-128-gcm← this is good!</li>
<li>aes-256-gcm  (with iv = 96bit,tag=128bit) ← this is good too!</li>
</ul>

<strong>How secure?</strong> <br /> <br />
<span class="red">GCM requires no padding. This is because CTR mode is also a part of GCM. </span> <br /> <br />
As a reminder, CTR mode is special in a few ways: <br /><br />

<ul>
<li> Padding doesn't apply and therefore eliminates all the padding attacks that were possible with modes like CCB where padding is required. . Normally, a block encryption algorithm (AES, Blowfish, DES, RC2, etc.) emit encrypted output that is a multiple of the block size (16 bytes for AES as an example). With CTR mode, the number of bytes output is exactly equal to the number of bytes input, so no padding/unpadding is required. The PaddingScheme property does not apply for counter mode.</li>

<li>CTR mode increments a counter for each subsequent block encrypted. For example, if an application encrypted the string "1234567890" twenty times in a row, using the same instance of the Chilkat Crypt2 object, then each iteration's result would be different. This is because the counter is being incremented. The decrypting application would need to decrypt in exactly the same manner. The 1st decrypt should begin with a new instance of a Crypt2 object so that it's counter is at the initial value of 0.</li>

Additionally, GCM mode provides authentication of the message without any additonal calculations.

</ul>

<br />
It would be a mistake to encrypt 20 strings using an instance of the Crypt2 object, and then attempt to decrypt with the same Crypt2 object. To decrypt successfully, the app would need to instantiate a new Crypt2 object and then decrypt, so that the counters match. <br /> <br />

<span class="green">Good points:</span>  Secure when done right, parallel encryption and decryption with authentication built in. <br />
<span class="red">Bad points:</span>  Not many. It is complicated to implement and can be catostrophical if not implemented correctly.

  <div class="col-md-12 col-sm-12 col-xs-12">

        <h2> <img src="/static_files/common/implementation.png " style="width:100px;height:100px;" /> AES Implementation</h2>

<font size="4"><strong>Concept:</strong></font>  DO NOT roll your own Crypto! Use standard services and libraries. <br />

It is NOT advisable in any circumstances to develop any sort of cryptography on your own. Instead , there are a few options for standard libraries that can be used.
These libraries offer better stability as they are usually a product of several years of experience in implementing cryptography by an active development community who are
dedicated towards efforts in implementation. It is therefore considered to be reliable and robust. <br /> <br />


<font size="3"><strong>Examples:</strong></font>
Openssl is one such library which popular and therefore is used as an example for this concept.
OpenSSL is not the only available crypto library. For a list of different libraries and a comparision
between them, visit <a href="https://en.wikipedia.org/wiki/Comparison_of_cryptography_libraries">here</a>.
<br /> <br />

The recommended version of OpenSSL is the latest 1.1.1. Some of them are additon the latest encryption standards and removal of older vulnerable ones.
<br /> <br />



<h2>Usage of Cryptography in Programming Languages</h2>

<font size="4"><strong>Concept:</strong></font> It is again advised to not roll out your own cryptography while developing software. There are popular libraries in almost all programming
languages that can readily be used to perform cryptographic operations.
<br /> <br />
<font size="4"><strong>Examples:</strong></font> <br />
<strong>Python: </strong> <br /><br />
There are multiple libraries that support AES in GCM mode. Some of them are:<br />
<ul>
  <li>PyCrypto – The Python Cryptography Toolkit PyCrypto, extended in PyCryptoDome</li>
<li>keyczar – Cryptography Toolkit keyczar</li>
<li>M2Crypto – M2Crypto is the most complete OpenSSL wrapper for Python.</li>
<li>Cryptography – Python library which exposes cryptographic recipes and primitives.</li>
<li>PyNaCl – Python binding for libSodium (NaCl)</li>
</ul>
<br />
Cryptography is a popular library and here is a basic example of how it works:
<code>
  <pre>
>>> import os
>>> from cryptography.hazmat.primitives.ciphers.aead import AESCCM
>>> data = b"a secret message"
>>> aad = b"authenticated but unencrypted data"
>>> key = AESCCM.generate_key(bit_length=128)
>>> aesccm = AESCCM(key)
>>> nonce = os.urandom(13)
>>> ct = aesccm.encrypt(nonce, data, aad)
>>> aesccm.decrypt(nonce, ct, aad)
b'a secret message'
</pre>
</code>

<a href="https://cryptography.io/en/latest/hazmat/primitives/aead/">Documentation</a><br /><br />


<strong>Java: </strong> <br />
Some of the popular libraries in Java:
<ul>
  <li>Java Cryptography Extension, integrated in the Java Runtime Environment since version 1.4.2</li>
  <li>IAIK JCE</li>
  <li>Bouncy Castle Crypto Library</li>
</ul>

An example from the Java Cryptographic Extensions:<br />
<code>
  <pre>
  SecretKey myKey = ...
  byte[] myAAD = ...
  byte[] plainText = ...
  int myTLen = ...
  byte[] myIv = ...

  GCMParameterSpec myParams = new GCMParameterSpec(myTLen, myIv);
  Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
  c.init(Cipher.ENCRYPT_MODE, myKey, myParams);

  // AAD is optional, if present, it must be supplied before any update/doFinal calls.
  c.updateAAD(myAAD);  // if AAD is non-null
  byte[] cipherText = new byte[c.getOutputSize(plainText.length)];
  // conclusion of encryption operation
  int actualOutputLen = c.doFinal(plainText, 0, plainText.length, cipherText);

  // To decrypt, same AAD and GCM parameters must be supplied
  c.init(Cipher.DECRYPT_MODE, myKey, myParams);
  c.updateAAD(myAAD);
  byte[] recoveredText = c.doFinal(cipherText, 0, actualOutputLen);

  // MUST CHANGE IV VALUE if the same key were to be used again for encryption
  byte[] newIv = ...;
  myParams = new GCMParameterSpec(myTLen, newIv);
</pre>
</code>
<a href="https://en.wikipedia.org/wiki/AES_implementations#Python"><strong>WIKI PAGE WITH OTHER LANGUAGES</strong></a><br /><br />
