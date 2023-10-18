#%%
# *-- Dictonary Tasarım Aşamasında Değer Atamak
musteriler = {
    "ad": "Zafer",
    "yaş": 53
}
print(type(musteriler))

# %%
print(musteriler["ad"])


# print(musteriler["meslek"])
print(musteriler.get("meslek" , "meslek alanı yok"))
# %%
# *-- LİSTELER VE DICTIONARY 
#  BİR DICTIONARY'Yİ LİSTE İÇİNDE SAKLAMAK VE ONA ERİŞMEK
data = ["Zafer", "Ege", { "ad": "Ayşe" }]
print(data[2])
print(data[2]["ad"])

#%%
#*-- DICTIONARY İÇİNDE DICTIONARY
data = {
    "takım": "liverpool",
    "kupa": { "2018": 1, "2017": 3 }
}
print(data["kupa"])
print( data["kupa"]["2018"] )

#%%
data = {
    "takım": "liverpool",
    "kupa": [ "2018", "2017" ]
}
print(data["kupa"])
print( data["kupa"][1] )

# %%

# *-- Yeni Veri Eklemek
araba = {"yıl": 2018}


araba["renk"] = "Mavi"


print("Yıl: {} \t Renk: {}".format( araba["yıl"], araba["renk"] ))
# %%

# *-- Değer Değiştirme
araba = {"yıl": 2018, "renk": "Mavi"}
araba["renk"] = "Kırmızı"
print("Yıl: {} \t Renk: {}".format( araba["yıl"], araba["renk"] ))
# *-- Eleman Çıkarma - del

araba = {"yıl": 2018}

#%%
try:
    del araba["yıl"]
    print(araba)
  
except:
    print("Böyle bir key yok")
    # *-- Dictionary ve Döngüler
personel = {"ad": "Zafer", "yas": 53}

for key in personel.keys():
        print(key)
        print( personel[key])

for value in personel.values():
  print( value)

# *-- TUPLE 
#  listeler gibidir ama değerleri değiştirilemez 
t1 = ("merhaba", 2, "zafer",2) # parantezle
t2 = True, 1  #parentezsiz

print(type(t1), type(t2)) 


# %%
print(t1[0])


# %%
dir(t1)
# %%
t1.count("ahmet")
# %%
t1.index("zafer")

# *-- SET
#%%
#  Set'ler sadece unique değerler  barındırırlar 
s1 = set([1, 2, 3, 1]) 
s2 = {4, 4, 5} 



print(type(s1), type(s2))
print(s1)
print(s2)

# %%
# *-- add()
s1.add(5) 
print(s1)
# %%
s1.remove(1)

# %%
print(s1)
#%%
f = open("test.txt", "w+")
f.write("Benim adım Zafer")
f.close()

#%%
f = open("test.txt", "r")
icerik = f.read()
f.close()

print(icerik)

#%%
from google.colab import drive
drive.mount('/content/drive')
