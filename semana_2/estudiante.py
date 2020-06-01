class estudiante:
  nombre="*Juan"
  apellido="*Elias"
  apellido2="*Melo"
  nacimiento="*1998"
  edad="*21 años"
  altura="*1.54 cm"
  tes="*morena"
  cabello="*negro"
  ojos="*cafes"
  sexo="*hombre"
  def estudiar (self):
    print("estudiar")
  def dormir (self):
    print("dormir")
  def comer (self):
    print("comer")
  def bañarse (self):
    print("bañarse")
  def trabajar(self):
    print("trabajar")
est=estudiante()
print(est.nombre)
print(est.apellido)
print(est.apellido2)
print(est.nacimiento)
print(est.edad)
print(est.altura)
print(est.tes)
print(est.cabello)
print(est.ojos)
print(est.sexo)
est.estudiar()
est.dormir()
est.comer()
est.bañarse()
est.trabajar()