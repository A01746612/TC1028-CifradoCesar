#Daniela Jace Olguín Montiel
#A01746612
"""
inicio de codificación
codificacion (mensaje, llave):
creo el string de respuesta:
for(cada una de las letras)¨{
    convierto la letra a ascii y la salvo en la variable let_asc;
    le sumo a la variable letra_asc la llave;
    convierto letra_asc a caracter;
    concatenar el caracter a un string de respuesta;
}
regresar el string de respuesta;
fin codificacion;
"""

def codificacion(mensaje,llave):
    respuesta=""
    for i in mensaje:
        asc= ord(i)
        asc= asc + llave
        letra = chr(asc)
        respuesta = respuesta + letra 
    return respuesta
"""
inicio de decodificacion
decodificacion(mensaje_encriptado,llave_desencriptado):
creo el string de desencriptado:
    for(cada una de las letras){
    convierto a ascii y salvo asc;
    le resto a la variable letra_asc la llave_desencriptar;
convierto letra_asc a caracter;    
}
regresar respuesta_desencriptada
"""
def decodificacion(mensaje_encriptado, llave_desencriptar):
    respuesta_desencriptada=""
    for i in mensaje_encriptado:
        asc=ord(i)
        asc=asc-llave_desencriptar
        letra=chr(asc)
        respuesta_desencriptada=respuesta_desencriptada+letra
    return respuesta_desencriptada
"""
inicio de main 
pedir el mensaje str (la letra del abecedario) y nombrarlo
pedir el numero entero y nombrar la variable 
pedir caracter y nombrar la variable 
pedir numero y nombrar variable 
nombrar variable respuesta a la funcion codificacion(mensaje,llave)
nombrar variable respuesta_desencriptada a la funcion 
decodificacion(mensaje_encriptado, llave_desencriptar)
imprimir respuesta
imprimir las respuestas del mensaje desencriptado 
"""

def main():
    mensaje=str(input())
    llave=int(input())
    mensaje_encriptado=str(input())
    llave_desencriptar=int(input())
    
    respuesta=codificacion(mensaje, llave)
    respuesta_desencriptada=decodificacion(mensaje_encriptado, llave_desencriptar)
    print(respuesta)
    print(respuesta_desencriptada)
    
main()
        