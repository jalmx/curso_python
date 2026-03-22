
class Mail:

    def send(self,text:str, mail:str):
        print(f"Enviando el contenido > {text}, al correo: {mail}")


    @staticmethod
    def formato(mail):
        return f"{mail}@mail.com"


