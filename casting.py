def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input("Precio: "))
    descuento = float(input("Descuento: "))
    cantidad = int(input("Cantidad: "))
    print(f"Precio: {precio}\nDescuento: {descuento}\nPrecio con descuento: {precio - descuento}")
    total = (precio - descuento) * cantidad
    print(f"Total: {total}")
