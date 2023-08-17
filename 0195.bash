# Read from the file file.txt and output the tenth line to stdout.

head -10 file.txt | sed -n 10p
