#importacion librerias
import random

#datos ingresados por usuario
jugada = input("Escribe tu jugada (piedra, papel o tijeras): ").lower()

#array de opciones
opciones = ['piedra','papel','tijeras']

#ciclo para corregir el input de usuario
while jugada not in opciones:
    jugada = input("Debes escribir una opción correcta (piedra, papel o tijeras): ")

#definir jugada de computadora
jugada_comp = random.choice(opciones)

#condiciones
if (jugada == jugada_comp):
    print(f'Usaste {jugada}, la computadora uso {jugada_comp}')
    print("Resultado: Empate")
elif (jugada == 'piedra' and jugada_comp=='tijeras') or (jugada == 'papel' and jugada_comp=='piedra') or (jugada=='tijeras' and jugada_comp=='papel'): 
    print(f'Usaste {jugada}, la computadora uso{jugada_comp}')
    print("Resultado: Ganaste")
else:
    print(f'Usaste {jugada}, la computadora uso: {jugada_comp}')
    print("Resultado: Perdiste")



