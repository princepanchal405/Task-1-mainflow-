# Custom Encryption-Decryption System

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Menu
def main():
    print("=== Custom Caesar Cipher Encryption-Decryption ===")
    while True:
        print("\nMenu:")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            msg = input("Enter message to encrypt: ")
            shift = int(input("Enter shift key (number): "))
            encrypted = caesar_encrypt(msg, shift)
            print("Encrypted Message:", encrypted)

        elif choice == '2':
            msg = input("Enter message to decrypt: ")
            shift = int(input("Enter shift key (number used during encryption): "))
            decrypted = caesar_decrypt(msg, shift)
            print("Decrypted Message:", decrypted)

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
