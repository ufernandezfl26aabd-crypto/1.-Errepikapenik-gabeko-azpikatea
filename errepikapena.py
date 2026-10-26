testua = "abcabcbb"
katea = ""
kontaketa = 0

for letra in testua:
    while letra in katea:
        katea = katea[1:]

    katea = katea + letra

    if len(katea) > kontaketa:
        kontaketa = len(katea)

print(kontaketa)