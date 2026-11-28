teks = input()
teks_inv = ""
for i in range(len(teks)):
    if teks[i].islower():
        teks_inv = teks_inv + teks[i].upper()
    else:
        teks_inv = teks_inv + teks[i].lower()
print(teks_inv)