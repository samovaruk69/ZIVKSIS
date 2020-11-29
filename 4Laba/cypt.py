import hashlib

input_pass = input("Enter password :").encode()

hash_pass = hashlib.sha256(input_pass)
save_pass = hash_pass.hexdigest()

print(save_pass)

input_new_pass = input("Please repeate password :").encode()
hash_new_pass = hashlib.sha256(input_new_pass)
save_new_pass = hash_new_pass.hexdigest()

print(save_new_pass)

if save_pass == save_new_pass:
    print("Password correct")
else:
    print("Password dont match try correct password")