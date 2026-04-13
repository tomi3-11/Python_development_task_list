def main():
	print("Basic File Encryption/Decryption")
	print("1. Encrypt a file")
	print("2. Decrypt a file")

	choice = input("Choose an option (1/2): ").strip()
	file_path = input("Enter file path: ").strip()
	shift = int(input("Enter shift key (e.g., 3): ").strip())

	if choice == "1":
		process_file(file_path, shift, "encrypt")
	elif choice == "2":
		process_file(file_path, shift, "decrypt")
	else:
		print("Invalid option. Please choose 1 or 2.")


def process_file(file_path, shift, mode):
	try:
		with open(file_path, "r", encoding="utf-8") as file:
			content = file.read()
	except FileNotFoundError:
		print(f"File not found: {file_path}")
		return
	except Exception as error:
		print(f"Error reading file: {error}")
		return

	if mode == "encrypt":
		transformed = caesar_cipher(content, shift)
		output_file = file_path + ".enc"
	else:
		transformed = caesar_cipher(content, -shift)
		output_file = file_path + ".dec"

	try:
		with open(output_file, "w", encoding="utf-8") as file:
			file.write(transformed)
		print(f"{mode.capitalize()}ed file saved as: {output_file}")
	except Exception as error:
		print(f"Error writing file: {error}")


def caesar_cipher(text, shift):
	result = []

	for char in text:
		if char.isalpha():
			base = ord('A') if char.isupper() else ord('a')
			shifted_char = chr((ord(char) - base + shift) % 26 + base)
			result.append(shifted_char)
		else:
			result.append(char)

	return ''.join(result)


if __name__ == "__main__":
	main()
