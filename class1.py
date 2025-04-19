import os

def search_in_files(directory, keyword):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        if keyword.lower() in line.lower():
                            print(f"[+] Found in: {file_path} (Line {line_num})")
            except Exception as e:
                print(f"[-] Could not read file: {file_path}. Reason: {e}")

# Set your directory and keyword
directory_to_search = "sany"
keyword_to_find = "sixgill"

search_in_files(directory_to_search, keyword_to_find)
