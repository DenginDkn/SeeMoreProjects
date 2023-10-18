# /// Author DenginDkn ///
#%%

# Mathematical Operators
x,y = 3,2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)

print(x%y)
print(-x)
print(int(3.9))
print(float(x))
print(x**y)
 
 
 #%%
# Boolean Operators
x = 1 > 2
print(x)
#False

y = 2 > 1
print(y)
#True

x,y = True, False

print((x or y )== True)

print((x and y )== False)

print((not y )== True)

#%%
# String Opearators

ad1= "Dengin"
print('ad:' , ad1)

ad2= "Şimay"
print('ad:' , ad2)

soyAd= "Diken"
print(ad1+ ' ' +soyAd)

#%%
# Format Method
ad = 'Dengin'

print('Merhaba {}'.format(ad))
print('Merhaba {}, {} yaşındasın!'.format(ad,22))

#%%
# F String Methodu  LAST MODEL Current

print(f'Merhaba {ad}, {28} yasindasin!')

ad='Dengin'
soyad='Diken'

print(f'Merhaba {ad} {soyad}')

x=1.546454236
print(f"Deger :{x:.2f}")

#%%
6 == "6"

# *  Important String Methods
y = '    Bugün hava çok güzel.     '
print(y)
print(y.strip())
#%%
# Başta ve sondaki boşlukları alır'
print('ByBye'.upper())
#%%
print('akıllıTelefon'.startswith('akıllı'))
#True
print('akıllıTelefon'.endswith('Telefon'))
# True
print('herbiri'.find('biri'))
# index:3
print("spor".replace("sp", "z"))
# zor
print(len("zafer "))
print("af" in "zafer")
#  True


#%%
# *-- Liste yapısı
sayilar = [1,5,9]
gunler = ["p.tesi","Salı","Çarşamba"]
karma =["zafer",52, "İstanbul", True]

print(sayilar[0])
print(gunler[-2])

# *-- String index
mesaj = "Merhaba"
print(mesaj[0])
print(mesaj[1])
print(mesaj[-1])

# %%
# *-- Dilimleme
print(mesaj[0:2])
#Me
# degisken_ismi[ start : stop : step ]
mesaj = "Merhaba bugün hava çok güzel."
print(mesaj[0:5:2])

#%%
l = [1, 2, 2]
print(len(l))
# 3



#%%
# **-- append 
x = [1, 2, 3]
x.append([4, 5])
print(x)

#%%
# **-- clear 
l.clear()
print(l)


#%%
# *-- Extend
x = [1, 2, 3]
x.extend([4, 5])
print(x)


#%%
# **-- Insert **
l = [1, 2, 4]
l.insert(1, 3) #Birinci indekse 3 ekle
print(l)
#[1, 3, 2, 4]


#%%
# *-- Liste birleştirme 
print([1, 2, 2] + [4])
#[1, 2, 2, 4]


#%%
# *-- Eleman Çıkarma 
# *-- Pop
l.pop()

# *-- remove
l = [1, 2, 2, 2, 4]
l.remove(2) #ilk bulduğu değeri çıkarır
print(l)
# [1, 2, 2, 4]