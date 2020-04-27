---
layout: quickstart
title: "Developer's QuickStart"
type: RSA
qtype: dev
upper-link: /articles/asymmetric_algorithms/rsa/rsa.html
image: /static_files/common/NewDevLogo.png
note: "Are you a developer? Get started with crucial implementation details above."
col: col-md-4 col-sm-4 col-xs-4 infoBlocks
alerts:

further-reading:

related-articles:

attacks:


---
<h2> <img src="/static_files/common/implementation.png " style="width:100px;height:100px;" /> RSA for Developers</h2>

<font size="4"><strong>Concept:</strong></font>  DO NOT roll your own Crypto! Use standard services and libraries. <br />

It is NOT advisable in any circumstances to develop any sort of cryptography on your own. Instead , there are a few options for standard libraries that can be used.
These libraries offer better stability as they are usually a product of several years of experience in implementing cryptography by an active development community who are
dedicated towards efforts in implementation. It is therefore considered to be reliable and robust. <br /> <br />

<h3>OpenSSL</h3>
OpenSSL is one such library which popular and therefore is used as an example for this concept.
OpenSSL is not the only available crypto library. For a list of different libraries and a comparison
between them, visit <a href="https://en.wikipedia.org/wiki/Comparison_of_cryptography_libraries">here</a>.
<br /> <br />

It is advisable to use the most up-to-date versions of software libraries to ensure that old vulnerabilities are taken care of.
<br />

<h4>Command line RSA key generation with OpenSSL</h4>
The OpenSSL key generation utility for the command line generates a _key pair_ in PEM format, so the _public_ key will need to be extracted into its own file without the secret information:
(Note that for clarity, filenames should end in _.pem_)
<br><br><code>openssl genrsa -out KEYPAIR_FILENAME 2048</code>
<br><code>openssl rsa -in KEYPAIR_FILENAME -outform PEM -pubout -out PUBLIC_KEY_FILENAME</code>

<h4>Command line signature generation and verification with RSA keys using OpenSSL</h4>
The OpenSSL signature utility for the command line allows you to specify which hash algorithm you'd like to use. It is recommended to use SHA256 or greater. MD5 and SHA1 are not advisable (see [here](https://eprint.iacr.org/2020/014) for a 2020 paper about SHA1 pre-image generation):
<br><br>
To sign:<br><code>openssl dgst -sha256 -sign PRIVATE_KEY_FILENAME -out SIGNATURE_FILENAME DATA_TO_SIGN_FILENAME</code>
<br><br>
To verify:<br>
<code>openssl dgst -sha256 -verify PUBLIC_KEY_FILENAME -signature SIGNATURE_FILENAME DATA_TO_VERIFY_FILENAME</code>
<br>If everything verifies successfully, you will see the following output:<br><code>Verified OK</code><br>

<h4>C library RSA key generation with OpenSSL</h4>
The OpenSSL library provides various APIs for cryptographic mechanisms. It can be difficult to figure out exactly how to achieve your end goal.

This key generation example is from a stackoverflow question that can be found [here](https://stackoverflow.com/a/6231683):
<br>
<pre>
<code class="c">
#include <openssl/rsa.h>
#include <openssl/pem.h>

const int kBits = 1024;
const int kExp = 3;

int keylen;
char *pem_key;

RSA *rsa = RSA_generate_key(kBits, kExp, 0, 0);

/* To get the C-string PEM form: */
BIO *bio = BIO_new(BIO_s_mem());
PEM_write_bio_RSAPrivateKey(bio, rsa, NULL, NULL, 0, NULL, NULL);

keylen = BIO_pending(bio);
pem_key = calloc(keylen+1, 1); /* Null-terminate */
BIO_read(bio, pem_key, keylen);

printf("%s", pem_key);

BIO_free_all(bio);
RSA_free(rsa);
free(pem_key);
</code>
</pre>

<br>
<h4>C library signature generation and verification with RSA keys using OpenSSL</h4>
MD5 and SHA1 are not advisable (see [here](https://eprint.iacr.org/2020/014) for a 2020 paper about SHA1 pre-image generation):
<br>
<br>
##### To sign: (example from OpenSSL wiki)
<pre>
<code class="c">
EVP_MD_CTX *mdctx = NULL;
int ret = 0;

*sig = NULL;

/* Create the Message Digest Context */
if(!(mdctx = EVP_MD_CTX_create())) goto err;

/* Initialise the DigestSign operation - SHA-256 has been selected as the message digest function in this example */
 if(1 != EVP_DigestSignInit(mdctx, NULL, EVP_sha256(), NULL, key)) goto err;

 /* Call update with the message */
 if(1 != EVP_DigestSignUpdate(mdctx, msg, strlen(msg))) goto err;

 /* Finalise the DigestSign operation */
 /* First call EVP_DigestSignFinal with a NULL sig parameter to obtain the length of the
  * signature. Length is returned in slen */
 if(1 != EVP_DigestSignFinal(mdctx, NULL, slen)) goto err;
 /* Allocate memory for the signature based on size in slen */
 if(!(*sig = OPENSSL_malloc(sizeof(unsigned char) * (*slen)))) goto err;
 /* Obtain the signature */
 if(1 != EVP_DigestSignFinal(mdctx, *sig, slen)) goto err;

 /* Success */
 ret = 1;

 err:
 if(ret != 1)
 {
   /* Do some error handling */
 }

 /* Clean up */
 if(*sig && !ret) OPENSSL_free(*sig);
 if(mdctx) EVP_MD_CTX_destroy(mdctx);
 </code></pre>

##### To verify: (example from OpenSSL wiki)
 <pre>
 <code class="c">
 /* Initialize `key` with a public key */
 if(1 != EVP_DigestVerifyInit(mdctx, NULL, EVP_sha256(), NULL, key)) goto err;

 /* Initialize `key` with a public key */
 if(1 != EVP_DigestVerifyUpdate(mdctx, msg, strlen(msg))) goto err;

 if(1 == EVP_DigestVerifyFinal(mdctx, sig, slen))
 {
     /* Success */
 }
 else
 {
     /* Failure */
 }
 </code>
 </pre>
