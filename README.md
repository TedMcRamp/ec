# Ec:
A Simple File Encryptor/Decryptor

This has been made for educational reasons only, any constructive criticism/advice/comments are welcome!
Also, please report any issues you see in this project!

# Usage: 
 ec.py [-h] [-e] [-d] -k KEY [-f FILE_OP] [-o OUTPUT] [action] [file]

# Positional arguments:
   __action:                Action: either Encryption or Decryption, if the key is not specified the program will generate
                        a random key and print it out.__
                        <br>
                        <br>
   __file:                  Encrypted/decrypted file input__

# Options:
  -h, --help            show this help message and exit
  <br>
  -e                    Alias for encrypt.
  <br>
  -d                    Alias for decrypt.
  <br>
  -k KEY, --key KEY     Encryption/decryption key
  <br>
  -f FILE_OP, --file FILE_OP
                        Encrypted/decrypted file.
                        <br>
  -o OUTPUT, --output OUTPUT
                        Encrypted/decrypted output (default is stdout if no output is specified).
