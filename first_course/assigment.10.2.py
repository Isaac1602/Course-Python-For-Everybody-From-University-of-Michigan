fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
    
fh = open(fname)
user_hour = dict()


for line in fh:
    if line.startswith("From"):
        lista = line.split()
        
        if len(lista)>2:
            hour = lista[5].split(":")
            user_hour[hour[0]] = user_hour.get(hour[0], 0) + 1    
    else:
        continue
tuples = sorted([(hour, number) for hour, number in user_hour.items()])

for tuple_ in tuples :
    print(tuple_[0], tuple_[1])