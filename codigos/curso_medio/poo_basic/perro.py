class Perro:
    nombre = "Firulays"
    raza = "electrico"

    def ladrar(self):
        print("guau!!!!")

    def correr(self, velocidad):
        print(f"correa a {velocidad} km/h")

    def jugar(self, pelota, hueso, chancla):
        return f"""
    {self.nombre} juega con una {pelota}, tambien con su hueeso { hueso} y le lanzaron una {chancla}
    """.strip()

if __name__ == "__main__":
    perrito_unicornio = Perro()
    perrito_unicornio.ladrar()
    perrito_unicornio.correr(180)
    mensaje = perrito_unicornio.jugar("pelota azul", "de alce siveriano", "chancla de mi mamá")
    print(mensaje)
