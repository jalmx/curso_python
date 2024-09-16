edad = int(input("indica tu edad: "))

# if edad >= 18:
#     print("Ya te toca CERESO")

# if edad < 18:
#     print("taz tiernito")


# if edad >= 18:
#     print("Ya te toca CERESO")
# else:
#     print("taz tiernito")

# Shorthand del IF-ELSE
# variable = RESULTADO_TRUE if COMPARACIÓN else RESULTADO_FALSE
resultado = "Ya te toca CERESO" if edad >= 18 else "taz tiernito"
print(resultado)
