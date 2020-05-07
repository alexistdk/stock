class Producto:

    listaProductos = []
    listaCodBarra = []

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @staticmethod
    def ingresaDatos():
        codBarra = int(input("Código de barra: ")) #ingresa el codigo de barras
        nombre = input("Nombre: ") #ingresa el nombre
        precio = int(input("Precio: ")) #ingresa el precio
        cantidad = int(input("Cantidad: ")) #ingresa la cantidad
        codBarra = Producto(nombre, precio, cantidad) #el codigo de barra se usa para instarciar el producto
        Producto.listaProductos.append(codBarra.__dict__) #los atributos y sus valores son guardados en una lista
    
    @staticmethod
    def imprimirProductos():
        print(*Producto.listaProductos, sep="\n")

    @classmethod
    def consultarStock(cls, nombreProducto):
        pass

    @staticmethod
    def consultarPrecio(codBarra): #consulta el precio de un producto
        return codBarra.precio