# Cryptly

**Cryptly** is a Python library implementing common encryption and cipher techniques. It provides easy-to-use functions for both encryption and decryption.

## Installation

You can install **Cryptly** using pip:

```bash
pip install cryptly
```

## Features

- Implementations of various encryption algorithms.
- Simple API for encryption and decryption.
- Supports custom alphabets.

## Usage

Here’s a quick example of how to use Cryptly:

```python
import string
from cryptly import AffineCipher

cipher = AffineCipher(key_1=5, key_2=24, alphabet=string.ascii_lowercase)
encrypted = cipher.encrypt("hello")
print(encrypted)
```

## Contribute

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
