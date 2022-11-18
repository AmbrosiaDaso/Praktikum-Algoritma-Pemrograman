#Latihan

#kalkulator sederhana
print(20*"=")
print("kalkulator sederhan")
print(20*"="+"\n")

angka_1 = float(input("masukan angka 1 ="))
operator = input("oprerator(+,-,x,/):")
angka_2 = float(input("masukan angka 2 ="))

#percabangannya
if operator=="+":
   hasil = angka_1 + angka_2
   print(f"hasilnya adalah {hasil}")
elif operator == "-":
   hasil = angka_1 - angka_2
   print(f"hasilnya adalah {hasil}")
elif operator =="/":
   hasil = angks_1 / angka_2
   print(f'hasilnya adalah {hasil}')
else:
    print("masukan yang bener dong! aku pusying")

print("akhir dari program'terima gajih!")