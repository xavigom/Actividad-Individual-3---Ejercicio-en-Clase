#Actividad Individual 3 - Ejercicio en Clase - Programación
#Nombre: Edgar Gomez - Fecha:10 de diciembre de 2024
#Conversion de un numero decimal a binario

numero = int (input("Por favor ingrese un numero: "))
valorDividir = numero
resultado = ""

while True:
    print (f"valorDividir {valorDividir}")
    if (valorDividir > 1):
        residuo = str(valorDividir % 2)
    else:
        residuo = str(valorDividir)

    resultado = residuo + resultado # 1 + 0 = 10
    print(f"residuo {residuo}")
    print(f"resultado {resultado}")
    if(valorDividir <= 1):
        break

    valorDividir //=2
    print()