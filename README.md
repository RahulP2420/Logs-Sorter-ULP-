# **Logs-Sorter-ULP**  

### **Read the File and Key Features of the Script**  
This script is designed to extract and reformat sensitive information (like URLs, usernames, and passwords) from specific log files. Below is an explanation of how it works and its key features.

---

### **Key Features**  

- **🚀 Automated File Traversal:**  
   Automatically scans the selected directory and subdirectories for target files, reducing manual effort.

- **🔍 Pattern Matching with Regular Expressions:**  
   Extracts data using robust regular expressions, ensuring flexibility and accuracy.

- **📂 Dynamic Output File Naming:**  
   Names the output file based on the input directory, making it easy to identify the source of extracted data.

- **⚡ Error Resilience:**  
   Gracefully handles errors (e.g., file encoding issues, missing patterns) and logs them for debugging.

- **👥 User-Friendly Interface:**  
   Uses Tkinter to provide a graphical interface for directory selection, making it accessible to non-technical users.

- **📈 Scalability:**  
   Efficiently handles large datasets with multiple subdirectories and files.

- **📝 Formatted and Readable Output:**  
   Outputs credentials in a structured format (`URL|username|password`) that can be directly used or parsed by other tools.

- **🌐 Cross-Platform Compatibility:**  
   Built with standard Python libraries (`os`, `re`, `tkinter`), ensuring compatibility across Windows, macOS, and Linux.

---

### **Checklist: Requirements to Run the Script**

#### **📋 Prerequisites**
1. **Python Environment:**  
   - Python 3.6 or higher installed.  
     Verify using:  
     ```bash
     python --version
     ```

2. **Required Libraries:**  
   - **os:** For directory and file operations.  
   - **re:** For regular expression matching.  
   - **tkinter:** For the graphical file selection dialog.  
   
   **Linux Users:** Install `tkinter` (if missing):  
   ```bash
   sudo apt-get install python3-tk
   ```

3. **Supported Operating Systems:**  
   - Windows  
   - macOS  
   - Linux  

4. **Target Files:**  
   - Files named `All Passwords.txt` or `Passwords.txt` must exist in the directory you select.

---

### **Steps to Run the Script**

1. **💻 Install Python (if not already installed):**  
   - Download and install from [python.org](https://www.python.org/downloads/).  

2. **📂 Save the Script:**  
   - Save the script as `LogsSorterULP.py` (or any other name).  

3. **📜 Prepare Log Files:**  
   - Place files (`All Passwords.txt` or `Passwords.txt`) in the directory you want to process.

4. **🔧 Set Up a Virtual Environment (Optional but Recommended):**  
   - Create and activate a virtual environment:  
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows: .\env\Scripts\activate
     ```

5. **▶ Run the Script:**  
   - Execute the script:  
     ```bash
     python LogsSorterULP.py
     ```

6. **📂 Select Directory:**  
   - A graphical window will open; select the folder containing the log files.

7. **✅ View Results:**  
   - The script saves the extracted credentials to a file named:  
     ```text
     <InputDirectoryName>_credentials.txt
     ```  
   - The file is located in the current working directory.

---

### **Example Output**  
For a file with the following entries:  
```
URL: https://example.com  
Username: user1  
Password: pass123  
```

The script generates:  
```
https://example.com|user1|pass123
```

---

### **Applications**  
- **Credential Analysis:** Helps analyze credential data for audits or investigations.  
- **Data Migration:** Formats credentials for easy migration to secure password managers.  
- **Cybersecurity Audits:** Assists in identifying and managing exposed credentials.  

This script is ideal for IT professionals, auditors, and penetration testers handling sensitive information efficiently!
