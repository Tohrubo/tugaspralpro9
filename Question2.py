print("Masukkan angka!")

nlist = []
chk = True
while chk:
    try:
        n = input(">")
        if n == "done":
            chk = False
        else:
            n = int(n)
            nlist.append(n)
    except:
        print("Invalid")
mx = max(nlist)
mn = min(nlist)
print(f"Angka terbesar adalah: {mx}")
print(f"Angka terkecil adalah: {mn}")