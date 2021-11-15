# Using RSA
This module allows you to encrypt & decrypt ASCII strings with the RSA algorithm.

First import the module and generate your keys.

```
from rsa import *

keys = generate_keys(100)
```

Note: The `100` in the `generate_keys()` function sets an upper bound for the size of the primes used in the key. This parameter should be as large as is computationally feasible to ensure the greatest possible security. This implementation is, of course, far from optimal, and primarily intended as a proof of concept, so we therefore choose relatively small numbers for this parameter. 

Your keys will be returned as a dictionary of the form: `{'public-key': {'n': 8633, 'e': 5}, 'private-key': {'d': 845}}
`

Next, define a message and encrypt it using the recipient's public-key.

```
message = "To strive, to seek, to find, and not to yield."
encrypted_message = encrypt(message,keys["public-key"])
```

The encrypted message will be a list of integers, where each integer represents an encrypted character. Note: it is of course just as easy to encrypt the message in multiple character chunks.

Finally, decrypt the encrypted message with the recipients private-key.

```
decrypt(encrypted_message,keys)
>>> 'To strive, to seek, to find, and not to yield.'
```
