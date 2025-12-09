# Symmetrisk kryptering
## AES
```console
https://gchq.github.io/CyberChef/#recipe=AES_Encrypt(%7B'option':'Hex','string':'1234567890abcdefghijklmnopqrstu1234567890abcde'%7D,%7B'option':'Hex','string':'1234567890abcdefghijklmnopqrstu1234567890abcde'%7D,'CBC','Raw','Hex',%7B'option':'Hex','string':''%7D)To_Base64('A-Za-z0-9%2B/%3D')From_Base64('A-Za-z0-9%2B/%3D',true,false)AES_Decrypt(%7B'option':'Hex','string':'1234567890abcdefghijklmnopqrstu1234567890abcde'%7D,%7B'option':'Hex','string':'1234567890abcdefghijklmnopqrstu1234567890abcde'%7D,'CBC','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=SSBsb3ZlIGN5YmVyc2VjdXJpdHkuIEkgd2FudCB0by4uLS0tVEhFIE9UVE9NQU4gRU1QSVJFIElTIFRIRSBCRVNU
```

## DES
```console
https://gchq.github.io/CyberChef/#recipe=DES_Encrypt(%7B'option':'Hex','string':'123456789101112'%7D,%7B'option':'Hex','string':'abcdefghijklmnopqrstuabcdefghijklmnopqrstuwabc'%7D,'CBC','Raw','Hex')To_Base64('A-Za-z0-9%2B/%3D')From_Base64('A-Za-z0-9%2B/%3D',true,false)DES_Decrypt(%7B'option':'Hex','string':'123456789101112'%7D,%7B'option':'Hex','string':'abcdefghijklmnopqrstuabcdefghijklmnopqrstuwabc'%7D,'CBC','Hex','Raw')&input=SSBkb24ndCB3aHkgSSBzYWlkIHdoYXQgSSBzYWlkIGluIHRoZSByZWNpcGUgYmVmb3JlIHRoaXMgb25lLiBCdXQgaXQgaXMgd2hhdCBpdCBpcy4
```

## Tripple DES
```console
https://gchq.github.io/CyberChef/#recipe=Triple_DES_Encrypt(%7B'option':'Hex','string':'ThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKey'%7D,%7B'option':'Hex','string':'THISISALSOVERYLONGTHISISALSOVERYLONGTHISISALSOVERYLONGTHISISALSOVERYLONG'%7D,'CBC','Raw','Hex')To_Base64('A-Za-z0-9%2B/%3D')From_Base64('A-Za-z0-9%2B/%3D',true,false)Triple_DES_Decrypt(%7B'option':'Hex','string':'ThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKeyThisIsAVeryLongKey'%7D,%7B'option':'Hex','string':'THISISALSOVERYLONGTHISISALSOVERYLONGTHISISALSOVERYLONGTHISISALSOVERYLONG'%7D,'CBC','Hex','Raw')&input=RGlkIHlvdSBrbm93IHRoYXQgVGhlIE90dG9tYW4gRW1waXJlJ3MgbWlsaXRhcnkgYmFuZCwgdGhlIE1laHRlciwgcGxheWVkIHNvIGxvdWRseSB0aGF0IEV1cm9wZWFuIGFybWllcyBzb21ldGltZXMgcGFuaWNrZWQgYmFzaWNhbGx5IHRoZSBvcmlnaW5hbCB0dXJuIHRoZSB2b2x1bWUgZG93biEgbW9tZW50IGluIGhpc3Rvcnku
```

# Asymmetrisk kryptering
## RSA - SHA1

Person A generer en public og private key
```console
https://gchq.github.io/CyberChef/#recipe=Generate_RSA_Key_Pair('1024','PEM')&input=MUV0dURTZmFSUmNndVdnbm9RZWR6bDEwUHdzZzBsMFFDVEFqN2NFdG9VdEwyOHFLbzcyOEFVcTllVFc3MWNWVWYrNXB4eFRHOFdPWVk2cGsrME9uOGtabldhRFV5aTF0TWcrZzRNMlpWZ3JvOHozbFdkMnIrTmppMVpMZzYwYUdtTDJkaG1pMHhoNWJCV2J3NTRkVUlmVTh5Ynd5cmVYNENoNE1EUHhhT0Y0PQ&oeol=CRLF
```
Person B bruger person A's public key til at kryptere sin besked
```console
https://gchq.github.io/CyberChef/#recipe=RSA_Encrypt('-----BEGIN%20PUBLIC%20KEY-----%5CnMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDG/zcWmsD6zQmkQG7gO%2BrjFPcR%5CnZKWkH4GU3u2/r8mdhltGlkFBSe37FlkXVlAyaUS2Iuou1l3xymRrutSURcxzI2o0%5CnZTbkdapxSFUl7W3mJNy0EIA9VWnR16Z7fIY3w6TLXz7gecBMwI3NyWXdltoXfMM0%5CnnZtEXw33a//hIYqpBwIDAQAB%5Cn-----END%20PUBLIC%20KEY-----','RSA-OAEP','SHA-1')To_Base64('A-Za-z0-9%2B/%3D')&input=VGhpcyBpcyBhIG1lc3NhZ2UgZW5jcnlwdGVkIHdpdGggYSBwdWJsaWMgUlNBIGtleSBieSBDeWJlcmNoZWYu
```
Person A tager person B's krypterede besked og dekrypterer den ved hjælp af sin egen tilhørende private key
```console
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)RSA_Decrypt('%5Cn-----BEGIN%20RSA%20PRIVATE%20KEY-----%5CnMIICXQIBAAKBgQDG/zcWmsD6zQmkQG7gO%2BrjFPcRZKWkH4GU3u2/r8mdhltGlkFB%5CnSe37FlkXVlAyaUS2Iuou1l3xymRrutSURcxzI2o0ZTbkdapxSFUl7W3mJNy0EIA9%5CnVWnR16Z7fIY3w6TLXz7gecBMwI3NyWXdltoXfMM0nZtEXw33a//hIYqpBwIDAQAB%5CnAoGACHOrg87D1oMh3zOLYgO5eLaZvcfgDyX1a3zCbUtKjWG4%2B7kDAYJh1LHAy/Bz%5CnDIkTDYdTGfUp3Uyi0j6Hq9qBEemjUpunKmL2bjuYEcjgk5s3CW4NcbrBr256SNQb%5CnBhXVgjcdZk1BFx6bu7zcSeUqxof3088kK6%2B%2B3UwMvIocD2ECQQDtQAYe72iX9QOU%5CnQFSviYWOVFxUbuq3iTNt6RCiiinjf%2BBGMCcC7VHmh13adaKBGFzAAIOlpDs6w9V6%5CnrukNHWrnAkEA1rlDqPA/BAgABrwrPWYmNLVw4V%2BQT3r5W19lNJbStKItfT%2B02fpy%5CnZSTkxfaNofM8wuO6rKSZltWOVnsVVzAs4QJASm3bfbj9xy5GgSvtZWRvUceFb7ec%5CnSxfv2ntTjKprmcN0SJCyrGhnWTr%2BZpqg8H8EGfgPVNfA/R6Syno1ArhH4QJBALmk%5CngUfNNl4w4HzyMNwrtbp6aDaiHa1p367NAj3%2Ba/t5/6Q68QxIiKDDzfsNmBQ9rPm%2B%5CnVAWxZYzP4/kG/0NbRmECQQCjaHwai1oToA42RxpV/PUqwgwN/AIVXiA5AkXSvrGJ%5Cn1rRkzGFbapiK0/GkZR1XwqNiZV3PbEZ9ni%2BYIRXpSkPb%5Cn-----END%20RSA%20PRIVATE%20KEY-----','','RSA-OAEP','SHA-1')&input=ZUFNWnplRXhHQXg3MFRqWVhGQStHbXVWeW9zWkptNWJnZzljU2pMaHRGZm51UTNnbWQ4b1RyaUR1S0ZoQ1lYY2t6MDNWYk1rT1dickxadzZMZDJlZHM0aUFPQ0h4NVRkbTRvODBhcEN6cFhwakphOGs2TTJzK3ZrbGoveGJ2THpDU0RHV0xldjI2bzRGL3hUMjI2NXpJRWRzRHQ1NVF5dzUvV3kycjZXY2tjPQ&ieol=CRLF
```

# Encoding
## HTML encoding
```console
https://gchq.github.io/CyberChef/#recipe=To_HTML_Entity(false,'Named%20entities')&input=PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg&ieol=CRLF
```
## URL Encoding
```console
https://gchq.github.io/CyberChef/#recipe=URL_Encode(false)&input=PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg&oenc=65001&ieol=CRLF
```
## Hash
```console
https://gchq.github.io/CyberChef/#recipe=MD4()&input=PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg&ieol=CRLF
```
