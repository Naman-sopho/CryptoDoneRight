---
layout: quickstart
title: "Developer's QuickStart"
type: SHA1
qtype: dev
upper-link: /articles/hashing_algorithms/sha1.html
image: /static_files/common/NewDevLogo.png
note: "Are you a developer? Get started with crucial implementation details above."
col: col-md-4 col-sm-4 col-xs-4 infoBlocks
further-reading:
  - name: History of Hash Functions
    link: https://www.esat.kuleuven.be/cosic/publications/article-1532.pdf
  - name: Comparative Study Between MD5 and SHA-1
    link: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.659.1400&rep=rep1&type=pdf
  - name: Comparisons between the different SHAs
    link: https://en.wikipedia.org/wiki/Secure_Hash_Algorithms
---

<p id="where">
          <strong>Protocols Used In:</strong>
            <ul>
              <li>Transport Layer Security (TLS)</li>
              <li>Secure Sockets Layer (SSL)</li>
              <li>Pretty Good Privacy (PGP)</li>
              <li>Secure Shell (SSH)</li>
              <li>Secure/Multipurpose Internet Mail Extensions (S/MIME)</li>
              <li>Internet Protocol Security (IPSec)</li>
            </ul>
          </p>
<p id="whenToUse">
<strong>When and Where is SHA-1 Ok?</strong>
Checking the hash of an executable or file that we know is trusted (from trusted site).
No known flaws in SHA-1 as a key derivation function which is how dh-group14-sha1 is being used.  
Similarly, HMAC-SHA1 is believed to be (still) safe as long as SHA1 is pseudorandom.   
The specific construct of HMAC-SHA1 is still considered safe to use (assuming a secret key) due to the security proof for HMAC which does not rely on collision resistance of the underlying PRF.
</p>

<p>
<strong>Simple Basic issues when doing web development and having or storing passwords using SHA-1.</strong><br />
If you're a web developer, you've probably had to make a user account system. The most important aspect of a user account system is how user passwords are protected. User account databases are hacked frequently, so you absolutely must do something to protect your users' passwords if your website is ever breached. The best way to protect passwords is to employ salted password hashing. This page will explain why it's done the way it is.
 </p>

<p>
The general workflow for account registration and authentication in a hash-based account system is as follows:
<ol>
<li>
The user creates an account.</li>
<li>
Their password is hashed and stored in the database. At no point is the plain-text (unencrypted) password ever written to the hard drive. </li>
<li>
When the user attempts to login, the hash of the password they entered is checked against the hash of their real password (retrieved from the database).
</li>
<li>
If the hashes match, the user is granted access. If not, the user is told they entered invalid login credentials.</li>
</ol>
Steps 3 and 4 repeat every time someone tries to login to their account.<br />
Refer to <a href="example_index.html">Hashing page</a> for known Attacks on Hashes.
</p>
<p id="c">
<strong>Basic Implementation of SHA-1</strong><br />
This is primarily for possible legacy device support. Ensure that this is done for less secure systems, and use stronger hashing for more secure systems.
</p>
<p>
<strong>In C/C++</strong>
<h3>(1)</h3>
<pre>
<code>
#include <openssl/sha.h>
int main()
{  
  const char str[] = "Original String";
  unsigned char hash[SHA_DIGEST_LENGTH]; // == 20
  SHA1(str, sizeof(str) - 1, hash);
  // do some stuff with the hash
  return 0;
}</code>
</pre>
</p>
<p>
OpenSSL crypto library: <a href="https://www.openssl.org/docs/manmaster/man1/sha1.html"> https://www.openssl.org/docs/manmaster/man1/sha1.html</a>
<br />
Man page: <a href="https://www.openssl.org/docs/manmaster/crypto/sha.html">https://www.openssl.org/docs/manmaster/crypto/sha.html</a>
</p>
<p>
CryptoPP is a great C++ library for cryptographic functions. It has a method for calculating a SHA1 digest. See examples of the hashing functions here. http://www.cryptopp.com/wiki/Hash_Functions</p>
<p>
Libcrypt: <a href="http://www.gnupg.org/documentation/manuals/gcrypt/Available-hash-algorithms.html#Available-hash-algorithms">http://www.gnupg.org/documentation/manuals/gcrypt/Available-hash-algorithms.html#Available-hash-algorithms</a>
</p>
<p>
Another opensource library - Boost: <a href="http://www.boost.org/doc/libs/1_46_0/libs/uuid/index.html">http://www.boost.org/doc/libs/1_46_0/libs/uuid/index.html</a></p>
<p>

<h3>(2)</h3>
<pre>
<code>
// The data to be hashed
char data[] = "Hello, world!";
size_t length = sizeof(data);
unsigned char hash[SHA_DIGEST_LENGTH];
SHA1(data, length, hash);
// hash now contains the 20-byte SHA-1 hash
++While using between packets in C:
// Error checking omitted for expository purposes
// Object to hold the current state of the hash
SHA_CTX ctx;
SHA1_Init(&ctx);
// Hash each piece of data as it comes in:
SHA1_Update(&ctx, "Hello, ", 7);
...
SHA1_Update(&ctx, "world!", 6);
// etc.
...
// When you're done with the data, finalize it:
unsigned char hash[SHA_DIGEST_LENGTH];
SHA1_Final(hash, &ctx);
</code>
</pre>
</p>


<h3>(3)</h3>
<p>
<pre>
<code>
#include <openssl/sha.h>   
int main(int argn, char *argv[]) {  
    int i = 0;
    unsigned char temp[SHA_DIGEST_LENGTH];
    char buf[SHA_DIGEST_LENGTH*2];
    if ( argn != 2 ) {
    printf("Usage: %s string\n", argv[0]);
    return -1;
    }
    memset(buf, 0x0, SHA_DIGEST_LENGTH*2);
    memset(temp, 0x0, SHA_DIGEST_LENGTH);
    SHA1((unsigned char *)argv[1], strlen(argv[1]), temp);
    for (i=0; i < SHA_DIGEST_LENGTH; i++) {
    sprintf((char*)&(buf[i*2]), "%02x", temp[i]);
    }
    printf("SHA1 of %s is %s\n", argv[1], buf);
    return 0;
    }
</code>
</pre>
</p>

<p>
<strong>Compiling:</strong><br />
<pre>
<code>
$ gcc sha.c -lssl -o sha
$ ./sha asd
SHA1 of asd is f10e2821bbbea527ea02200352313bc059445190</code>
</pre>
</p>

<p id="python">
<strong>In Python:</strong>
<pre>
<code>
import hashlib
hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

import uuid
import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')</code>
</pre>
</p>
