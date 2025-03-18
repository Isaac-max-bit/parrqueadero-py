
def cuenta():
    intentos = 0
    while intentos < 3:
        U = input("Ingrese su Usuario: ")
        P = input("Ingrese su Contraseña: ")

        if U == "Isaac" and P == "123":
            print("Acceso Correcto")
            break
        else:
            intentos += 1
            if intentos < 3:
                print(f"Error. Te quedan {3 - intentos} intentos.")
            else:
                print("Eres una rata, Cuenta bloqueada")
                
cuenta()
