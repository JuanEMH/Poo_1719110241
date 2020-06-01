class banco:
  nombre="*santander"
  cajeros="*11 cajeros"
  tarjetas="*devito y credito"
  horarios="*9:00am a 4:00pm"
  lugar="*floresta"
  direccion="*centro"
  cubiculos="*30 cubiculos"
  empleados="*30 empleados"
  ventanillas="*12 ventanillas"
  tramites="*pagares, depositos y transferencias"
  def retirar (self):
    print("Retirar")
  def depositar (self):
    print("Depositar")
  def transferir (self):
    print("Transferir")
  def abonar (self):
    print("Abonar")
  def pagar_servicios_(self):
    print("Pagar servicios ")
ban=banco()
ban.retirar()
ban.depositar()
ban.transferir()
ban.abonar()
ban.pagar_servicios_()
print(ban.nombre)
print(ban.cajeros)
print(ban.cubiculos)
print(ban.lugar)
print(ban.tarjetas)
print(ban.tramites)
print(ban.horarios)
print(ban.direccion)
print(ban.ventanillas)
print(ban.empleados)