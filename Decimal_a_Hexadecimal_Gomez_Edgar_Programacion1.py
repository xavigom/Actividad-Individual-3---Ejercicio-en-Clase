#Actividad Individual 3 - Ejercicio en Clase - Programación
#Nombre: Edgar Gomez - Fecha:10 de diciembre de 2024
#Conversion de numero decimal a hexadecimal

numero = int (input("Por favor ingrese un numero: "))

def decimalhexadecimal(numero):
    if numero == 0:
        return "0"
    opciones = "0123456789ABCDEF"
    hexadecimal = ""
    while numero > 0:
        tecla = numero % 16
        hexadecimal = opciones[tecla] + hexadecimal
        numero = numero // 16
    else:
        return hexadecimal
resultado = decimalhexadecimal(numero)

print(f"La conversion hexadecimal de [ {numero} ] es [ {resultado} ].")