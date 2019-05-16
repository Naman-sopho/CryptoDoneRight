---
layout: quickstart
title: "Developer's QuickStart"
type: AES
image: /static_files/NewDevLogo.png
note: "Are you a developer? Get started with crucial implementation details above."
col: col-md-4 col-sm-4 col-xs-4 infoBlocks
alerts:

further-reading:

related-articles:

attacks:


---
<p>
<h2> <img src="/static_files/implementation.png " style="width:100px;height:100px;" /> AES Implementation</h2>

<font size="4"><strong>Concept:</strong></font>  DO NOT roll your own Crypto! Use standard services and libraries. <br />

It is NOT advisable in any circumstances to develop any sort of cryptography on your own. Instead , there are a few options for standard libraries that can be used.
These libraries offer better stability as they are usually a product of several years of experience in implementing cryptography by an active development community who are
dedicated towards efforts in implementation. It is therefore considered to be reliable and robust. <br /> <br />


<font size="3"><strong>Examples:</strong></font>
Openssl is one such library which popular and therefore is used as an example for this concept.
OpenSSL is not the only available crypto library. For a list of different libraries and a comparison
between them, visit <a href="https://en.wikipedia.org/wiki/Comparison_of_cryptography_libraries">here</a>.
<br /> <br />

The recommended version of OpenSSL that is to be used for AES is 1.1.0. This is for various reasons that concern and do not concern with AES. Some of them include for the ladev encryption standards and removal of older vulnerable ones.
<br /> <br />


<h2>Usage of Cryptography in Programming Languages</h2>

<font size="4"><strong>Concept:</strong></font> It is again advised to not roll out your own cryptography while developing software. There are popular libraries in almost all programming
languages that can readily be used to perform cryptographic operations.
<br /> <br />
<font size="4"><strong>Examples:</strong></font> <br />
<strong>PHP: </strong> <br />
PHP supported AES using two libraries, mcrypt and openssl. It should be noted that support for mcrypt is depracted since PHP 7.1.x. OpenSSL is the only available option at the moment. The examples for using AES encryption with mcrypt and openssl. <br /> <br />

<a href="https://aesencryption.net/#PHP-aes-encryption-example">https://aesencryption.net/#PHP-aes-encryption-example </a>
<br /> <br />

<strong>Java: </strong> <br />
The following sample Java program shows how to encrypt data using AES encryption algorithm. Java provides a number of helper classes for AES encryption such as Cipher (for encryption/decryption), SecretKey (represents the shared secret key) and KeyGenerator (generates the shared secret key). Also note that both secret key and encrypted data is binary data and hence cannot be printed directly. The following program prints them in hexadecimal form. <br /> <br />

In the following program, the KeyGenerator is initialized with a 128 bit secret key. If you want stronger keys such as 256 bit key, you need to Java cryptography extension (JCE) unlimited strength jurisdiction policy files. <br /> <br />

Download policy files for Java 7 <br />
Download policy files for Java 8 <br /> <br />

These zip files contain a number of jars and you need to copy them to {java.home}/jre/lib/security  directory of your JRE installation. Now you can pass 256 as secret key bit size to KeyGenerator. <br /> <br />

<pre>
<code>
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.xml.bind.DatatypeConverter;

/*
  * This example program shows how AES encryption and decryption can be done in Java.
  * Please note that secret key and encrypted text is unreadable binary and hence
  * in the following program we display it in hexadecimal format of the underlying bytes.
  * @author Jayson
*/
public class AESEncryption {

/*
  * 1. Generate a plain text for encryption
  * 2. Get a secret key (printed in hexadecimal form). In actual use this must
  * by encrypted and kept safe. The same key is required for decryption.
  * 3.
*/
public static void main(String[] args) throws Exception {
String plainText = "Hello World";
SecretKey secKey = getSecretEncryptionKey();
byte[] cipherText = encryptText(plainText, secKey);
String decryptedText = decryptText(cipherText, secKey);

System.out.println("Original Text:" + plainText);
System.out.println("AES Key (Hex Form):"+bytesToHex(secKey.getEncoded()));
System.out.println("Encrypted Text (Hex Form):"+bytesToHex(cipherText));
System.out.println("Descrypted Text:"+decryptedText);

}

/*
* gets the AES encryption key. In your actual programs, this should be safely
* stored.
* @return
* @throws Exception
*/
public static SecretKey getSecretEncryptionKey() throws Exception{
KeyGenerator generator = KeyGenerator.getInstance("AES");
generator.init(128); // The AES key size in number of bits
SecretKey secKey = generator.generateKey();
return secKey;
}

/*
* Encrypts plainText in AES using the secret key
* @param plainText
* @param secKey
* @return
* @throws Exception
*/
public static byte[] encryptText(String plainText,SecretKey secKey) throws Exception{
                      // AES defaults to AES/ECB/PKCS5Padding in Java 7
Cipher aesCipher = Cipher.getInstance("AES");
aesCipher.init(Cipher.ENCRYPT_MODE, secKey);
byte[] byteCipherText = aesCipher.doFinal(plainText.getBytes());
return byteCipherText;
}

/*
* Decrypts encrypted byte array using the key used for encryption.
* @param byteCipherText
* @param secKey
* @return
* @throws Exception
*/
public static String decryptText(byte[] byteCipherText, SecretKey secKey) throws Exception {
                      // AES defaults to AES/ECB/PKCS5Padding in Java 7
Cipher aesCipher = Cipher.getInstance("AES");
aesCipher.init(Cipher.DECRYPT_MODE, secKey);
byte[] bytePlainText = aesCipher.doFinal(byteCipherText);
return new String(bytePlainText);
}

/*
* Convert a binary byte array into readable hex form
* @param hash
* @return
*/
private static String  bytesToHex(byte[] hash) {
return DatatypeConverter.printHexBinary(hash);
}
}
</code>
</pre>
In highly secure systems, the secret key is usually stored in a separate hardware known HSMs(Hardware Security Modules). HSMs are expensive devices and hence a more cost effective way is to store the secret key in a separate secure partition or schema. <br /> <br />

<a href="https://stackoverflow.com/questions/992019/java-256-bit-aes-password-based-encryption"> https://stackoverflow.com/questions/992019/java-256-bit-aes-password-based-encryption </a> <br /> <br />

Here is another example that uses the OpenSSL library. This example has been pulled from the same website where the PHP examples are listed: <br /> <br />
<pre>
<code>
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import org.apache.commons.codec.binary.Base64;
/*
Aes encryption
*/
public class AES
{

private static SecretKeySpec secretKey ;
private static byte[] key ;

private static String decryptedString;
private static String encryptedString;

public static void setKey(String myKey){


MessageDigest sha = null;
try {
    key = myKey.getBytes("UTF-8");
    System.out.println(key.length);
    sha = MessageDigest.getInstance("SHA-1");
    key = sha.digest(key);
    key = Arrays.copyOf(key, 16); // use only first 128 bit
    System.out.println(key.length);
    System.out.println(new String(key,"UTF-8"));
    secretKey = new SecretKeySpec(key, "AES");


} catch (NoSuchAlgorithmException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
} catch (UnsupportedEncodingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}



}

public static String getDecryptedString() {
return decryptedString;
}
public static void setDecryptedString(String decryptedString) {
AES.decryptedString = decryptedString;
}
public static String getEncryptedString() {
return encryptedString;
}
public static void setEncryptedString(String encryptedString) {
AES.encryptedString = encryptedString;
}
public static String encrypt(String strToEncrypt)
{
try
{
    Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");

    cipher.init(Cipher.ENCRYPT_MODE, secretKey);


    setEncryptedString(Base64.encodeBase64String(cipher.doFinal(strToEncrypt.getBytes("UTF-8"))));

}
catch (Exception e)
{

    System.out.println("Error while encrypting: "+e.toString());
}
return null;
}
public static String decrypt(String strToDecrypt)
{
try
{
    Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5PADDING");

    cipher.init(Cipher.DECRYPT_MODE, secretKey);
    setDecryptedString(new String(cipher.doFinal(Base64.decodeBase64(strToDecrypt))));

}
catch (Exception e)
{

    System.out.println("Error while decrypting: "+e.toString());
}
return null;
}
public static void main(String args[])
{
        final String strToEncrypt = "My text to encrypt";
        final String strPssword = "encryptor key";
        AES.setKey(strPssword);

        AES.encrypt(strToEncrypt.trim());

        System.out.println("String to Encrypt: " + strToEncrypt);
        System.out.println("Encrypted: " + AES.getEncryptedString());

        final String strToDecrypt =  AES.getEncryptedString();
        AES.decrypt(strToDecrypt.trim());

        System.out.println("String To Decrypt : " + strToDecrypt);
        System.out.println("Decrypted : " + AES.getDecryptedString());

}

}
</code>
</pre>
</p>
