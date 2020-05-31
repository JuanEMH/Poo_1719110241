class calculadora:
 
  tipo="cientifica"

  def suma(self):
        print("sumar")

  def multi(self):
        print("multiplicar")

  def res(self):
        print("restar")

  def div(self):
        print("divide")

  def potencias(self):
        print("saca potencias")

class casio(calculadora):
  marca="***casio***"
  def graficas(self):
    print("grafica")

class patito(calculadora):
  marca="***Patito***"
  def graficas(self):
    print("No funcionan graficas")



cal=casio()
print(cal.marca)
cal.graficas()
cal.div()
cal.suma()
cal.res()
cal.multi()
cal.potencias()

cal=patito()
print(cal.marca)
cal.graficas()
cal.div()
cal.suma()
cal.res()
cal.multi()
cal.potencias()
  

