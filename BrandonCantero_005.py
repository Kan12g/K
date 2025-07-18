lst_productos = {'C-123': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                        'C-111': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                        'C-234': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                        'C-456': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                        'C-1222': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                        'C-477': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                        'C-334': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                        'C-2906': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

lst_stock = {'C-123': [387990,10], 
                        'C-111': [327990,4], 
                        'C-234': [424990,1],
                        'C-456': [664990,21], 
                        'C-477': [290890,32], 
                        'C-334': [444990,7],
                        'C-1222': [749990,2], 
                        'C-2906': [349990,1]}


def stock_marca(lst_productos:dict, lst_stock: dict, marca_buscada: str) -> int:
        for codigo, dato in lst_productos.items():
                if codigo in lst_productos and codigo in lst_stock:
                        print(f"El total de stocks para el codigo: {dato[0]} es: {lst_stock[codigo][1]}")


def busqueda_precio(lst_productos:dict, lst_stock: dict, p_min: int, p_pax: int) -> None:
        for dato in lst_stock.values():
                precio = dato[0]
        if p_min >= precio and p_pax <= precio:
                print(f"Los productos que estan dentro del precio son: {lst_productos}")


def actualizar_precio(lst_stock: dict, codigo: str, nuevo_precio: int) -> bool:
        if codigo in lst_stock.keys():
                lst_stock[codigo][0] = nuevo_precio
                return True
        else:
                return False
        

def menu():
        while True:
                print("*"*50)
                print("Menu")
                print("1. Consultar stock total de una marca")
                print("2. Buscar productos")
                print("3. Actualizar precio de un producto")
                print("4. Salir")
                try:
                        opcion = int(input("Ingrese una de las opciones: "))
                except ValueError:
                        print("Error, solo se pueden escoger una de las opciones")
                print("*"*50)
                if opcion == 1:
                        marca_buscada = input("Ingrese la marca que necesita buscar: ")
                        stock_marca(lst_productos,lst_stock,marca_buscada)
                        
                elif opcion == 2:
                        try:
                                p_min = int(input("Ingrese el precio minimo: "))
                        except ValueError:
                                print("El valor que ingreso es incorrecto...")
                        
                        try:
                                p_max = int(input("Ingrese el precio maximo: "))
                        except ValueError:
                                print("El valor que ingresa es incorrecto")
                        busqueda_precio(lst_productos,lst_stock,p_min,p_max)
                        
                elif opcion == 3:
                        codigo = input("Ingrese el codigo: ")
                        try:
                                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                        except ValueError:
                                print("Solo se permite ingresar el nuevo precio....")
                        if actualizar_precio(lst_stock,codigo,nuevo_precio):
                                print("Se actualizo el precio")
                        else:
                                print("No se pudo actualizar el precio...")
                elif opcion == 4:
                        print("Saliendo del programa....")
                        break
menu()