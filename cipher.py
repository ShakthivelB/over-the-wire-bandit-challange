def caesar_cipher(text, shift, mode='encrypt'):
    """Encrypt or decrypt text using Caesar cipher."""
    result = []
    shift = shift % 26

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)

    return ''.join(result)


def brute_force(text):
    """Try all 25 possible shifts and display results."""
    print("\n--- Brute Force (All Shifts) ---")
    for shift in range(1, 26):
        decrypted = caesar_cipher(text, shift, mode='decrypt')
        print(f"Shift {shift:2d}: {decrypted}")


def main():
    print("=" * 45)
    print("        Caesar Cipher Tool")
    print("=" * 45)

    while True:
        print("\nOptions:")
        print("  1. Encrypt")
        print("  2. Decrypt")
        print("  3. Brute Force (try all shifts)")
        print("  4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == '4':
            print("Goodbye!")
            break

        if choice not in ('1', '2', '3'):
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        text = input("Enter text: ")

        if choice == '3':
            brute_force(text)
            continue

        while True:
            try:
                shift = int(input("Enter shift (1-25): "))
                if 1 <= shift <= 25:
                    break
                print("Shift must be between 1 and 25.")
            except ValueError:
                print("Please enter a valid integer.")

        mode = 'encrypt' if choice == '1' else 'decrypt'
        output = caesar_cipher(text, shift, mode)

        print(f"\n--- Result ---")
        print(f"Mode   : {mode.capitalize()}")
        print(f"Shift  : {shift}")
        print(f"Input  : {text}")
        print(f"Output : {output}")


if __name__ == "__main__":
    main()
