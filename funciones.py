# Función para registrar un pedido
def registrar_prestamo(prestamos):
    #Pedir ingreso de datos 
    Prestamo = int(input("Ingrese el numero del prestamo: "))
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    id = int(input("Ingrese el ID del libro: "))
    fechaPrestamo= input("Ingrese la fecha actual: ")
    fechaDevolcion= input("Ingrese la fecha a devolver: ")
    #Verificar si los datos ingresados son correctos
    if not nombre or not id or not fechaPrestamo or not fechaDevolcion:
        print("Error: Todos los campos son obligatorios")
        return 
    #salir si algun campo no esta correcto
    
    #Creamos un diccionario
    prestamo = {
        'prestamo': Prestamo,
        'nombre': nombre,
        'apellido': apellido,
        'ID libro': id,
        'Fecha Prestamo': fechaPrestamo,
        'Fecha Devolucion': fechaDevolcion

    }
    #Agregamos los datos a la lista de prestamos
    prestamos.append(prestamo)
    print("Prestamo registrado exitosamente.")
# Función para listar todos los pedidos
def listar_prestamos(prestamos):
    #Verificamos si hay prestamos
    if not prestamos:
        print("No hay prestamos registrados.")
        return

    for prestamo in prestamos:
        print(f"Prestamo : {prestamo['prestamo']}")
        print(f"Cliente: {prestamo['nombre']} {prestamo['apellido']}")
        print(f"ID Libro: {prestamo['ID libro']}")
        print(f"Fecha Prestamo: {prestamo['Fecha Prestamo']}")
        print(f"Fecha devolucion: {prestamo['Fecha Devolucion']}")
        

def recibo_prestamo(prestamos):
    #Verificamos si hay prestamos 
    if not prestamos:
        print("No hay prestamos registrados.")
        return
    
    #listamos los prestamos 
    print("Listado de Préstamos:")
    for i, prestamo in enumerate(prestamos):
        print(f"{i + 1}. \n Nombre: {prestamo['nombre']} {prestamo['apellido']} \n ID Libro: {prestamo['ID libro']} \n Fecha Prestamo: {prestamo['Fecha Prestamo']} \n Fecha devolucion: {prestamo['Fecha Devolucion']}")
    #Seleccionamos el prestamo a realizar el recibo
    try:
        numeroPrestamo = int(input("Seleccione el número del préstamo para generar el recibo: ")) - 1
        if numeroPrestamo < 0 or numeroPrestamo >= len(prestamos):
            print("Selección inválida.")
            return
        #Estructuramos el recibo 
        prestamo_seleccionado = prestamos[numeroPrestamo]
        recibo = (
             
            f"Nombre: {prestamo_seleccionado['nombre']} {prestamo['apellido']}\n"
            f"ID libro: {prestamo_seleccionado['ID libro']}\n"
            f"Fecha de Préstamo: {prestamo_seleccionado['Fecha Prestamo']}\n"
            f"Fecha de Devolución: {prestamo_seleccionado['Fecha Devolucion']}\n"
        )
        #Lo guardamos todo en un txt
        with open(f"recibo_{prestamo_seleccionado['ID libro']}.txt", "w") as file:
            file.write(recibo)

        print(f"Recibo generado con éxito: recibo_{prestamo_seleccionado['ID libro']}.txt")
    #Mensaje de error en caso de dato mal ingresado 
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
#Funcion salir del programa 
def salir():
    print("Saliendo del programa. ¡Hasta luego!")    