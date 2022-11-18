# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("/nPROGRAM KONVERSI TEMPERATURE/n")

celcius = float(input('Masukan suhu dalam celcius')) 
print("suhu adalah",celcius,"Celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dala reamur adalah",reamur,"Reamur")


# fahrenheit
fahrenheit = ((9/5) * celcius)+32
print("suhu dala fahrenheit adalah",fahrenheit, "Fahrenheit")


#Kelvin
kelvin = celcius + 32
print("suhu dalam kelvin adalah",kelvin,"Kelvin")
