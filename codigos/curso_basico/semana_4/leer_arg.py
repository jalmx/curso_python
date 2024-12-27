import sys
import circulo


if __name__ == "__main__":
    print(sys.argv)
    args = sys.argv

    if len(args) > 1:
        radio = int(args[1])
        area = circulo.area_circulo(radio)
        print(f"El area del circulo es {area}")
    else:
        print("no diste el valor del radio")


