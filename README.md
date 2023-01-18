# Python_telegram_bot

Bot is used for encrypting and decrypting files and messages. Text encrypting uses method of [Polybius square](https://en.wikipedia.org/wiki/Polybius_square) which was used in ancient Greece.
Feature of this principle is that one letter can have two matches.

Here in example, we can see how to encrypt and decrypt text. Also, we can see that "a" has two matches, in encrypted version. It is "Г" and "Ę":
![Example text](/text_encode.png)

Files are encrypted by [cryptography library](https://pypi.org/project/cryptography/). It creates decrypted file and key.

Here in example we can see how to decrypt file:
![encrypt file](/dcdng_file.png)

Decrypt file:
![encrypt file](/encdng_file.png)
