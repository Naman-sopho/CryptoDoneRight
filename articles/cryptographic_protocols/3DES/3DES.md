---
layout: page
title: 3DES
type: cryptographic_protocols
update: Last Updated Thu, 12 Dev 2018 12:00:01 -0400
permalink: "articles/cryptographic_protocols/3DES.html"
alerts:
  - id: 1
    type: danger
    description: This is the NOT the recommended standard.
    link: dev/articles/cryptographic_protocols/AES
  - id: 2
    type: danger
    description: There are serious security implications if not configured properly!
    link: ""
further-reading:

related-articles:

attacks:
  - name: Meet in the Middle Attack
    description: ":This particular attack can occur with specific settings in which DES could operate (keying option 1)."
    link: ""
  - name: Sweet 32
    description: This is a major attack that renders 3DES weak and compromises the security entirely. But like mentioned before, there are ways to mitigate and still use 3DES. OpenSSL does not include 3DES per default since version 1.1.0 (August 2016), and considers it a "weak cipher". Cisco's advisory on Sweet32:"
    link: "https://tools.cisco.com/security/center/viewAlert.x?alertId=48625"

---
3DES is an encryption algorithm that evolved from previous flavors of the same algorithm (DES which was first published in 1975). 3DES is being phased out slowly as there are new vulnerabilities that make the protocol significantly weaker. Although 3DES might be widely deployed still, it is because there are certain settings which when applied along with DES can provide good security. But considering the fact that there are newer protocols such as AES, there are no reasons to stick to 3DES apart from backward compatibility or legacy support.
