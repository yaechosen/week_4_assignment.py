import hashlib

target_hash = "5e737f891db1175442a39fde73e51d781a545506d71c95477a6deb5988bd7f9a"
with open("password.txt", "r") as file:
    for line in file:
        word = line.strip()

        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        if hashed_word == target_hash:
            print(word)
            break
            print("Done checking")
        
