import os

# Specify the directory containing your source files
source_dir = "src/iOS"

# List to store the file paths
sources = []

# Walk through the directory and collect .cpp and .m files
for root, dirs, files in os.walk(source_dir):
    for file in files:
         sources.append(os.path.join(root, file))

# Print the source files as a CMake variable
print("set(SOURCES " + " ".join(sources) + ")")
