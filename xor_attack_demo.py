# xor_attack_demo.py

# === XOR Cipher Functions ===
def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key)) for c in text)

# === Known-Plaintext Attack Simulation ===
def known_plaintext_attack(ciphertext, known_plaintext):
    print("\n[Known-Plaintext Attack on XOR Cipher]")
    guessed_key = chr(ord(ciphertext[0]) ^ ord(known_plaintext[0]))
    print("Guessed Key:", repr(guessed_key))

    # Decrypt with guessed key
    decrypted = xor_encrypt_decrypt(ciphertext, guessed_key)
    print("Decrypted Message:", decrypted)

# === Main Execution ===
def main():
    print("=== XOR Cipher Demo ===")

    message = "SecretData"
    key = "K"

    encrypted = xor_encrypt_decrypt(message, key)
    print("Encrypted Message (raw):", encrypted)

    decrypted = xor_encrypt_decrypt(encrypted, key)
    print("Decrypted Message:", decrypted)

    # Simulate attacker knows message starts with 'S'
    known_plaintext_attack(encrypted, "S")

if __name__ == "__main__":
    main()
