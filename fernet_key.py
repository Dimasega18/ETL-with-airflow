from cryptography.fernet import Fernet

f_key = Fernet.generate_key()
print(f_key.decode())
