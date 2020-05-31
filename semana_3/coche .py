class avion: 
  def __init__(self, tipo, modelo, transportar ,carga ,auxilio, accion):
    self.tipo=tipo
    self.modelo=modelo
    self.transportar=transportar
    self.carga=carga
    self.auxilio=auxilio
    self.accion=accion
  
class elicoptero(avion):
  def elicoptero (self):
    print("**el elicoptero ayuda**")

class jet(avion):
  def jet (self):
    print("**jet de combate**")
  
class cargero(avion):
  def cargero (self):
    print("**cargero**")

class privado(avion):
  def privado (self):
    print("**avion publico**")

class avioneta(avion):
  def avioneta (self):
    print("**auxiliar**")