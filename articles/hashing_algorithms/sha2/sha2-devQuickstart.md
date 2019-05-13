---
layout: quickstart
title: "Developer's QuickStart"
type: SHA2
image: /dev/static_files/NewDevLogo.png
note: "Are you a developer? Get started with crucial implementation details above."
col: col-md-4 col-sm-4 col-xs-4 infoBlocks
---

<p id="nocryptoroll">
  <div class="col-md-12 col-sm-12 col-xs-12">
<h2> <img src="/dev/static_files/implementation.png " style="width:150px;height:150px;" /> SHA2 Implementation</h2>	  

<p id="usagelibrary">
<h2>Usage of Cryptography in Programming Languages</h2>

<font size="4"><strong>Concept:</strong></font>  DO NOT roll your own Crypto! Use standard services and libraries. <br />

It is NOT advisable in any circumstances to develop any sort of cryptography on your own. Instead , there are a few options for standard libraries that can be used.
These libraries offer better stability as they are usually a product of several years of experience in implementing cryptography by an active development community who are
dedicated towards efforts in implementation. It is therefore considered to be reliable and robust. <br /> <br />

<font size="4"><strong>Examples:</strong></font> <br />
<strong>Python </strong> <br />
hashlib is a popular crypto library for Python that supports SHA2. We may want to hash data for multiple reasons ranging from public link creation to client verification. Let’s look at how we might go about this in Python:
<br /> <br />
<pre>
<code>
import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
</code>
</pre>
<br /><br />

Here we have a method that takes a string to be hashed and returns an encrypted hash. Conveniently, Python ships with a handy built-in dependency that does the majority of the heavy-lifting for us. We just have to be conscious of the format of the string we pass as it must be passed as a bytestring and, if it is not, we need to use the .encode() method to convert it to bytestring format. <br />

With a method like this in place, we should be able handle encryption with ease: <br /><br />

<pre>
<code>import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
hash_string = 'confidential data'
sha_signature = encrypt_string(hash_string)
print(sha_signature)
# 3fef7ff0fc1660c6bd319b3a8109fcb9f81985eabcbbf8958869ef03d605a9eb
</code>
</pre>
Above, you can see the encrypted hash returned by the SHA2 hashing method. <br />
<br /><br />

<strong>Java: </strong> <br />
Java provides a lot of libraries/classes for performing SHA2. Some of the popular examples are listed below:<br />
<ul>
<li>
Inbuilt MessageDigest class for SHA-256 hashing:

<pre>
<code>
MessageDigest digest = MessageDigest.getInstance("SHA-256");
byte[] encodedhash = digest.digest(
  originalString.getBytes(StandardCharsets.UTF_8));
  </code>
</pre>
  However, here we have to use a custom byte to hex converter to get the hashed value in hexadecimal:<br />

  <pre>
  <code>
  private static String bytesToHex(byte[] hash) {
    StringBuffer hexString = new StringBuffer();
    for (int i = 0; i < hash.length; i++) {
    String hex = Integer.toHexString(0xff & hash[i]);
    if(hex.length() == 1) hexString.append('0');
        hexString.append(hex);
    }
    return hexString.toString();
}
</code>
</pre>
</li>
<li>
Guava Library<br />
The Google Guava library also provides a utility class for hashing.<br /><br />

First, let’s define the dependency:<br />
<pre>
<code>
<dependency>
    <groupId>com.google.guava</groupId>
    <artifactId>guava</artifactId>
    <version>20.0</version>
</dependency>
</code>
</pre>
Now, here’s how we can use Guava to hash a String: <br />

<pre>
<code>
String sha256hex = Hashing.sha256()
  .hashString(originalString, StandardCharsets.UTF_8)
  .toString();
</code>
</pre>
Here’s the utility class – called DigestUtils – that supports SHA-256 hashing:<br />
<pre>
<code>
String sha256hex = DigestUtils.sha256Hex(originalString);
</code>
</pre>
</li><br />

<li>
Apache Commons Codecs<br /><br />
Similarly, we can also use Apache Commons Codecs as well:<br />
<pre>
<code>
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
    <version>1.10</version>
</dependency>
</code>
</pre>
Here’s the utility class – called DigestUtils – that supports SHA-256 hashing:<br />

<pre>
<code>
String sha256hex = DigestUtils.sha256Hex(originalString);
</code>
</pre>
</li>
</ul>

<strong>C++:</strong> <br />
For example to prove that "Rosetta code" translates to 764faf5c61ac315f1497f9dfa542713965b785e5cc2f707d6468d7d1124cdfcf after hashing with SHA2:<br />

<pre>
  <code>

  Uses crypto++. Compile it with -lcryptopp

int main(int argc, char argv){
    CryptoPP::SHA256 hash;
    std::string digest;
    std::string message = "Rosetta code";
    CryptoPP::StringSource s(message, true,
      	new CryptoPP::HashFilter(hash,
      		new CryptoPP::HexEncoder(
      			new CryptoPP::StringSink(digest))));
    std::cout << digest << std::endl;
    return 0;
}



  </code>
</pre>
</p><br/>

<font size="4"><strong>How to Hash Properly: Hashing with Salt:</strong></font> <br />

Salt should be generated using a Cryptographically Secure Pseudo-Random Number Generator (CSPRNG). CSPRNGs are very different than ordinary pseudo-random number generators, like the "C" language's rand() function. As the name suggests, CSPRNGs are designed to be cryptographically secure, meaning they provide a high level of randomness and are completely unpredictable. We don't want our salts to be predictable, so we must use a CSPRNG. The following table lists some CSPRNGs that exist for some popular programming platforms.<br />

<img src="/dev/static_files/CSPRNG.JPG" style="width:600px;height:500px;" /><br />

<strong>In a Web Application, always hash on the server</strong><br />
If you are writing a web application, you might wonder where to hash. Should the password be hashed in the user's browser with JavaScript, or should it be sent to the server "in the clear" and hashed there?<br />

Even if you are hashing the user's passwords in JavaScript, you still have to hash the hashes on the server. Consider a website that hashes users' passwords in the user's browser without hashing the hashes on the server. To authenticate a user, this website will accept a hash from the browser and check if that hash exactly matches the one in the database. This seems more secure than just hashing on the server, since the users' passwords are never sent to the server, but it's not.<br />

The problem is that the client-side hash logically becomes the user's password. All the user needs to do to authenticate is tell the server the hash of their password. If a bad guy got a user's hash they could use it to authenticate to the server, without knowing the user's password! So, if the bad guy somehow steals the database of hashes from this hypothetical website, they'll have immediate access to everyone's accounts without having to guess any passwords.<br />

This isn't to say that you shouldn't hash in the browser, but if you do, you absolutely have to hash on the server too. Hashing in the browser is certainly a good idea, but consider the following points for your implementation:<br />

Client-side password hashing is not a substitute for HTTPS (SSL/TLS). If the connection between the browser and the server is insecure, a man-in-the-middle can modify the JavaScript code as it is downloaded to remove the hashing functionality and get the user's password.<br />

Some web browsers don't support JavaScript, and some users disable JavaScript in their browser. So for maximum compatibility, your app should detect whether or not the browser supports JavaScript and emulate the client-side hash on the server if it doesn't.<br />

You need to salt the client-side hashes too. The obvious solution is to make the client-side script ask the server for the user's salt. Don't do that, because it lets the bad guys check if a username is valid without knowing the password. Since you're hashing and salting (with a good salt) on the server too, it's OK to use the username (or email) concatenated with a site-specific string (e.g. domain name) as the client-side salt.<br />
[https://crackstation.net/hashing-security.htm]	<br />
<p id="tls12patch">
<h2> <img src="/dev/static_files/patch.png " style="width:100px;height:100px;" /> Upgrade/Patch Management </h2>

<font size="4"><strong>Concept:</strong></font> <span class="red">Please be careful while upgrading your crypto library. Do not simply upgrade the package without thinking about the implications it might have on existing features of your application or operating system. </span>
<br />
A lot of application and Operating System vendors provide specific guidelines on how to upgrade your software. A lot of vendors perform extensive testing of new releases of
libraries like OpenSSL to ensure that no existing functionality is affected. Usually, these vendors release their own updates called <u>backported packages</u>. The security team
backports security fixes to the released code versions, so while you will not get new features you can be reasonably sure that your SSL libraries are up to date.
</p>
