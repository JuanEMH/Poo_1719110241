class calculadora:
  nombre="*casio"
  teclas="*alfa numericos"
  pantalla="*pantalla de tinta"
  tipo="*cientifica"
  modelo="*258dg"
  bateria1="*pilas"
  bateria_2="*solar"
  forma="*rectangular"
  tiempo="*dos años de vida sin cambiar pilas"
  color="*negra"
  def sumar (self):
    print("sumar")
  def restar (self):
    print("restar")
  def dividir (self):
    print("dividir")
  def multiplicar (self):
    print("multiplicar")
  def graficar(self):
    print("graficar")
cal=calculadora()
print(cal.nombre)
print(cal.teclas)
print(cal.pantalla)
print(cal.tipo)
print(cal.modelo)
print(cal.bateria1)
print(cal.bateria_2)
print(cal.forma)
print(cal.tiempo)
print(cal.color)
cal.sumar()
cal.restar()
cal.dividir()
cal.multiplicar()
cal.graficar()