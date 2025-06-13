# 🔐 Encryption & Decryption Script

This is `encryption_decryption.py`, a command-line Python script offering multiple options for symmetric encryption and decryption, including a **ransomware simulation** feature (for educational use only).

---

## ℹ️ **Note on PBKDF2 Options (options 7 and 8)**  
This option was primarily developed to test PBKDF2 functionality.  
For this reason, the password is hardcoded as:  
```
my password is unbreakable
```  
In a production-grade tool, this would never be done — users would be required to input their own passwords securely.

## ⚠️ Important Notice: Running the Ransomware Simulation (Option 9)

The **ransomware simulation** feature of this script performs actions that are typically flagged as malicious by antivirus software. In **Windows Defender**, this does not only block the script — it can also **automatically delete it** before you have a chance to run it.

### 🔧 To prevent this, follow these steps before running the script:

1. Open **Windows Security**.
2. Go to **Virus & threat protection**.
3. Under **Virus & threat protection settings**, click **Manage settings**.
4. Toggle **Real-time protection** to **Off**.


⚠️ **Warning:** 
> Disabling real-time protection significantly reduces your system's defenses.  
> Only run this script in a **controlled, isolated environment** (such as a **virtual machine** or test lab).  
> Re-enable your protection immediately after testing.

## 💡 How the Ransomware Simulation Works

- The ransomware simulation (option 9) will **encrypt all files inside a folder named `secret`**.
- This folder must be placed in the **same directory** as `encryption_decryption.py`.
- **Do not place the script inside the `secret` folder.**
- A sample `secret` folder is available in the repository for testing.

This feature uses **symmetric encryption**, so the same password is used for both encryption and decryption.

### 🛠️ To decrypt after the simulation:

1. Run the script again.
2. Choose: 6 - Decrypt all the Files in a directory
3. Enter the path to the `secret` folder when prompted.

---

## 📁 Encrypted Test File

Inside the folder `encrypted-message-group`, you will find:
- A text file that was encrypted using the script
- A corresponding key used during the encryption process

You can use this file to test the **"4 - Decrypt File"** option in the script.  
Make sure the key is in the same directory as the script.

---

## 💻 OS Compatibility

- ✅ Options 1–8: Compatible with **Windows** and **Linux**.
- ⚠️ Option 9 (Ransom Simulation): **Only available on Windows**.

---

## 🔐 Encryption Methods

The script uses **symmetric encryption** via the `cryptography` Python library.  
Options 7 and 8 use **PBKDF2** for password-based key derivation, adding stronger protection for file encryption.

---

