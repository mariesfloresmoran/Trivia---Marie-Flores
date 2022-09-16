puntaje = 0
opciones = ["a", "b", "c", "d", "A", "B", "C", "D"]

print("Bienvenido a mi trivia sobre Apple.\n")

print("A continuación pondremos a prueba tus conocimientos\n")

nombre = input("Ingresa tu nombre: ")
print("\nHola",nombre,"responde las siguientes preguntas escribiendo la letra de la alternativa correcta y presionando 'Enter' para enviar la respuesta: \n")

print("1° ¿Cuál es la última versión de IPhone en el mercado")
print("a) IPhone 12")
print("b) IPhone 13")
print("c) IPhone 14")
print("d) IPhone 13 Plus")
respuesta_1 = input("\nIngresa tu respuesta: ")
while respuesta_1 not in opciones:
  print ("Debes responder a,b,c o d.")
  respuesta_1 = input("\nIngresa tu respuesta: ")
if respuesta_1.lower() == "c":
  print("¡Correcto", nombre,"! +4")
  puntaje = puntaje + 4
else:
  print("Incorrecto ", nombre,":(")

print("")
  
print("2° ¿Cuál es el número máximo de núcleos de CPU en una MACBOOK?")
print("a) 8 núcleos")
print("b) 10 núcleos")
print("c) 12 núcleos")
print("d) Ninguna de las anteriores")

respuesta_2 = input("\nIngresa tu respuesta: ")
while respuesta_2 not in opciones:
  print ("Debes responder a,b,c o d.")
  respuesta_2 = input("\nIngresa tu respuesta: ")
if respuesta_2.lower() == "b":
  print("¡Correcto", nombre,"! +4")
  puntaje = puntaje + 4
else:
  print("Incorrecto ", nombre,":(")

print("")
  
print("3° ¿Cuántos tipos de Apple Watch se venden en el 2022")
print("a) 3 tipos")
print("b) 2 tipos")
print("c) 1 tipos")
print("d) 4 tipos")

respuesta_3 = input("\nIngresa tu respuesta: ")
while respuesta_3 not in opciones:
  print ("Debes responder a,b,c o d.")
  respuesta_3 = input("\nIngresa tu respuesta: ")
if respuesta_3.lower() == "a":
  print("¡Correcto", nombre,"! +4")
  puntaje = puntaje + 4
else:
  print("Incorrecto ", nombre,":(")

print("")
  
print("4° ¿Quién (es) se consideran como fundador (es) de Apple?")
print("a) Steve Wozniak")
print("b) Steve Jobs")
print("c) Ronald Wayne")
print("d) Todos los anteriores")

respuesta_4 = input("\nIngresa tu respuesta: ")
while respuesta_4 not in opciones:
  print ("Debes responder a,b,c o d.")
  respuesta_4 = input("\nIngresa tu respuesta: ")
if respuesta_4.lower() == "d":
  print("¡Correcto", nombre,"! +4")
  puntaje = puntaje + 4
else:
  print("Incorrecto ", nombre,":(")
  
print("")
  
print("5° ¿Quién es el actual CEO de Apple")
print("a) Susan L. Wagner")
print("b) Tobert A. Iger")
print("c) Tim Cook")
print("d) Andrea Jung")

respuesta_5 = input("\nIngresa tu respuesta: ")
while respuesta_5 not in opciones:
  print ("Debes responder a,b,c o d.")
  respuesta_5 = input("\nIngresa tu respuesta: ")
if respuesta_5.lower() == "c":
  print("¡Correcto", nombre,"! +4")
  puntaje = puntaje + 4
else:
  print("Incorrecto ", nombre,":(")

print("\nHaz terminado, el puntaje obtenido es: " ,puntaje)