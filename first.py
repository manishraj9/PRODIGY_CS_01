def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)  # Decrypting is just encrypting with a negative shift

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    if shift < 1 or shift > 25:
        print("Invalid shift value. Please enter a number between 1 and 25.")
        return

    if choice == 'E':
        result = caesar_encrypt(text, shift)
        print(f"Encrypted text: {result}")
    else:
        result = caesar_decrypt(text, shift)
        print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()