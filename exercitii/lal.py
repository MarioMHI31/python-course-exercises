from cryptography.fernet import Fernet

# Generate and save the key (run once and save securely)
key = Fernet.generate_key()
print(f"Save this key securely: {key.decode()}")