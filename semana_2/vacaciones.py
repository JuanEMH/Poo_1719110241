class vacaciones:
  playa="*cancun"
  viajar="*playa"
  equipaje="*ropa y traje de baño"
  jugar="*pelota"
  tomar="*tomar el sol"
  arena="*hacer castillos"
  playa2="*nadar"
  isla="*islas"
  lanchas="*lanchas"
  canoas="*canoas"

  def descansar (self):
    print("descansar")
  def relajarse (self):
    print("relajarse")
  def comer (self):
    print("comer")
  def pescar (self):
    print("pescar")
  def surfear (self):
    print("surfear")
pla=vacaciones()
print(pla.playa)
print(pla.viajar)
print(pla.equipaje)
print(pla.jugar)
print(pla.tomar)
print(pla.arena)
print(pla.playa2)
print(pla.isla)
print(pla.lanchas)
print(pla.canoas)
pla.descansar()
pla.relajarse()
pla.comer()
pla.pescar()
pla.surfear()