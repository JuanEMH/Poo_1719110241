class cajero: 
  def __init__(self,ID_cajero,codigo,datos_ingresados,registro,red_bancaria ):
    self.ID_cajero=ID_cajero
    self.codigo=codigo
    self.datos_ingresados=datos_ingresados
    self.registro=registro
    self.red_bancaria=red_bancaria
    
class caj_bancomer(cajero):
  def ban (self):
    print("***BBVA***")

class caj_banamex(cajero):
  def mex (self):
    print("***BANAMEX**")
 

class caj_HSBC(cajero):
  def HSB (self):
    print("***HSBC***")

class caj_santander(cajero):
  def santan (self):
    print("***SANTANDER***")


cajero_1=caj_banamex("...ID-171911...","BAN194...","NOMBRE_APELLIDO...","CARNET...","RED-BANAMEX...")
cajero_1.mex()
print(cajero_1.ID_cajero,cajero_1.codigo,cajero_1.datos_ingresados,cajero_1.registro,cajero_1.red_bancaria)

cajero_2=caj_bancomer("...ID-59874...","BBVA-879...","NOMBRE_APELLIDO...","CARNET-845...","RED-BANCONMER...")
cajero_2.ban()
print(cajero_2.ID_cajero,cajero_2.codigo,cajero_2.datos_ingresados,cajero_2.registro,cajero_2.red_bancaria)

cajero_3=caj_HSBC("...ID/598...","HSBC//587...","JUAN HERNANDEZ...","CARNET-JH98...","RED-HSBC...")
cajero_3.HSB()
print(cajero_3.ID_cajero,cajero_3.codigo,cajero_3.datos_ingresados,cajero_3.registro,cajero_3.red_bancaria)

cajero_4=caj_santander("...ID/598...","HSBC//587...","DIEGO HERNANDEZ...","CARNET6587...","RED-SANTANDER...")
cajero_4.santan()
print(cajero_4.ID_cajero,cajero_4.codigo,cajero_4.datos_ingresados,cajero_4.registro,cajero_4.red_bancaria)