
def main():
    edad = int(input("Ingresa tu edad: "))
    identificacion = ""
    
    if (edad >= 18):
        identificacion = str(input("¿Tienes identificación oficial? (s/n): "))
        if identificacion == "s" or identificacion == "S":
            print("Trámite de licencia concedido")
        elif identificacion == 'n' or identificacion == "N":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    elif (0 < edad < 18):
            print("No cumples requisitos")
    else: 
            print("Respuesta incorrecta")


if __name__ == '__main__':
    main()
