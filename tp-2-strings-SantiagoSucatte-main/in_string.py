def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre = input("Nombre: ").lower()
    print(f"Contiene a: {"a" in nombre}\nContiene e: {"e" in nombre}\nContiene i: {"i" in nombre}\nContiene o: {"o" in nombre}\nContiene u: {"u" in nombre}")

