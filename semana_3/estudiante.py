class estudiante: 
  def __init__(self, nombre, altura, edad,c_piel,c_ojos,):
    self.nombre=nombre
    self.altura=altura
    self.edad=edad
    self.c_piel=c_piel
    self.c_ojos=c_ojos

class femenino(estudiante):
  def fem (self):
    print("SOY ALUMNA")

class masculino(estudiante):
  def mas (self):
    print("SOY ALUMNO")

estudi = femenino("...Mariana...", "1.40 cm...", "20 años...","guero","azules")
estudia = masculino("...Diego...", "mido 1.70 cm...", "22 años...","blaco...","cafes...")
estudia.mas()
print (estudia.nombre,estudia.edad, estudia.altura)
estudi.fem()
print (estudi.nombre,estudia.edad, estudia.altura)
