class avion:
  color="gris..."
  llanatas="16 llantas..."
  turbinas="5 turbinas..."
  modelo="boing07..."
  ventanas="30 ventanilas..."
  velocidad="1040 kilómetros por hora..."
  peso="397.000 kilos..."
  capasidad="180 pasajeros..."
  cabinas="4 cabinas..."
  pilotos="2 pilotos..."
  def acelerar(self):
    print("Acelerar")
  def volar (self):
    print("Volar")
  def aterrizar(self):
    print("Aterrizar")
  def cargar (self):
    print("llevar mercansia")
  def comercial(self):
    print("Levar pasajeros")
avi=avion()
avi.acelerar()
avi.aterrizar()
avi.volar()
avi.cargar()
avi.comercial()
print(avi.color,avi.capasidad,avi.cabinas,avi.turbinas,avi.pilotos)
print(avi.peso,avi.modelo,avi.llanatas,avi.ventanas,avi.velocidad)