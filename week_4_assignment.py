import hashlib
import argparse

parser = argparse.ArgumentParser(description="SHA256 Password Cracker")

parser.add_argument("filename", help="File containing password list")
parser.add_argument("hash", help="SHA256 hash to crack")

args = parser.parse_args()

target_hash = args.hash
filename = args.filename

try:
    with open(filename, "r") as file:
        for line in file:
            word = line.strip()
            hashed_word = hashlib.sha256(word.encode()).hexdigest()

            if hashed_word == target_hash:
                print(word)
                break
        else:
            print("Password not found.")

except FileNotFoundError:
    print("File not found.")
