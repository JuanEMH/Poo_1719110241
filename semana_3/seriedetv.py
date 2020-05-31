class serie_tv:
  def genero (self):
    print ("terror")
  def genero_1 (self):
    print ("accion")
  def genero_2(self):
    print ("documental")
  def genero_3 (self):
    print ("ficcion")
  def genero_4 (self):
    print ("drama")
    

class netflix(serie_tv):
  compañia="Netflix"
  color="Rojo"
  def parametro (self):
    print("**auto correccion")
  def recomendaciones (self):
    print("**recomienda contenido")
  def menus (self):
    print("**te otorga categorias")
  def notificasiones (self):
    print ("**notificaciones")

class HBO(serie_tv):
  compañia="HBO"
  color="Gris con negro"
  def parametro (self):
    print("**auto correccion")
  def recomendaciones (self):
    print("**recomienda contenido")
  def menus (self):
    print("**te otorga categorias")
  def notificasiones (self):
    print ("**notificaciones")

class Blim(serie_tv):
  compañia="Blim"
  color="Blanco con azul"
  def parametro (self):
    print("**auto correccion")
  def recomendaciones (self):
    print("**recomienda contenido")
  def menus (self):
    print("**te otorga categorias")
  def notificasiones (self):
    print ("**notificaciones")

serie=netflix()
print (serie.compañia)
print (serie.color)
serie.genero()
serie.genero_1()
serie.genero_2()
serie.genero_3()
serie.genero_4()
serie.recomendaciones()
serie.parametro()
serie.notificasiones()
serie.menus()

serie=HBO()
print (serie.compañia)
print (serie.color)
serie.genero()
serie.genero_1()
serie.genero_2()
serie.genero_3()
serie.genero_4()
serie.recomendaciones()
serie.parametro()
serie.notificasiones()
serie.menus()

serie=Blim()
print (serie.compañia)
print (serie.color)
serie.genero()
serie.genero_1()
serie.genero_2()
serie.genero_3()
serie.genero_4()
serie.recomendaciones()
serie.parametro()
serie.notificasiones()
serie.menus()