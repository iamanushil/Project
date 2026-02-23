"""
4. Read from a File
Open file in read mode and use file.read() to read and print the content.
"""

# Open file in read mode
file = open("sample_content.txt", "r")

# Read entire content and print
content = file.read()
print("--- Content of sample_content.txt ---")
print(content)

# Close the file when done
file.close()
