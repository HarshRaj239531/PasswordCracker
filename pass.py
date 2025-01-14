print("harsh")
import hashlib

#Function to crack the password
def crack_password(hash_to_crack, password_file):
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip() #Remove any extra spaces/newlines
            # Hash the password using MDS (common for learning purposes)
            hashed_password = hashlib.md5(password.encode()).hexdigest()


            #compare the hashes
            if hashed_password == hash_to_crack:
                print(f"[+] Password found: {password}")
                return
            print("[-] Password not found in the dictionary.")

#Example MD5 hash (this is "password123")
hash_to_crack = "482c811da5d5b4bc6d497ffa98491e38"


# Path to a dictionary file (replace with the actual file path)
password_file = "passwords.txt"

# Run the function
crack_password(hash_to_crack, password_file)