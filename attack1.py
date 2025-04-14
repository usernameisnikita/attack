# crypto_attack_demo.py

# === Caesar Cipher Functions ===
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def caesar_brute_force(cipher_text):
    print("\n[Brute-force Attack on Caesar Cipher]")
    for shift in range(26):
        decrypted = caesar_decrypt(cipher_text, shift)
        print(f"Shift {shift}: {decrypted}")

# === XOR Cipher Functions ===
def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key)) for c in text)

def xor_known_plaintext_attack(ciphertext, known_plaintext):
    print("\n[Known-Plaintext Attack on XOR Cipher]")
    guessed_key = chr(ord(ciphertext[0]) ^ ord(known_plaintext[0]))
    print("Guessed Key:", guessed_key)
    decrypted = xor_encrypt_decrypt(ciphertext, guessed_key)
    print("Decrypted Message:", decrypted)

# === Main Execution ===
def main():
    # Caesar Cipher Demo
    print("=== Caesar Cipher Demo ===")
    message1 = "HelloWorld"
    caesar_key = 3

    encrypted_caesar = caesar_encrypt(message1, caesar_key)
    print("Encrypted Message:", encrypted_caesar)

    decrypted_caesar = caesar_decrypt(encrypted_caesar, caesar_key)
    print("Decrypted Message:", decrypted_caesar)

    caesar_brute_force(encrypted_caesar)

    # XOR Cipher Demo
    print("\n=== XOR Cipher Demo ===")
    message2 = "SecretMessage"
    xor_key = "K"

    encrypted_xor = xor_encrypt_decrypt(message2, xor_key)
    print("Encrypted Message:", encrypted_xor)

    decrypted_xor = xor_encrypt_decrypt(encrypted_xor, xor_key)
    print("Decrypted Message:", decrypted_xor)

    xor_known_plaintext_attack(encrypted_xor, "S")  # Known first letter

if __name__ == "__main__":
    main()
