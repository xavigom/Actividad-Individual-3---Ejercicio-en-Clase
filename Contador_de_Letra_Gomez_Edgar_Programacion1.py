#Actividad Individual 3 - Ejercicio en Clase - Programación
#Nombre: Edgar Gomez - Fecha:10 de diciembre de 2024
#Contador de letra en una oración, utilizando lorem ipsum. 
#Solicitar al usuario una letra e indicar cuantas veces se repite en el texto


letra = input("Por favor, ingrese una letra al azar: ").lower()

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ut placerat augue. Praesent commodo massa vel leo vestibulum, a finibus est feugiat. Phasellus neque erat, ornare iaculis faucibus sit amet, elementum nec ante. Duis vel felis vehicula, ullamcorper libero in, efficitur felis. Cras efficitur mi nec sem placerat, vel tincidunt odio rhoncus. Nunc orci mi, placerat ac feugiat vel, faucibus eget velit. Nulla fringilla sapien in sem viverra auctor. Nullam et volutpat justo. Nulla vitae ornare lectus. Nam porta pellentesque nulla, eget feugiat orci interdum eu. Vivamus non vulputate metus. Curabitur ut dignissim risus. Pellentesque feugiat id urna eu pellentesque. Curabitur sit amet vulputate lacus, sit amet feugiat ex. Etiam gravida consectetur nisi, in cursus ante vestibulum at. Praesent eu dignissim lorem. Nulla sodales arcu non pharetra faucibus. Praesent convallis convallis urna, at rutrum justo. Integer congue sit amet mi in tempus. Quisque accumsan arcu risus. Suspendisse volutpat in magna vel sodales."

i = 0
indice = 0
while indice < len(texto):
    if texto[indice].lower() == letra:
        i += 1
    indice += 1
else:
    print(f"La letra ' {letra} ' se repite [ {i} ] veces en el texto.")