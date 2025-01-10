# Logs-Sorter-ULP-
Read the File and Key Features of the Script
This script is designed to extract and reformat sensitive information (like URLs, usernames, and passwords) from specific log files. Below is an explanation of how it works and its key features.

Key Features
Automated File Traversal:
The script automatically scans the selected directory and subdirectories for target files, reducing manual effort.

Pattern Matching with Regular Expressions:
Extracts data using robust regular expressions, ensuring flexibility and accuracy.

Dynamic Output File Naming:
The output file name is based on the input directory's name, making it easy to identify the source of extracted data.

Error Resilience:
Gracefully handles errors, such as file encoding issues or missing patterns, and logs the errors for debugging.

User-Friendly Interface:
Utilizes Tkinter to provide a graphical interface for directory selection, making it accessible to non-technical users.

Scalability:
Can handle large datasets with multiple subdirectories and files.

Formatted and Readable Output:
Outputs credentials in a structured format (URL|username|password) that can be directly used or parsed by other tools.

Cross-Platform Compatibility:
Built using standard Python libraries (os, re, tkinter), ensuring compatibility across Windows, macOS, and Linux.

Here’s a **checklist** of requirements and steps to run this script, formatted as a box list for clarity:

---

### **📋 Requirements to Run the Script**

1. **✅ Python Environment**
   - **Python 3.6+** installed on your system.
   - Verify installation:  
     ```bash
     python --version
     ```

2. **✅ Pre-Installed Python Libraries**
   - `os`: For directory and file operations.
   - `re`: For regular expression matching.
   - `tkinter`: For the GUI file selection dialog.

   **Note for Linux Users:** Install `tkinter` if missing:
   ```bash
   sudo apt-get install python3-tk
   ```

3. **✅ Supported Operating Systems**
   - Windows
   - macOS
   - Linux

4. **✅ Target Log Files**
   - Files named `All Passwords.txt` or `Passwords.txt` must be present in the selected directory.

5. **✅ Output File Storage**
   - Ensure write permissions for the directory where the output file will be saved.

---

### **📦 Steps to Run the Script**

1. **💻 Install Python (if not installed):**
   - Download and install from [python.org](https://www.python.org/downloads/).

2. **📂 Save the Script:**
   - Save the script as `CredExtractor.py` (or any other name) in a desired directory.

3. **📜 Prepare Log Files:**
   - Place files (`All Passwords.txt` or `Passwords.txt`) in a directory.

4. **🔧 Optional: Set Up a Virtual Environment (Recommended):**
   - Create and activate a virtual environment:
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows: .\env\Scripts\activate
     ```

5. **▶ Run the Script:**
   - Navigate to the script's directory and execute:
     ```bash
     python CredExtractor.py
     ```

6. **📂 Select Directory:**
   - Use the graphical prompt to select the folder containing the log files.

7. **✅ View Results:**
   - Extracted credentials will be saved to a file named:
     ```
     <InputDirectoryName>_credentials.txt
     ```
   - Check the current working directory for the output file.

---
