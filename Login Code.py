users = {"mm": "12345", "ll": "98765"}

def login():
    while True:
        username = input("Correo institucional: ")
        if username not in users:
            print("Correo equivocado.")
        else:
            password = input("Contraseña: ")
            if users[username] != password:
                print("Contraseña incorrecta.")
            else:
                print("Inicio de sesion exitoso")
                break

login()