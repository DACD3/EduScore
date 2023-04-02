#registro = {}

#while True:
#    usuario = input("Ingrese su correo institucional: ")
    
    # Validación de correo electrónico
#    if not usuario.endswith("@alumnos.udg.mx"):
#        print("Solo se permiten correos electrónicos que terminen en '@alumnos.udg.mx'.")
#        continue
        
#    contraseña = input("Ingrese una contraseña: ")
#    registro[usuario] = contraseña
#    print("Usuario registrado correctamente.")
    
#    continuar = input("¿Desea seguir registrando usuarios? (S/N)").lower()
#    if continuar == "n":
#        break

#print("Registro de usuarios completado:", registro)

import re

registro = {}

while True:
    usuario = input("Ingrese su correo institucional: ")
    
    # Validación de correo electrónico
    if not usuario.endswith("@alumnos.udg.mx"):
        print("Solo se permiten correos electrónicos que terminen en '@alumnos.udg.mx'.")
        continue
        
    # Validación de contraseña
    while True:
        contraseña = input("Ingrese una contraseña: ")
        
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
            continue
        
        if not re.search("[a-z]", contraseña):
            print("La contraseña debe incluir al menos una letra minúscula.")
            continue
        
        if not re.search("[A-Z]", contraseña):
            print("La contraseña debe incluir al menos una letra mayúscula.")
            continue
        
        if not re.search("[0-9]", contraseña):
            print("La contraseña debe incluir al menos un número.")
            continue
        
        break
    
    registro[usuario] = contraseña
    print("Usuario registrado correctamente.")
    
    continuar = input("¿Desea seguir registrando usuarios? (S/N)").lower()
    if continuar == "n":
        break

print("Registro de usuarios completado:", registro)