def hacer_menu():
    print("1. Registar Nuevo Cliente.")
    print("2. Eliminar Cliente.")
    print("0. Salir del Sistema.")
    print("...seleccione una opcion...")
    opcion = int(input())
    return opcion

def registrar_cliente():
    nombre_cliente = input("digite el nombre: ")
    apellido_cliente = input("digite el apellido: ")
    cedula_cliente = input("digite la cedula: ")
    info_cliente = [nombre_cliente, apellido_cliente, cedula_cliente]
    return info_cliente

def guardar_cliente():
    base_datos_clientes
#*zona principal de codigo*
base_datos_clientes = []
aux_opcion = hacer_menu()
aux_info= registrar_cliente()
print(aux_info)