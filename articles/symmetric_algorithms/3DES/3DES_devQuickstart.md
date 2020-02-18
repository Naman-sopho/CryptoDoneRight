---
layout: quickstart
title: "Developer's QuickStart"
type: 3DES
qtype: dev
url: /quickstarts/dev/3DES
image: /static_files/common/NewDevLogo.png
note: "Are you a developer? Get started with crucial implementation details above."
col: col-md-4 col-sm-4 col-xs-4 infoBlocks
alerts:
  - id: 1
    type: warning
    description: "Background Reading: Understanding Different Types of Problems in Crypto."
    link: "/flaw-categories.html"
  - id: 2
    type: danger
    description: This is the NOT the recommended standard.
    link: /articles/cryptographic_protocols/AES.html
  - id: 3
    type: danger
    description: There are serious security implications if not configured properly!
    link: ""
further-reading:

related-articles:

attacks:


---
<p id="nocryptoroll">
<h2> <img src="/static_files/common/implementation.png " style="width:100px;height:100px;" /> 3DES Implementation</h2>
<font size="4"><strong>Concept:</strong></font>  DO NOT roll your own Crypto! Use standard services and libraries. <br />
It is NOT advisable in any circumstances to develop any sort of cryptography on your own. Instead , there are a few options for standard libraries that can be used.
These libraries offer better stability as they are usually a product of several years of experience in implementing cryptography by an active development community who are
dedicated towards efforts in implementation. It is therefore considered to be reliable and robust. <br /> <br />
<font size="3"><strong>Examples:</strong></font>
Openssl is one such library which popular and therefore is used as an example for this concept.
OpenSSL is not the only available crypto library. For a list of different libraries and a comparision
between them, visit <a href="https://en.wikipedia.org/wiki/Comparison_of_cryptography_libraries">here</a>.
<br /> <br />
Find out which openssl version you are using: <br /> <br />
Use the version option. <br />
<pre>
  <code>
$ openssl version
OpenSSL 1.0.1e-fips 11 Feb 2013
</code>
</pre>
<br />
You can get much more information with the version -a option. <br />
<pre>
  <code>
$ openssl version -a
OpenSSL 1.0.1e-fips 11 Feb 2013
built on: Thu Jul 23 19:06:35 UTC 2015
platform: linux-x86_64
options:  bn(64,64) md2(int) rc4(16x,int) des(idx,cisc,16,int)
          idea(int) blowfish(idx)
compiler: gcc -fPIC -DOPENSSL_PIC -DZLIB -DOPENSSL_THREADS -D_REENTRANT
-DDSO_DLFCN -DHAVE_DLFCN_H -DKRB5_MIT -m64 -DL_ENDIAN -DTERMIO
-Wall -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions
-fstack-protector --param=ssp-buffer-size=4 -m64 -mtune=generic
-Wa,--noexecstack -DPURIFY -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT
-DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM
-DSHA512_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM
-DWHIRLPOOL_ASM -DGHASH_ASM
OPENSSLDIR: "/etc/pki/tls"
engines:  rdrand dynamic
 </code>
</pre>
<br /> <br />
<span class="red">Please note that OpenSSL 1.0.2k has removed 3DES support. There are still ways you can re-enable 3DES (<a href="https://www.openssl.org/blog/blog/2016/08/24/sweet32/">Re-enable 3DES</a>), but considering the security implications, this should be done only if absolutely necessary. </span>
</p>


<p id="usagelibrary">
<h2>Usage of Cryptography in Programming Languages</h2>
<font size="4"><strong>Concept:</strong></font> It is again advised to not roll out your own cryptography while developing software. There are popular libraries in almost all programming
languages that can readily be used to perform cryptographic operations.
<br /> <br />
<font size="4"><strong>Examples:</strong></font> <br />
<strong>C/C++: </strong> <br />
There are multiple options for libraries that support 3DES in C/C++.  <br /> <br />
Using OpenSSL: <a href="http://www.firmcodes.com/triple-des-cbc-mode-encryption-example-c-programming-openssl/">http://www.firmcodes.com/triple-des-cbc-mode-encryption-example-c-programming-openssl/ </a><br />
Using Crypto++ Library: <a href="https://www.cryptopp.com/wiki/TripleDES">https://www.cryptopp.com/wiki/TripleDES</a><br />
</p>
