class Led:
    
    def __init__(self, color, corriente=0.018):
        # print("Se crea el objeto LED")
        self.__color = color
        self.__corriente = corriente
    
    def get_color(self):
        return self.__color
    
    def get_corriente(self):
        return self.__corriente


led1 = Led("blanco", 0.025) #estoy creando una instancia 
led2 = Led("rojo") #estoy creando una instancia 
led3 = Led("verde", 0.02) #estoy creando una instancia 
led4 = Led("amarillo", 0.019) #estoy creando una instancia 

for l in [led1, led2, led3, led4]:
    print(f"El es color {l.get_color()}")
    print(f"consume una corriente de {l.get_corriente()}A")
    print("-"*30)