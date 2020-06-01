class futbolista:
  nombre="*chicharito"
  numero="*11"
  posicion="*delantero"
  nacimiento="*1899"
  edad="*31 años"
  altura="*1.62 cm"
  tes="*morena"
  cabello="*pelon"
  ojos="*negros"
  sexo="*hombre"
  def delantero (self):
    print("delantero")
  def correr (self):
    print("correr")
  def barrerse (self):
    print("barrerse")
  def cabesear (self):
    print("cabesear")
  def selebrar(self):
    print("selebrar")
est=futbolista()
print(est.nombre)
print(est.numero)
print(est.posicion)
print(est.nacimiento)
print(est.edad)
print(est.altura)
print(est.tes)
print(est.cabello)
print(est.ojos)
print(est.sexo)
est.delantero()
est.correr()
est.barrerse()
est.cabesear()
est.selebrar()