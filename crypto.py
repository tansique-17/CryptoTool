import os
from cryptography.fernet import Fernet
import customtkinter as ctk
from tkinter import filedialog, messagebox

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption/Decryption Tool")
        self.root.geometry("600x400")
        ctk.set_appearance_mode("dark")

        self.key = None

        # Frame Setup
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title Label
        self.title_label = ctk.CTkLabel(self.frame, text="File Encryption/Decryption", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Buttons for Actions
        self.generate_key_button = ctk.CTkButton(self.frame, text="Generate Key", command=self.generate_key)
        self.generate_key_button.pack(pady=10)

        self.encrypt_button = ctk.CTkButton(self.frame, text="Encrypt File", command=self.encrypt_file)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ctk.CTkButton(self.frame, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack(pady=10)

    def generate_key(self):
        self.key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(self.key)
        messagebox.showinfo("Key Generated", "Secret key saved as 'secret.key'. Keep it safe!")

    def load_key(self):
        try:
            with open("secret.key", "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            messagebox.showerror("Error", "Key file not found. Generate a new key first.")
            return None

    def encrypt_file(self):
        file_path = filedialog.askopenfilename(title="Select File to Encrypt")
        if not file_path:
            return
        output_path = filedialog.asksaveasfilename(title="Save Encrypted File", defaultextension=".enc")
        if not output_path:
            return
        self.key = self.load_key()
        if not self.key:
            return
        try:
            with open(file_path, "rb") as file:
                data = file.read()
            fernet = Fernet(self.key)
            encrypted_data = fernet.encrypt(data)
            with open(output_path, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
            messagebox.showinfo("Success", f"File encrypted and saved as '{output_path}'.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decrypt_file(self):
        file_path = filedialog.askopenfilename(title="Select File to Decrypt")
        if not file_path:
            return
        output_path = filedialog.asksaveasfilename(title="Save Decrypted File", defaultextension=".txt")
        if not output_path:
            return
        self.key = self.load_key()
        if not self.key:
            return
        try:
            with open(file_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data)
            with open(output_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)
            messagebox.showinfo("Success", f"File decrypted and saved as '{output_path}'.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = EncryptionApp(root)
    root.mainloop()
