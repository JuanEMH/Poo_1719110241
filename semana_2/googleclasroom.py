class clasroom:
  año="*2014"
  color1="*verde"
  color2="*amarillo"
  color3="*blanco"
  logo="*persona minimalista"
  empresa="*goolge"
  dispositivos="*celular y computadora"
  pestanas="*desplegables"
  calendario="*1 calendario"
  tablon="*tablones"
  def pu_tarea (self):
    print("publicar tarea")
  def daranuncios (self):
    print("publicar")
  def calificar (self):
    print("calificar")
  def video (self):
    print("video llamadas")
  def subir(self):
    print("subir archivos")
est=clasroom()
print(est.año)
print(est.color1)
print(est.color2)
print(est.color3)
print(est.logo)
print(est.empresa)
print(est.dispositivos)
print(est.pestanas)
print(est.calendario)
print(est.tablon)
est.pu_tarea()
est.daranuncios()
est.calificar()
est.video()
est.subir()