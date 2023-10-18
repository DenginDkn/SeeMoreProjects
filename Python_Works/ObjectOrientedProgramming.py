#%%
class Araba():
    renk = "Kırmızı"
    korna = "biip"

ford = Araba()
toyota = Araba()

print(ford.korna)
print(ford.renk)
print(toyota.korna)
print(toyota.renk)
# %%

ford.renk ="mavi"

print(ford.korna)
print(ford.renk)
print(toyota.korna)
print(toyota.renk)

# %%
class Araba():    

    renk = ["Kırmızı", "Mavi", "Yeşil"]
    

ford = Araba()
toyota = Araba()

#%%
print(ford.renk)
print(toyota.renk)

# %%

ford.renk.append("Siyah")
# %%
print(ford.renk)
print(toyota.renk)

# %%
class Araba():    
    def __init__(self):
       self.renk = ["Kırmızı", "Mavi", "Yeşil"]
    

ford = Araba()
toyota = Araba()


# %%
print(ford.renk)
print(toyota.renk)
# %%
ford.renk.append("Siyah")
# %%
print(ford.renk)
print(toyota.renk)

# %%

# *-- Parametre ile __init__' e Değer Atama
class Araba():
    def __init__(self, color, year):
        self.renk = ["Turuncu", "Beyaz"]
        self.yil = year
        self.renk.append(color)


ford = Araba("Siyah", 2016)
toyota = Araba("Mavi", 2018) 

print(ford.yil)
print(toyota.yil)

# %%
class Kopek():  
    ses= "hav hav"
    def havla(self):
        print(self.ses)


# %%
karabas = Kopek()
karabas.havla()
# %%

# *-- MİRAS
class Kedigil():
    def ses(self):
        print('miyav')
        
class Kedi(Kedigil):   # Kedigil Sınıfndan miras
    cins = 'Van'
    
mestan = Kedi()

mestan.ses()  
mestan.cins
print('mestan.cins: ', mestan.cins)

#%%
aslan = Kedigil()
aslan.ses()

# %%
# *-- ÇOK BİÇİMLİLİK (polymorphism)
print(len("Programlama"))
print(len(["Çarşamba", "Perşembe", "Cuma"]))
print(len({"Ad": "Zafer", "yaş": 53}))