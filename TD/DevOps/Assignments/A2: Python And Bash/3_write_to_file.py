"""
3. Write to a File
Create a text file and write some content to it.
Uses file functions: open() and write().
"""

# Open file in write mode (creates file if it doesn't exist)
file = open("sample_content.txt", "w")

# Write content to the file
file.write("Hello, this is content written by the Python program.\n")
file.write("Assignment A2: Python and Bash - Write to File.\n")
file.write("We used open() and write() to create and write to this file.\n")

# Close the file when done
file.close()

print("Content has been written to 'sample_content.txt'.")
