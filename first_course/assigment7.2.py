# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
spam = 0
counter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    position = line.find(": ")
    number = float(line[position + 2: ])
    spam += number
    counter += 1
    
   
print("Average spam confidence:", spam/counter)