#%%
def mesaj ():
  print("Merhaba herkese")
  
  #%%
  mesaj()
  #%%
def hesap():
    x , y = 5 , 10
    print(x+y)
    
# %%
hesap()

#%%
def hesap(a, b):    
    print(a+b)

#%%

hesap(5,12)

# %%
hesap(50,102)

# %%
def hesap(a, b):    
    
    return(a+b)
# %%
x = hesap(8,15)
print(x)
#%%
sayilar1= [2,4,5,10]
sayilar2= [1,5,6]

def karesi(sayilar):
  for sayi in sayilar:
    print(sayi**2)
    
    karesi(sayilar1)
    karesi(sayilar2)
# %%
def daire_alani(r,pi=3.14):
  alan=pi*(r**2)
  print("Alan: ",alan)
  daire_alani(2,3.145789)
  
  
  # *-- Opsiyonel Parametreler
def isim_yaz(ilk, son, orta=""):
        if orta:
            print( "{} {} {}".format(ilk, orta, son) )
        else:
            print( "{} {}".format(ilk, son) )
            

isim_yaz("Zafer", "Demirkol")
isim_yaz("Zafer", "Demirkol", "Ege") 

# *-- Parametre İsmi ile Değer Atamak
def sayilar(sayi1, sayi2):
    print(sayi2)
    print(sayi1)

sayilar(5,  sayi2 = 2.5)

# %%
# *-- args
# args tuple tipindedir
def isim_yazdir(isim, *args):
    # print(type(args))
    print(isim)

    for arg in args:
        print(arg)

isim_yazdir("Zafer Demirkol", 5, True, "Ege")
isim_yazdir("Zafer Demirkol", 5, True, "Ege", "ayşe")
# %%
# *-- Ternary Operator / Kısayol Koşul İfadesi
def aramaListesi(liste, el):
    return True if el in liste else False

sonuc = aramaListesi([ "bir", 2, "üç" ], 2) 
print(sonuc)

# if el in liste:
#      return True
#  else:
#     return False