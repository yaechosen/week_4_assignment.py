import hashlib

target_hash = "PUT_HASH_HERE"

with open password.txt as file:
    for line in file:
        word = line.strip()

        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        if hashed_word == target_hash:
            print(word)
            break