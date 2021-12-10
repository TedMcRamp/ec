# Ec:
A Simple File Encryptor/Decryptor

This has been made for educational reasons only, any constructive criticism/advice/comments are welcome!

# Usage:
usage: ec.py [-h] [-e] [-d] -k KEY [-f FILE_OP] [-o OUTPUT] [action] [file]

File Encrypter/Decryptor

positional arguments:
  action                Action: either Encryption or Decryption, if the key is not specified the program will generate
                        a random key and print it out.
  file                  Encrypted/decrypted filetest input

options:
  -h, --help            show this help message and exit
  -e                    Alias for encrypt.
  -d                    Alias for decrypt.
  -k KEY, --key KEY     Encryption/decryption key
  -f FILE_OP, --file FILE_OP
                        Encrypted/decrypted file.
  -o OUTPUT, --output OUTPUT
                        Encrypted/decrypted output (default is stdout if no output is specified).
