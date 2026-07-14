import random
import string

chars=string.punctuation + string.ascii_letters + string.digits + " "
chars=list(chars)
og_text=input("enter message to be encrypted")
keys=chars.copy()
random.shuffle(keys)
encrypted_message=""

#ENCRYPT
for character in og_text:
    index=chars.index(character)
    encrypted_message += keys[index]

print(f"original text={og_text}")
print(f"encrypted text={encrypted_message}")


#DECRYPT
decrypt=input("enter the message to decrypt")
decrypted_message=" "
for character in decrypt:
    index=keys.index(character)
    decrypted_message += chars[index]

print(f"original text={decrypt}")
print(f"encrypted text={decrypted_message}")