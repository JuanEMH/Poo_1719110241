class vacasiones:
  playa="playas"
  pueblomagico="pueblo magico"
  piramides="piramides"
  campo="bosques"
  def desestresar1 (self):
    print ("tomar el sol") 
  def desestresar2 (self):
    print ("acampa")
  def desestresar3 (self):
    print ("ecala")
  def desestresar4 (self):
    print ("monta")
  def desestresar5 (self):
    print ("nada")

class cancun(vacasiones):
  cancun="***cancun mexico***"
  def visita (self):
    print("visita las islas")
  def nada (self):
    print("nada en las posas")
  def ve (self):
    print("visitar antros")
  def jugar (self):
    print ("juega pelota")

class teotihuacan(vacasiones):
  teotihuacan="***teotihuacan***"
  def subir(self):
    print ("sube a las piramides")

class pueblo(vacasiones):
  real="***real del monte***"
  def comer(self):
    print ("comer pastes")
  def visitar (self):
    print ("ve a las sonas turisticas")
  def dormir (self):
    print ("visita las cabañas")

vaca=cancun()
print(vaca.cancun)
vaca.desestresar1()
vaca.desestresar2()
vaca.desestresar3()
vaca.desestresar4()
vaca.nada()
vaca.jugar()
vaca.ve()
vaca.visita()

vaca=teotihuacan()
print(vaca.teotihuacan)
vaca.desestresar1()
vaca.desestresar2()
vaca.desestresar3()
vaca.desestresar4()
vaca.subir()

vaca=pueblo()
print(vaca.real)
vaca.comer()
vaca.dormir()
vaca.visitar()
vaca.desestresar2()
vaca.desestresar3()
vaca.desestresar4()