import sys
from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random


def encrypt(msg, key):
    newkey = MD5.new(key).hexdigest().encode()
    r = Random.new().read(AES.block_size)
    cipher = AES.new(newkey, AES.MODE_CFB, r)
    return r + b"$" + cipher.encrypt(msg)


def decrypt(msg, key):
    r = msg[:msg.find(b"$")]
    msg = msg[msg.find(b"$")+1:]
    newkey = MD5.new(key).hexdigest().encode()
    cipher = AES.new(newkey, AES.MODE_CFB, r)
    return cipher.decrypt(msg)


def main():
    order = input("What do you want to do ? (default is encrypt): ")
    if order == "decrypt" or order == "d":
        io = input("filename: ")
        with open(io, "rb") as text:
            key = input("Enter the key: ")
            print(decrypt(text.read(), key.encode()))

    else:
        key = input("Enter the key: ")
        msg = input("Enter msg: ")
        filename = input("Enter file: ")

        with open(filename, "wb") as io:
            io.write(encrypt(msg.encode(), key.encode()))


if __name__ == "__main__":
    main()
