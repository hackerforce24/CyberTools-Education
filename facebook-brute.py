print("⚠️ This script is a for brute-force. Using it in real scenarios can violate laws.")
username = input("Username: ")
with open("passwords.txt") as f:
    for line in f:
        password = line.strip()
        print(f"Trying password: {password}")
