def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base = int(input("Base: "))
    altura = int(input("Altura: "))
    area = base * altura
    perimetro = base * 2 + altura * 2
    print(f"Base: {base}\nAltura: {altura}\nArea: {area}\nPerimetro: {perimetro}")

