import random

def nivel_uno():
  num = random.randint(0,100)
  return num
def nivel_dos():
  num = random.randint(0, 1000)
  return num
def nivel_tres():
  num = random.randint(0, 1000000)
  return num
def nivel_cuatro():
  num = random.randint(0, 1000000000000)
  return num

def respuestaStartSiONo():
  respuestaStart = ("Si", "si", "Yes", "yes")
  try:
    return input().lower() in respuestaStart
  except:
    return False

def decidirNivel():
  while True:
    print("1 - Nivel uno(de 0 a 100)" )
    print("2 - Nivel dos(de 0 a 1000")
    print("3 - Nivel tres(de 0 al 1000000")
    print("4 - Nivel cuatro(de 0 a 1000000000000")

    respuestaNivel = input("Elige un nivel: ")
    if respuestaNivel == "1":
      nivel_uno()
    elif respuestaNivel == "2":
      nivel_dos()
    elif respuestaNivel == "3":
      nivel_tres()
    elif respuestaNivel =="4":
      nivel_cuatro()
    else:
      print("Elija un nivel")
      return decidirNivel()
