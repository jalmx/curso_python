import lib
from mail import Mail

if __name__ == "__main__":
    #lib.mensaje() #metodo estatico

    mail = Mail() #cree la instancia 

    correo= Mail.formato("patito")

    print(correo)
    mail.send("hola", correo)