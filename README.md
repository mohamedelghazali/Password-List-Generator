# 🔐 **Dz PLG** (Password List Generator)  

A high-performance Python tool for generating custom password lists based on user-provided keywords. Perfect for **security professionals, pentesters, and red teamers** who need tailored wordlists for brute-force simulations, credential stuffing tests, or security research.  

---

## 🚀 **Features**  

✅ **Smart Keyword Transformations**  
   - **Leet-speak substitutions** (e.g., `a → @`, `e → 3`).  
   - **Case variations** (uppercase, lowercase, camelCase, alternating).  
   - **Reversed words** (e.g., `password → drowssap`).  

✅ **Advanced Pattern Generation**  
   - **Multi-keyword combinations** (1–3 words).  
   - **Symbol & number insertion** (`!`, `@`, `2024`, etc.).  
   - **Dynamic length control** (min/max password length).  

✅ **Optimized Performance**  
   - **Batched disk writes** (reduces I/O overhead).  
   - **No duplicates** (ensures uniqueness).  
   - **Configurable limits** (control output size).  

---

## 📥 **Installation**  

1. **Requirements**:  
   - Python 3.8+  
   - No external dependencies.  

2. **Clone & Run**:  
   ```bash
   git clone https://github.com/yourusername/Password-List-Generator.git
   cd Password List Generator
   python DzPLG.py
   ```

---

## 🛠 **Usage**  

1. **Input Keywords**:  
   ```plaintext
   Enter base keywords (e.g., names, dates): admin password 1990
   ```

2. **Set Password Length**:  
   ```plaintext
   Minimum password length: Preferably not less than 6
   Maximum password length: unlimited
   ```

3. **Output**:  
   Generated passwords are saved to:  
   `output/password_list_YYYYMMDD_HHMMSS.txt`  

---

## 📂 **Example Output**  

For input `admin 123`:  
```plaintext
admin
@dmin
4DM1N
123admin
admin!123
aDm1n#2024
```

---

## ⚙️ **Customization**  

Edit `DzPLG.py` to tweak:  
- **Leet substitutions** (`LEET_MAP`).  
- **Symbols/numbers** (`SYMBOLS`, `NUMBERS`).  
- **Performance** (`BATCH_SIZE`, `TARGET_COUNT`).  

---

## 📜 **License**  
MIT License. **Use ethically and legally.**  

---

## 💡 **Contributing**  
Found a bug? Want a new feature? Open an issue or submit a PR!  

---

> ⚠️ **Disclaimer**: Only use on systems you own/have permission to test.  

--- 

🔐 **Stay secure, stay sharp!** 🔐
