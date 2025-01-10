import os
import re
from tkinter import Tk
from tkinter.filedialog import askdirectory

def extract_and_reformat(input_directory, output_file):
    """
    Extract and reformat credentials from log files in the given directory.

    :param input_directory: str - The directory to search for log files.
    :param output_file: str - The file to save the extracted credentials.
    """
    # Regular expressions for extracting credentials
    url_pattern = re.compile(r"(URL|url):\s*(https?://[^\s]+|android://[^\s]+)", re.IGNORECASE)
    user_pattern = re.compile(r"(USER|Username|login):\s*([^\s]+)", re.IGNORECASE)
    pass_pattern = re.compile(r"(PASS|Password|password):\s*([^\s]+)", re.IGNORECASE)

    file_count = 0
    extracted_count = 0

    with open(output_file, 'a', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(input_directory):
            for file in files:
                try:
                    # Process only specific file names
                    if file.lower() in ["all passwords.txt", "passwords.txt"]:
                        file_count += 1
                        file_path = os.path.join(root, file)
                        print(f"[INFO] Processing file: {file_path}")

                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            url = user = password = None

                            for line in infile:
                                # Extract patterns
                                url_match = url_pattern.search(line)
                                user_match = user_pattern.search(line)
                                pass_match = pass_pattern.search(line)

                                if url_match:
                                    url = url_match.group(2)
                                if user_match:
                                    user = user_match.group(2)
                                if pass_match:
                                    password = pass_match.group(2)

                                # Write the formatted data when all components are found
                                if url and user and password:
                                    # Format the entry
                                    formatted_entry = f"{url}|{user}|{password}\n"

                                    outfile.write(formatted_entry)
                                    extracted_count += 1
                                    print(f"[EXTRACTED] {formatted_entry.strip()}")

                                    # Reset variables for the next entry
                                    url = user = password = None
                except Exception as e:
                    print(f"[ERROR] Failed to process {os.path.join(root, file)}: {e}")

    print(f"\n[SUMMARY] Processed {file_count} files. Extracted {extracted_count} credentials.")
    print(f"Data saved to {output_file}")

def main():
    """
    Main function to prompt the user for input directory and start the extraction process.
    """
    Tk().withdraw()  # Hide the Tkinter root window
    input_directory = askdirectory(title="Select the directory containing 'All Passwords.txt' or 'Passwords.txt'")

    if input_directory:
        # Generate output file path based on the directory name
        directory_name = os.path.basename(input_directory.rstrip(os.sep))
        output_file = os.path.join(os.getcwd(), f"{directory_name}_credentials.txt")
        extract_and_reformat(input_directory, output_file)
    else:
        print("No directory selected. Exiting.")

if __name__ == "__main__":
    main()
