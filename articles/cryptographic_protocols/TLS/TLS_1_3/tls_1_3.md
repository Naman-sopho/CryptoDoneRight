---
layout: page
title: TLS 1.3
type: cryptographic_protocols
update: Last Updated Tues, 27 Aug 2019 12:00:01 -0400
permalink: "articles/cryptographic_protocols/tls/tls_1_3.html"
alerts:
  - id: 1
    type: success
    description: This is the LATEST and RECOMMENDED Version of TLS.
    link: ""
  - id: 2
    type: danger
    description: TLSv1.3 is still in its intial roll-out phase. Expect minimum information about issues.
    link: ""

warnings:
  - name: Turn off 0-RTT
    description: "0-RTT, or the zero round trip functionality that was written into the TLSv1.3 specification could allow for replay attacks. It is recommended to disable this functionality. These security concerns are documented near the end of the RFC, but attacks have also been presented at conferences. See the Further Reading section for links."

further-reading:
  - name: "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3"
    link: "https://tools.ietf.org/html/rfc8446"
  - name: "TLSv1.3 0-RTT Vulnerabilites"

---
TLSv1.3 is the latest version of the Transport Layer Security, or TLS, protocol. This protocol was designed for securing internet traffic and is typically seen in client/server architectures like connecting to a website from a browser. It was officially made a standard by the IETF in 2018 as an improvement upon TLSv1.2, providing many security and performance enhancements.

Filippo Valsorda had a great talk describing the major benefits of TLS 1.3 vs that of TLS 1.2. Many products, services, and companies have migrated to TLSv1.3 as it is the recommended version of the protocol. Implementations can be found in many major TLS stacks, but some are listed [here](https://github.com/tlswg/tlswg-wiki/blob/master/IMPLEMENTATIONS.md).
