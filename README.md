# Python_telegram_bot

Bot is used for encrypting and decrypting files and messages. Text encrypting uses method of [Polybius square](https://en.wikipedia.org/wiki/Polybius_square) which was used in ancient Greece.
Feature of this principle is that one letter can have two matches.

Example how to encrypt and decrypt text. Also, we can see that __"a" has two matches, in encrypted version. It is "Г" and "Ę"__:
![Example text](/text_encode.png)

Files are encrypted by [cryptography library](https://pypi.org/project/cryptography/). It creates decrypted file and key.

Here in __example__ we can see how __to encrypt__ month transactions report:
![encrypt file](/encdng_file.png)

__Decrypt file__:
![encrypt file](/dcdng_file.png)
