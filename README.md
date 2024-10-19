README.md

# Indexed Caesar Cipher with Random Shifts

This project introduces a modern take on the classic Caesar Cipher by incorporating random shifts for each character, making the cipher more secure and unpredictable. The key for decryption is a sequence of random integers that are applied to each character's position in the alphabet.

## Features

- **Random Shifts**: Each letter is shifted by a random value from 1 to 5.
- **Custom Key**: The encryption function generates and returns both the encoded message and the key used for the shifts.
- **Supports Upper and Lowercase Letters**: Non-letter characters remain unchanged.
- **Encryption and Decryption**: Two separate functions for encoding and decoding messages.

## Usage

### Encryption
To encode a message, run the `index_cipher_shifts()` function, which will return the encrypted text and the key.

```python
from cipher import index_cipher_shifts

text = "Hello World!"
encoded_text, key = index_cipher_shifts(text)
print(f"Encoded Text: {encoded_text}")
print(f"Key: {key}")

Decryption

To decode a message, use the decode_indexed_cipher() function and provide the encoded text along with the key.

from decipher import decode_indexed_cipher

encoded_text = "Your encoded message here"
key = [4, 2, 5, ...]  # Key generated during encryption
decoded_text = decode_indexed_cipher(encoded_text, key)
print(f"Decoded Text: {decoded_text}")

Example

Input Message: Hello World!
Encoded Message: Jgnnq Yqtnf!
Key: [2, 4, 3, 5, 1, 2, 3, 4, 2, 1, 5]

