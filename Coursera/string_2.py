  # program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# Use words.txt as the file name
fname=raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
        prt =  line.upper()
        print prt.strip()
