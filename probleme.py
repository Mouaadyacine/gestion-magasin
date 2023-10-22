cln = []
cla = []

for i in range(3):
    cln.append(input(f"enter FULLNAME For client number [{i+1}]: "))
    Artn = int(input(f"enter number of ARTICLEs for client [{i+1}]: "))
    
    s = 0
    for j in range(Artn):
        ht = float(input(f"enter the price for article number[{j+1}]: "))
        s=s+ht
    TVA = s * 15 / 100
    TTC = s + TVA 
    total = TTC - TTC * 2/100

    cla.append(total)

print("_________________________")
print("        FACTURE")
print("_________________________")
for i in range(3):
    print("Total amount for client [ ",cln[i],"] is : ",cla[i],"DH")