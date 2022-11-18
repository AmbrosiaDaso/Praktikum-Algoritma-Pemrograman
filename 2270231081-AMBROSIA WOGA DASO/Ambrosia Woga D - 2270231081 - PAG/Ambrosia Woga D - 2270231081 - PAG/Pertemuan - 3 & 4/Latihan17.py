#width and multiline
#data
data_nama = "ucup surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

#string standard
data_string = f"nama = {data_nama}, umur ={data_umur}, tinggi ={data_tinggi}, sepatu ={data_nomor_sepatu}"
print("\n"+5*"="+"data string"+5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}"""

print("\n"+5*"="+"data string"+5*"=")
print(data_string)

#mengatur lebar
data_nama = "ucup surucup"
data_tinggi = 105.17
data_string = f"""
nama = {data_nama:>5}
umur = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""

print("\n"+5*"="+"data string"+5*"=")
print(data_string)
