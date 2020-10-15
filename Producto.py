from os import system


class Producto:

    lista_productos = []

    def __init__(self, cod_barra, precio, cantidad):
        self.cod_barra = cod_barra
        self.precio = precio
        self.cantidad = cantidad

    @classmethod
    def ingresa_datos(cls):
        nombre = input("Nombre del producto: ")
        cod_barra = int(input("Código de barra: "))
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        if cls.no_existe_producto:
            cls.crea_producto(nombre, cod_barra, precio, cantidad)
        system('clear')
    pass

    @classmethod
    def crea_producto(cls, nombre_producto, cod_barra, precio, cantidad):
        nombre_producto = Producto(cod_barra, precio, cantidad)
        cls.lista_productos.append(nombre_producto.__dict__)
        return nombre_producto

    @classmethod
    def listar_productos(cls):
        system('clear')
        return cls.lista_productos

    @classmethod
    def consultar_stock_producto(cls, cod_barra):
        i = cls.indice_cod_barra(cod_barra)
        return cls.lista_productos[i]['cantidad']

    @classmethod
    def consultar_precio(cls, cod_barra):
        i = cls.indice_cod_barra(cod_barra)
        return cls.lista_productos[i]['precio']

    @classmethod
    def indice_cod_barra(cls, cod_barra):
        for i in range(len(cls.lista_productos)):
            if cls.lista_productos[i]['cod_barra'] == cod_barra:
                return i

    @classmethod
    def actualizar_precio(cls, cod_barra, precio_nuevo):
        i = cls.indice_cod_barra(cod_barra)
        cls.lista_productos[i]['precio'] = precio_nuevo
    pass

    @classmethod
    def no_existe_producto(cls, cod_barra):
        if cls.indice_cod_barra(cod_barra) is None:
            return True

    @classmethod
    def imprimir_productos(cls):
        print(*cls.lista_productos, sep="\n")
