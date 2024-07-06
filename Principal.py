# Importar funciones desde el archivo de funciones
from funciones import registrar_prestamo, listar_prestamos,recibo_prestamo,salir


# Lista para almacenar los pedidos
prestamos = []

# Programa principal
while True:
    print("\nSistema de Gestión de Pedidos - BibliotecaPublica")
    print("1. Registrar prestamo")
    print("2. Listar todos los prestamos")
    print("3. Imprimir recibo de prestamo")
    print("4. Salir del programa")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_prestamo(prestamos)
    elif opcion == '2':
        listar_prestamos(prestamos)
    elif opcion == '3':
        recibo_prestamo(prestamos)
    elif opcion == '4':
        salir()
        break
    else:
        print("Opción no válida. Intente de nuevo.")