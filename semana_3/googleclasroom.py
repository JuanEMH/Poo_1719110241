class google_classroom:
  colo1="amarillo"
  color2= "verde"
  color3="blanco"
  def video_llamadas (self):
    print("linck de llamadas")
  def publicar (self):
    print("publica tareas")
  def monitorear (self):
    print ("chequeo de tareas")
  def calificar (self):
    print("calificar")
  def calificaciones (self):
    print("mostrar la calificasion")
class Quizizz(google_classroom):
  marca="*****Quizizz*****"
  color="azul"
  def examen (self):
    print ("realiza examenes")
  def encuestas (self):
    print ("realiza encuestas")
  def puntuacion(self):
    print ("da puntuaciones")
  def imajen (self):
    print("http://www.eduforics.com/wp-content/uploads/2016/08/logo_5_orig.png")

class classFlow(google_classroom):
  marca="*****ClassFlow*****"
  color="negro" 
  def trabajo (self):
    print ("trabajo interactivio")
  def tablas (self):
    print ("hace tabla como power point")
  def imajen (self):
    print("http://www.eduforics.com/wp-content/uploads/2016/08/classflow-logo_2.png")  
quizz=Quizizz()
print(quizz.marca)
print(quizz.color, "y" ,quizz.color3)
quizz.encuestas()
quizz.examen()
quizz.puntuacion()
quizz.imajen()
quizz.monitorear()

clas=classFlow()
print(clas.marca)
print(clas.color, "y" ,clas.color3)
clas.trabajo()
clas.tablas()
clas.imajen()
clas.video_llamadas()
clas.calificaciones()
