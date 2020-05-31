class banco: 
  def __init__(self, pagos, transferencias,atencion_al_cliente,saldos,pagares,):
    self.pagos=pagos
    self.transferencias=transferencias
    self.atencion_al_cliente=atencion_al_cliente
    self.saldos=saldos
    self.pagares=pagares

class bancomer(banco):
  def ban (self):
    print("BBVA")

class banamex(banco):
  def mex (self):
    print("BANAMEX")

class HSBC(banco):
  def HSB (self):
    print("HSBC")

class santander(banco):
  def santan (self):
    print("SANTANDER")

banco=bancomer("...pagos...","transferencias...","atencion_al_cliente...","saldos...","pagares...")
banco.ban()
print (banco.pagos,banco.transferencias,banco.atencion_al_cliente,banco.saldos,banco.pagares)

banco=banamex("...pagos...","transferencias...","atencion_al_cliente...","saldos...","pagares...")
banco.mex()
print (banco.pagos,banco.transferencias,banco.atencion_al_cliente,banco.saldos,banco.pagares)

banco=HSBC("...pagos...","transferencias...","atencion_al_cliente...","saldos...","pagares...")
banco.HSB()
print (banco.pagos,banco.transferencias,banco.atencion_al_cliente,banco.saldos,banco.pagares)

banco=santander("...pagos...","transferencias...","atencion_al_cliente...","saldos...","pagares...")
banco.santan()
print (banco.pagos,banco.transferencias,banco.atencion_al_cliente,banco.saldos,banco.pagares)