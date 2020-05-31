class carro: 
  accion="**corren y frenan**"
  def __init__(self, color, año, capasidad ,kilometraje,):
    self.color=color
    self.año=año
    self.capasidad=capasidad
    self.kilometraje=kilometraje
    
  
class ferrary(carro):
  def ferrary (self):
    print("****Ferrary deportivo****")

class camaro(carro):
  def camaro (self):
    print("****Camaro deportivo****")
  
class Honda(carro):
  def honda (self):
    print("****Honda semideportivo****")

class tsuru (carro):
  def tsuru (self):
    print("*****Tsuru particular****")

class combi (carro):
  def combi (self):
    print("****Combi de ransporte****")


carr=ferrary("...Rojo...","2019...","2 personas...","0 a 300 en 5 seg...",)
carr.ferrary()
print(carr.accion)
print(carr.color,carr.año,carr.capasidad,carr.kilometraje)

carr=camaro("...Azul...","2018...","4 personas...","0 a 200 en 5 seg...",)
carr.camaro()
print(carr.accion)
print(carr.color,carr.año,carr.capasidad,carr.kilometraje)

carr=Honda("...Rojo...","2019...","4 personas...","0 a 100 en 4seg")
carr.honda()
print(carr.accion)
print(carr.color,carr.año,carr.capasidad,carr.kilometraje)

carr=tsuru("...verde...","1998...","4 personas...","velocidad media",)
carr.tsuru()
print(carr.accion)
print(carr.color,carr.año,carr.capasidad,carr.kilometraje)

carr=combi("...Rojo...","año 2000...","10 personas...","0 a 300 en 5 seg...",)
carr.combi()
print(carr.accion)
print(carr.color,carr.año,carr.capasidad)