class serietv:
  terror="*terror"
  accion="*accion"
  drama="*drama"
  ficcion="*ficcion"
  infantil="*infantil"
  horror="*horror"
  romantica="*romantica"
  triller="*triller"
  otros="*tros"
  blanco_y_negro ="*blanco y negro"

  def abrir_menu (self):
    print("abrir menu")
  def play (self):
    print("poner play")
  def stop (self):
    print("poner stop")
  def pausa (self):
    print("poner pausa")
  def abrir (self):
    print("abrir")
serie=serietv()
print(serie.terror)
print(serie.accion)
print(serie.drama)
print(serie.ficcion)
print(serie.infantil)
print(serie.horror)
print(serie.romantica)
print(serie.triller)
print(serie.otros)
print(serie.blanco_y_negro)
serie.abrir_menu()
serie.play()
serie.stop()
serie.pausa()
serie.abrir()