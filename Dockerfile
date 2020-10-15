FROM python:3.10.0a1-alpine3.12

ADD Carrito.py /

ADD Producto.py /

ADD Menu.py /

ADD main.py /

CMD [ "python", "main.py" ]
