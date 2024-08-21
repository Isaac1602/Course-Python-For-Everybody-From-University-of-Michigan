# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for row in fh:
    rowstripped = row.strip()
    print(rowstripped.upper())