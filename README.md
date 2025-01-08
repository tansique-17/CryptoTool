# CryptoTool
## File Encryption/Decryption Tool

This Python application provides a graphical user interface (GUI) for encrypting and decrypting files using the `cryptography` library. The tool ensures your files are securely encrypted and easy to decrypt when needed.

## Features
- **Generate Key**: Generate a new encryption key and save it as `secret.key`.
- **Encrypt File**: Encrypt any file and save it with a custom name and with any extension.
- **Decrypt File**: Decrypt the encrypted file and save it with a custom name and the original content format.

## Requirements
- Python 3.7+
- `cryptography` library
- `customtkinter` library

### Installation
1. Clone or download the repository.
2. Install the required Python packages by running:
   ```bash
   pip install cryptography customtkinter
   ```

## How to Use

### 1. Launch the Application
Run the script `crypto.py` in your Python environment:
```bash
python crypto.py
```

### 2. Generate a Key
1. Click the **Generate Key** button to generate an encryption key.
2. The key will be saved in the current directory as `secret.key`. Keep this file safe, as it is essential for both encryption and decryption.

### 3. Encrypt a File
1. Click **Encrypt File**.
2. Select the file you want to encrypt using the file dialog.
3. Provide a name for the encrypted file in the save dialog .
4. The file will be encrypted and saved in the specified location.

### 4. Decrypt a File
1. Click **Decrypt File**.
2. Select the encrypted file using the file dialog.
3. Provide a name for the decrypted file in the save dialog (e.g., `original_file.txt`).
4. The file will be decrypted and saved in the specified location.

## Important Notes
- The encryption key (`secret.key`) is required for both encryption and decryption. Losing the key means you will not be able to decrypt your files.
- Always use strong and unique passwords if you decide to manage your key securely elsewhere.

## Dependencies
This application uses the following Python libraries:
- `cryptography`: Provides the core encryption and decryption functionality.
- `customtkinter`: For creating the modern and user-friendly GUI.

Install dependencies using pip:
```bash
pip install cryptography customtkinter
```

## License
This project is licensed under the [MIT License](./LICENSE). Feel free to use, modify, and distribute this software as needed.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Bug reports and feature requests are also welcome.

---

Enjoy secure file encryption and decryption with this easy-to-use tool!

