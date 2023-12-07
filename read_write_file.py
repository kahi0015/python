# Write to a new (or overwrite an existing) file
with open("file_test", "w") as f:
    f.write("This is my first python file")

# Open and read that file
with open("file_test", "r") as f:
    print(f.read())

# Delete a file
import os

if os.path.exists("file_test_1"):
    os.remove("file_test_1")
else:
    print("The file does not exist!!")