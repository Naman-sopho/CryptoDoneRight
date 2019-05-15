---
layout: quickstart
title: "Developer's QuickStart"
type: AES-CBC
image: /static_files/NewDevLogo.png
note: "Are you a developer? Get started with crucial implementation details above."
col: col-md-4 col-sm-4 col-xs-4 infoBlocks
alerts:
  - id: 1
    type: warning
    description: "Background Reading: Understanding Different Types of Problems in Crypto."
    link: ""

further-reading:

related-articles:

attacks:
---
<p id="cbcintro">

  <h2> <img src="/static_files/configuration.jpg " style="width:110px;height:100px;" /> AES CBC Introduction </h2>

<strong>How it works:</strong><br />
Each block of plaintext is xor'ed with the previous block of ciphertext before being transformed, ensuring that identical plaintext blocks don't result in identical ciphertext blocks when in sequence. For the first block of plaintext (which doesn't have a preceding block) we use an initialization vector instead. This value should be unique per message per key, to ensure that identical messages don't result in identical ciphertexts.  <br /> <br />

<strong>Where is it commonly used:</strong><br />
CBC is used in many of the SSL/TLS cipher suites. <br /> <br />

<strong>Why CBC Mode?</strong><br />
CBC - Cipher Block Chaining. This mode is very common, and is considered to be reasonably secure.  <br /> <br />

<strong>How secure?</strong><br />
Unfortunately, there are attacks against CBC when it is not implemented alongside a set of strong integrity and authenticity checks. One property it has is block-level malleability, which means that an attacker can alter the plaintext of the message in a meaningful way without knowing the key, if he can mess with the ciphertext. As such, implementations usually include a HMAC-based authenticity record. But we are going to save that for a later post. <br /> <br />

<strong>How to use it securely:</strong><br />
<ul>
<li>Ensure you are using a randomized IV that is not re-used.</li>
<li>Use PKCS7 padding: Normally, a block encryption algorithm (AES, Blowfish, DES, RC2, etc.) emit encrypted output that is a multiple of the block size (16 bytes for AES as an example). This is only required in CBC mode. In CTR mode, the number of bytes output is exactly equal to the number of bytes input, so no padding/unpadding is required.</li>
<li>For all the recommendations, please follow the FAQ page on the landing page. </li>
</ul>

<strong>What to use:</strong><br />
These are the most commonly available options: <br /> <br />

aes-128-cbc ← this is okay <br />
aes-192-cbc <br />
aes-256-cbc ← this is recommended <br /> <br />

<span class="green">Good points:</span>  Secure when used properly, parallel decryption. <br />
<span class="red">Bad points:</span>  No parallel encryption, susceptible to malleability attacks when authenticity checks are bad / missing. But when done right, it's very good.

</p>

<p id="nocryptoroll">
  <div class="col-md-12 col-sm-12 col-xs-12">

        <h2> <img src=/static_files/implementation.png " style="width:100px;height:100px;" /> AES Implementation</h2>

<font size="4"><strong>Concept:</strong></font>  DO NOT roll your own Crypto! Use standard services and libraries. <br />

It is NOT advisable in any circumstances to develop any sort of cryptography on your own. Instead , there are a few options for standard libraries that can be used.
These libraries offer better stability as they are usually a product of several years of experience in implementing cryptography by an active development community who are
dedicated towards efforts in implementation. It is therefore considered to be reliable and robust. <br /> <br />


<font size="3"><strong>Examples:</strong></font>
Openssl is one such library which popular and therefore is used as an example for this concept.
OpenSSL is not the only available crypto library. For a list of different libraries and a comparision
between them, visit <a href="https://en.wikipedia.org/wiki/Comparison_of_cryptography_libraries">here</a>.
<br /> <br />

The recommended version of OpenSSL that is to be used for AES is 1.1.0. This is for various reasons that concern and do not concern with AES. Some of them include for the latest encryption standards and removal of older vulnerable ones.
<br /> <br />
To use openssl: <br /> <br />

Encryption:
<pre>
  <code>
openssl aes-256-cbc -in attack-plan.txt -out message.enc
</code>
</pre>
Decryption:
<pre>
  <code>
openssl aes-256-cbc -d -in message.enc -out plain-text.txt
  </code>
</pre>
You can get openssl to base64-encode the message by using the -a switch on both encryption and decryption. This way, you can paste the ciphertext in an email message, for example. It'll look like this:
<pre>
  <code>
stefano:~$ openssl aes-256-cbc -in attack-plan.txt -a
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
U2FsdGVkX192dXI7yHGs/4Ed+xEC3ejXFINKO6Hufnc=
  </code>
</pre>
Note: OpenSSL uses PKCS7 by default for padding.

</p>


<p id="usagelibrary">
<h2>Usage of Cryptography in Programming Languages</h2>

<font size="4"><strong>Concept:</strong></font> It is again advised to not roll out your own cryptography while developing software. There are popular libraries in almost all programming
languages that can readily be used to perform cryptographic operations.
<br /> <br />
<font size="4"><strong>Examples:</strong></font> <br />
<strong>PHP: </strong> <br />
Examples of encryption and decryption  using AES in PHP: <br /> <br />

<a href="https://askubuntu.com/questions/60712/how-do-i-quickly-encrypt-a-file-with-aes">https://askubuntu.com/questions/60712/how-do-i-quickly-encrypt-a-file-with-aes </a>
<br /> <br />

<strong>Java: </strong> <br />
<span class="green">AES Encryption in Java</span> <br /> <br />

Following is the sample program in Java that performs AES encryption. Here, we are using AES with CBC mode to encrypt a message as ECB mode is not semantically secure.The IV (what is an IV? <!--LINK HERE-->) mode should also be randomized for CBC mode. And the mode of padding is PKCS7. <!--WHAT and WHY PKCS7--> <br /> <br />

If the same key is used to encrypt all the plain text and if an attacker finds this key then all the cipher can be decrypted in the similar way.We can use salt and iterations to improve the encryption process further.In the following example we are using 128 bit encryption key. An <br /> <br />

Example:
<pre>
  <code>
private static final String key = "aesEncryptionKey";
private static final String initVector = "encryptionIntVec";

public static String encrypt(String value) {
               try {
                              IvParameterSpec iv = new IvParameterSpec(initVector.getBytes("UTF-8"));
                              SecretKeySpec skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES");

                              Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
                              cipher.init(Cipher.ENCRYPT_MODE, skeySpec, iv);

                              byte[] encrypted = cipher.doFinal(value.getBytes());
                              return Base64.encodeBase64String(encrypted);
               } catch (Exception ex) {
                              ex.printStackTrace();
               }
               return null;
}
</code>
</pre>

<br /> <br />

<span class="red">AES Decryption in Java</span> <br /> <br />

Following is the reverse process to decrypt the cipher.The code is self explanatory. <br /> <br />

<pre>
  <code>

public static String decrypt(String encrypted) {
               try {
                              IvParameterSpec iv = new IvParameterSpec(initVector.getBytes("UTF-8"));
                              SecretKeySpec skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES");

                              Cipher cipher = Cipher.getInstance("AES/CBC/PKCS7PADDING");
                              cipher.init(Cipher.DECRYPT_MODE, skeySpec, iv);
                              byte[] original = cipher.doFinal(Base64.decodeBase64(encrypted));

                              return new String(original);
               } catch (Exception ex) {
                              ex.printStackTrace();
               }

               return null;
}

Testing AES Encryption and Decryption

Following is the main() implementation to test our AES implementation.

public static void main(String[] args) {
               String originalString = "password";
               System.out.println("Original String to encrypt - " + originalString);
               String encryptedString = encrypt(originalString);
               System.out.println("Encrypted String - " + encryptedString);
               String decryptedString = decrypt(encryptedString);
               System.out.println("After decryption - " + decryptedString);
}
</code>
</pre></p>
