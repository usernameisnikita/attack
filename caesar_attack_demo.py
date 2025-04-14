# caesar_attack_demo.py

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

# === Brute-force Attack with Early Stop ===
def caesar_brute_force(cipher_text, known_word):
    print("\n[Brute-force Attack on Caesar Cipher]")
    for shift in range(26):
        decrypted = caesar_decrypt(cipher_text, shift)
        print(f"Trying Shift {shift:2}: {decrypted}")
        if known_word.lower() in decrypted.lower():
            print(f"\n[✓] Found match with shift {shift}: {decrypted}")
            break
    else:
        print("\n[!] No match found.")

# === Main Execution ===
def main():
    print("=== Caesar Cipher Demo ===")

    message = "AttackAtDawn"
    key = 4

    encrypted = caesar_encrypt(message, key)
    print("Encrypted Message:", encrypted)

    decrypted = caesar_decrypt(encrypted, key)
    print("Decrypted Message:", decrypted)

    # Attacker knows message contains the word "Attack"
    caesar_brute_force(encrypted, known_word="Attack")

if __name__ == "__main__":
    main()
