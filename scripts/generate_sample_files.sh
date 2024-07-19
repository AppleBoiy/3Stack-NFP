#!/bin/bash

# Create a directory for sample files if it doesn't exist
mkdir -p sample_files

# Text file
echo "This is a sample text file for testing file uploads." > sample_files/example.txt

# PDF file (requires `brew install pdftk`)
echo "Sample PDF content." | text2pdf > sample_files/example.pdf

# Executable file (simple script)
echo '#!/bin/bash' > sample_files/example.sh
echo 'echo "Hello, this is an executable file!"' >> sample_files/example.sh
chmod +x sample_files/example.sh

# Rename example.sh to example.exe (simulate an executable file)
mv sample_files/example.sh sample_files/example.exe

# PNG image file (simple 1x1 pixel image)
echo -n -e '\x89PNG\r\n\x1a\n\0\0\0\rIHDR\0\0\0\x01\0\0\0\x01\x08\x06\0\0\0\x1f\x15\xc4\x89\0\0\0\nIDAT\x08\xd7c\xf8\xff\x00\0\1\0\1\5\0\0\0?\x0c\x1b\0\0\0\0IEND\xaeB`\x82' > sample_files/example.png

echo "Sample files generated in sample_files directory:"
ls -l sample_files
