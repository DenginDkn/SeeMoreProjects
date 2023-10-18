#%%
ad= input("ismin nedir? ")
print("Merhaba " ,ad)
# %%
yas = input("Yasiniz ?")

yas_toplam = int(yas) + 3
print(yas_toplam)
#%%
x , y = 5 , 10
if x < y :
  print("x, y den kucuktur.")
  print("her zaman calisir")
  
# %%
cevap = int(input("5+5 nedir ?"))
if cevap  == 10:
  print("Dogru cevap tebrikler.")
  
print("Cevap yanlis tekrar deneyiniz.")
# %%
x , y , z= 5 , 10 , 5
if x < y and x == z:
  print(" her iki kosulda dogrudur.")
  
#%%
x , y , z= 5 , 10 , 5
if x < y or x != z:
  print(" Bir veya daha fazla kosul dogru.")
  
#%%
durum = False
if not durum:
  print("durum: false")

# %%
kelime = "Basketbol"
if "b" in kelime:
  print("{} kelimesinde b karakteri vardir.".format(kelime))
  
# %%
# *-- "not in" Operatörü
kelime = "Basketbol"
if "x" not in kelime:
      print( f"{kelime} kelimesi x karakteri barındırmıyor")
# %%
# *-- elif  
x, y = 5, 10
if x > y:
      print("x büyüktür")
elif x < y:
      print("x küçüktür")

# %%
x= int(input("x: "))
y= int(input("y: "))

if x > y:
      print("x büyüktür")
elif (x + 10) < y:
      print("y 15'den büyük ")
elif (x + 5) == y: 
      print("eşit")  
# %%
# *-- Çoklu Koşul
x, y, z = 5, 10, 5
if x > y:
      print("büyüktür")
elif x <= y:
      if x == z:
         print("x, z'ye eşittir") 
      elif x != z:
         print("x, z'ye eşit değildir") 