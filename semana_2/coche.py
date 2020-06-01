class carro:
  nombre="*ferrari"
  tipo="*deportivo"
  color="*rojo"
  año="*2019"
  llantas="*4 llantas"
  velocidadmaxima="*350hm/h"
  combustible="*gasolina verde"
  cilindros="*12 cilindros"
  velocidad="*Acelera de 0 a 100 km/h en 2,9 segundos"
  duracion="15,4 litros a los 100 kilómetros"
  def acelerar (self):
    print("acelerar")
  def frenar (self):
    print("frenar")
  def turbo (self):
    print("meter turbo")
  def arrancar (self):
    print("arrancar")
  def sonar(self):
    print("estacionarce solo")
carr=carro()
print(carr.nombre)
print(carr.tipo)
print(carr.color)
print(carr.año)
print(carr.llantas)
print(carr.velocidadmaxima)
print(carr.combustible)
print(carr.cilindros)
print(carr.velocidad)
print(carr.duracion)
carr.acelerar()
carr.frenar()
carr.turbo()
carr.arrancar()
carr.sonar()