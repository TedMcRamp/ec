import sys
import argparse
from cipher import encrypt, decrypt


def handle_args():
    parser = argparse.ArgumentParser(description="File Encrypter/Decryptor")

    action = parser.add_mutually_exclusive_group(required=True)

    action.add_argument("action", nargs=argparse.OPTIONAL,
                        help="Action: either Encryption or Decryption, if the key is not specified the program will generate a random key and print it out.")
    action.add_argument(
        "-e", help="Alias for encrypt.", dest="encrypt", action="store_true"
    )

    action.add_argument(
        "-d", help="Alias for decrypt.", dest="decrypt", action="store_true"
    )

    parser.add_argument("-k", "--key", dest="key",
                        help="Encryption/decryption key", required=True)

    inp = parser.add_mutually_exclusive_group(required=True)
    inp.add_argument("file", help="Encrypted/decrypted filetest input",
                     nargs=argparse.OPTIONAL)
    inp.add_argument("-f", "--file", dest="file_op",
                     help="Encrypted/decrypted file.")

    parser.add_argument(
        "-o", "--output", help="Encrypted/decrypted output (default is stdout if no output is specified).")

    args = parser.parse_args()
    action = args.action

    if action is not None:
        action = action.lower()
        if not (action == "encrypt" or action == "decrypt" or action == "e" or action == "d"):
            print(parser.format_usage() + '\n' +
                  "test.py: error: argument action: action must be either encrypt/e or decrypt/d.", file=sys.stderr)
            exit(1)
        elif action == "e":
            action = "encrypt"
        elif action == "d":
            action = "decrypt"
    elif args.encrypt:
        action = "encrypt"
    else:
        action = "decrypt"

    return {
        "action": action,
        "key": args.key,
        "file": args.file or args.file_op,
        "output": open(args.output, "wb") if args.output is not None else sys.stdout
    }


def main():
    args = handle_args()

    action = encrypt
    if args["action"] == "decrypt":
        action = decrypt

    target = open(args["file"], "rb").read()
    output = args["output"]

    key = args["key"]
    if key is not None:
        result = action(target, key.encode())
        if output == sys.stdout:
            try:
                print(result.decode())
            except:
                print("Wrong Key!", file=sys.stderr)
                exit(1)
        else:
            output.write(result)


if __name__ == "__main__":
    main()
