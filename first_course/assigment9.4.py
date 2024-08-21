fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
    
fh = open(fname)
user = dict()

for line in fh:
    if line.startswith("From"):
        lista = line.split()
        if len(lista)>2:
            user[lista[1]] = user.get(lista[1], 0) + 1    
    else:
        continue
largest_word = ""
largest_value = 0
        
for key, value in user.items():
    if value >  largest_value :
        largest_value = value 
        largest_key = key
    else: continue

print(largest_key, largest_value)