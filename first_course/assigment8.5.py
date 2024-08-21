fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From"):
        lista = line.split()
        if len(lista)>2:
            print(lista[1])
            count += 1
    else:
        continue


print("There were", count, "lines in the file with From as the first word")
