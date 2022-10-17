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

def oportunidades():
  numIntentos = 0
  while True:
    oportunidades = numIntentos + 1
  if oportunidades <= 5:
    print("Sigue intentandolo")
  else:
    print("Game over")
  return oportunidades

def puntuaciones():
  tabla = {}
  tabla["nombreJugador"] = input("Introduce un nombre: ")
  tabla["puntuacion"] = puntuacion
  puntos = 0
  if oportunidades == 1:
    puntuacion = puntos + 100
  elif oportunidades == 2:
    puntuacion = puntos + 50
  elif oportunidades == 3:
    puntuacion = puntos + 25
  elif oportunidades == 4:
    puntuacion = puntos + 10
  elif oportunidades == 5:
    puntuacion = puntos + 5
  else:
    puntuacion = 0
    
  print (tabla["nombreJugador", "puntos"])
  return tabla

def juego(numero, minimo, maximo):
  intento = decidirNivel("Adivine el numero", minimo, maximo)

  if intento < numero:
    print("El numero que buscas es mas grande")
    minimo = intento + 1
    victoria = False
  elif intento > numero:
    print("El numero que buscas es mas pequeño")
    maximo = intento - 1
    victoria = False
  elif intento == oportunidades:
    victoria = False
  else:
    print("Enhorabuena, has ganado")
    intento = minimo = maximo
    victoria = True
    return minimo, maximo, victoria

def eligirNivel(minimo,maximo):
  return decidirNivel("Elige un nivel", minimo,maximo)

def jugarPartida(numero, minimo, maximo):
  minimo,maximo,victoria = juego(numero, minimo, maximo)
  if(victoria):
    return

def jugar():
  minimo, maximo = decidirNivel()
  while True:
    numero = eligirNivel(minimo, maximo)
    jugarPartida(numero, minimo, maximo)
    if not respuestaStartSiONo("Nueva Partida: "):
      print("Hasta la próxima")
      return
