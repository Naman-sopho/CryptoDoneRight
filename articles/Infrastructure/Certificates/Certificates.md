---
layout: page
title: Certificates
type: infrastructure
update: Last Updated Thu, 12 Dec 2018 12:00:01 -0400
permalink: "articles/infrastructure/Certificates/Certificates.html"
alerts:

further-reading:

related-articles:

warnings:

    
best_practices:


---
A digital certificate, or just "certificate," is a combination of three basic components: an asymmetric public key, metadata related to the key (including an identity associated with the key's owner), and a digital signature over the rest of the data. The signature must come from the public key of the "Certificate Authority" (CA) that signs (issues) the certificate. In cryptography, a certificate is used for one party to determine that another party is who they claim to be. 

In an idealized and simplified example, a browser connects to "https://example.com" and the webserver responds. The webserver is claiming to be "example.com" but the browser needs to verify this and make sure that the response is not from an imposter. To prove its identity, the webserver sends a certificate to the browser that includes the name "example.com", a public key, and a signature from a certificate authority (CA). The browser must already have another certificate for the CA stored internally. Using the CA's public key (from its certificate), the browser verifies the signature on the certificate for "example.com" to prove that it was issued by the CA.

As a final step, the browser and the webserver engage in a handshake in which the webserver proves that it has the private key associated with the certificate. Now the browser "knows" that a trusted third party (the CA) has approved the webserver to claim the identity "example.com."

In actuality, this description is over-simplified and there are a number of ways for imposters to try and fool the system. The quick-start guides provide more details about the types of protections and policies that are necessary for certificates to be used correctly.