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

aviones = elicoptero ("apache...", "boing...", "pasientes...", "suministros...", "desastres...","volar...",)
aviones.elicoptero()
print (aviones.tipo, aviones.modelo, aviones.transportar, aviones.carga, aviones.auxilio,aviones.accion)

aviones = jet ("...comboy...", "municion...", "armamento...", "ajentes...", "ataca...","combate...",)
aviones.jet()
print ( aviones.modelo, aviones.transportar, aviones.carga, aviones.auxilio,aviones.accion,aviones.tipo,)

aviones = cargero ("comboy...", "...municion...", "armamento...", "ajentes...", "ataca...","transporta civiles...",)
aviones.cargero()
print ( aviones.modelo, aviones.transportar, aviones.carga, aviones.auxilio,aviones.accion,aviones.tipo,)

aviones = privado ("...comboy...", "civiles...", "paqueteria...", "vuela mas rapido...","privado...","trasporta personal",)
aviones.privado()
print ( aviones.modelo, aviones.transportar, aviones.carga,aviones.accion,aviones.tipo,)

aviones = avioneta ("...comboy...", "...civiles...", "paqueteria...", "vuela mas rapido...","privado...","trasporta personal",)
aviones.avioneta()
print ( aviones.transportar, aviones.carga,aviones.accion,aviones.modelo,)