def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre = input("Ingrese nombre completo: ")
    email = input("Ingrese email: ")
    nota1 = int(input("Ingrese nota 1: "))
    nota2 = int(input("Ingrese nota 2: "))
    nota3 = int(input("Ingrese nota 3: "))
    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)
    nombre_limpio = nombre.strip().title()
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    print(f"Iniciales: {nombre_limpio[0] + nombre_limpio[nombre_limpio.find(" ") + 1]}")
    nombre_solo = nombre_limpio[:nombre_limpio.find(" ")]
    apellido = nombre_limpio[nombre_limpio.find(" ") + 1:]
    print(f"Usuario: {apellido.lower()}.{nombre_solo.lower()}")
    print(f"Email valido: {"@" in email}")
    print(f"Dominio: {email.lower()[email.find("@") + 1:]}")
    print(f"Nombre para archivo: {nombre_limpio.replace(" ", "_")}")
    print(f"Cantidad de a: {nombre_limpio.lower().count("a")}")
    print(f"Codigo secreto: {nombre_limpio[::-1].upper()}")
    n1 = int(nota1)
    n2 = int(nota2)
    n3 = int(nota3)
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    print(f"Suma: {n1 + n2 + n3}")
    print(f"Promedio: {(n1 + n2 + n3) / 3}")
    print(f"Promedio entero: {(n1 + n2 + n3) // 3}")
    print("=" * 24)




