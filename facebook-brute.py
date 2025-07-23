print("⚠️ এই স্ক্রিপ্টটি ডেমো ব্রুটফোর্স দেখানোর জন্য। বাস্তবে ব্যবহারে ফেসবুক বা আইন লঙ্ঘন হতে পারে।")
username = input("Username: ")
with open("passwords.txt") as f:
    for line in f:
        password = line.strip()
        print(f"Trying password: {password}")
