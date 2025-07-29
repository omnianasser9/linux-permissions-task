import os

# Replace 'your_file.py' with the actual filename you want to change permissions for
file_path = "your_file.py"

# Apply chmod 775 (rwxrwxr-x)
os.chmod(file_path, 0o775)

print(f"Permissions changed to 775 for file: {file_path}")
