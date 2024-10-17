import pandas as pd
print(pd.__version__)
"""""
numeros = [random.randint(1,100) for i in range(10)]
print("Numeros generados: ",numeros)

#Contar el numero de palabras de un texto
texto = "Hoy es miercoles, y mañana es jueves"
contador={}

for palabra in texto.split():
    palabra = palabra.strip(",")
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
        
print(contador)
"""""
"""""
numero =int(input())

Dividir = numero % 2
if Dividir == 0 or Dividir == 1:

  print("El numero:",numero, "Es par")
  
else:
 print("El numero no es par")
 
 """""
 
 #Crear un data frame (Arreglo de datos)
 
datos = {
     
     'Nombre':['Andres','Juan','Carlos','Maria'],
     'Edad': [12,14,21,56],
     'Nota': [3.5,1.2,3,4.9]
 }
df = pd.DataFrame(datos)
print(df)

media = df['Edad'].mean()
print(media)

media_note = df['Nota'].mean()
print(media_note)

#Calificación > 4.0

cal_4 =df[df['Nota']> 4.0]
print(cal_4)
