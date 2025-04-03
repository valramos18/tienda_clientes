def hacer_menu():
    print ("1. Registrar nuevo cliente.")
    print ("2. Eliminar cliente.")
    print ("0. Salir del sistema.")
    print ("... Seleccione una opcion ...")
    opcion = int(input())
    return opcion

def registrar_cliente():
    nombre_cliente = input("digite el nombre:")
    apellido_cliente = input("digite el apellido:")
    cedula_cliente = input("digite la cedula:")
    inf_cliente = [nombre_cliente, apellido_cliente, cedula_cliente]
    return inf_cliente

def guardar_clientes(inf_cliente, bd_cliente):
    bd_cliente.append(inf_cliente)
    return bd_cliente

def incluir_nueva_lista():
    aux_lista = []
    cantidad_nuevas = int(input("Digite la cantidad nueva de clientes: "))
    for i in range(0, cantidad_nuevas, 1):
        aux = registrar_cliente()
        aux_lista.append(aux)
    print(aux_lista)
    #return aux_lista



#*** Zona principal de codigo ***
incluir_nueva_lista()
base_datos_clientes = [5]
while True:
    aux_opcion = hacer_menu()
    match aux_opcion:
        case 1:
            aux_info_cliente = registrar_cliente()
        case 2:
            aux_lista = incluir_nueva_lista()
            base_datos_clientes.extend(aux_lista)






base_datos_clientes =  []

aux_info_cliente = registrar_cliente()
aux_basedatos = guardar_clientes(aux_info_cliente, base_datos_clientes)
base_datos_clientes = aux_basedatos
print (base_datos_clientes)

aux_info_cliente = registrar_cliente()
aux_basedatos = guardar_clientes(aux_info_cliente, base_datos_clientes)
base_datos_clientes = aux_basedatos
print (base_datos_clientes)

aux_info_cliente = registrar_cliente()
aux_basedatos = guardar_clientes(aux_info_cliente, base_datos_clientes)
base_datos_clientes = aux_basedatos
print (base_datos_clientes)