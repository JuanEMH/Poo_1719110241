class futbolista:
  seleccion="***mexicana***"
  
  
  def __init__(self, altura, edad,):
    self.altura=altura
    self.edad=edad
  def correr (self):
    print("corre por el balon")

  def porter(self):
    print("proteje la porteria")    
  
class chicharito(futbolista):
  nombre="chicharito"
  
  def delantero(self):
    print("delantero")
  def chicharito (self):
    print("chicharito")
  def numero (self):
    print("Num 5")

class osvaldo(futbolista):
  nombre= "osvaldo"
  def portero (self):
    print("portero")
  def osvaldo (self):
    print("osvaldo")
  def numero (self):
    print("Num 10")

class ochoa(futbolista):
  nombre= "ochoa"
  def portero (self):
    print("suplente")
  def ochoa (self):
    print("ochoa")
  def numero (self):
    print("Num 1")

class aguirre(futbolista):
  nombre= "aguirre"
  def posicion (self):
    print("director tecnico")
  def aguirre (self):
    print("aguirre")
  def numero (self):
    print("S/N")

fut=chicharito("1.75 cm...", "38 años...")
print(fut.seleccion)
fut.delantero()
fut.correr()
fut.chicharito()
fut.numero()
print(fut.altura,fut.edad)

fut=osvaldo("1.60 cm...", "33 años...")
print(fut.seleccion)
fut.portero()
fut.porter()
fut.osvaldo()
fut.numero()
print(fut.altura,fut.edad)

fut=ochoa("1.78 cm...", "36 años...")
print(fut.seleccion)
fut.portero()
fut.porter()
fut.ochoa()
fut.numero()
print(fut.altura,fut.edad)

fut=aguirre("1.60cm...", "52 años...")
print(fut.seleccion)
fut.posicion()
fut.aguirre()
fut.numero()
print(fut.altura,fut.edad)
