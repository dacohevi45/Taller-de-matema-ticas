# --------------------------------------------------------
# Taller realizado por David Correa Herrera
# Ingeniería de software
# Tecnológico de antioquia
# --------------------------------------------------------

# ------------------------------------------------------------------
# CONSTANTES FIJAS
# ------------------------------------------------------------------
NOMBRES_VARIABLES = ["A", "B", "C", "D"]
# fuera de {0, 1}: significa "aún no ingresada"
VALOR_SIN_ASIGNAR = -1
DIGITOS_MAYUSCULAS = "0123456789ABCDEF"
DIGITOS_MINUSCULAS = "0123456789abcdef"
# constante: el conjunto vacío (nunca se modifica)
CONJUNTO_VACIO = []               


# ------------------------------------------------------------------
# DEFINICIONES DE LIMPIAR PANTALLA Y SI SE ESCRIBEN DATOS INCORRECTOS
# ------------------------------------------------------------------

# Limpia la pantalla haciendo saltos de linea 
def limpiar_pantalla():
    print("\n" * 40)

# Cadena de espacios dependiento de la cantidad que se especifique
def espacios(cantidad):          
    return " " * cantidad

# Genera cantidad de guiones segun se especifique    
def guiones(cantidad):
    return "-" * cantidad


# Verificación de que los valores esten bien ingresados
def variables_ingresadas(variables):
    # Devuelve True solo si las cuatro variables valen 0 o 1
    for valor in variables:
        if valor != 0 and valor != 1:
            return False
    return True


# Evalua cada variable y sus valores ingresados
def mostrar_variables(variables):
    texto = " Variables ->"
    for i in range(4):
        if variables[i] == 0 or variables[i] == 1:
            texto = texto + "  " + NOMBRES_VARIABLES[i] + " = " + str(variables[i]) + " "
        else:
            texto = texto + "  " + NOMBRES_VARIABLES[i] + " = ? "
    print("=" * 56)
    print(texto)
    print("=" * 56)

# Evalua que los valores si sean 0 o 1
def pedir_bit(nombre):
    # Pide un valor hasta que sea exactamente 0 o 1
    while True:
        texto = input("Ingrese el valor de " + nombre + " (0 o 1): ")
        if texto == "0" or texto == "1":
            valor = int(texto)
            break
        print("Valor no válido. Solo se admite 0 o 1.")
    return valor

# guarda la variable
def ingresar_variables(variables):
    for i in range(4):
        variables[i] = pedir_bit(NOMBRES_VARIABLES[i])
    print("Variables guardadas correctamente.")

# Dando valor a A,B,C Y D
def pedir_indice_variable(mensaje):
    # Pide una letra A, B, C o D y devuelve su posición (0, 1, 2 o 3)
    while True:
        texto = input(mensaje)
        if texto == "A" or texto == "a":
            indice = 0
            break
        elif texto == "B" or texto == "b":
            indice = 1
            break
        elif texto == "C" or texto == "c":
            indice = 2
            break
        elif texto == "D" or texto == "d":
            indice = 3
            break
        print("Variable no válida. Escriba A, B, C o D.")
    return indice


# ------------------------------------------------------------------
# COMPUERTAS LÓGICAS (solo aritmética con 0 y 1)
# ------------------------------------------------------------------
def compuerta_if(valor):
    # Reconfigura la señal: si la suma dio más de 1, se deja en 1
    if valor > 1:
        return 1
    return valor


def compuerta_not(a):
    return 1 - a


def compuerta_and(a, b):
    return a * b


def compuerta_or(a, b):
    # La suma lógica con enteros puede dar 2, por eso se usa IF
    return compuerta_if(a + b)


def compuerta_xor(a, b):
    # A xor B = (A y no B) o (no A y B)
    izquierda = compuerta_and(a, compuerta_not(b))
    derecha = compuerta_and(compuerta_not(a), b)
    return compuerta_or(izquierda, derecha)


def compuerta_nand(a, b):
    return compuerta_not(compuerta_and(a, b))


def compuerta_nor(a, b):
    return compuerta_not(compuerta_or(a, b))


def compuerta_xnor(a, b):
    return compuerta_not(compuerta_xor(a, b))


def compuerta_buffer(a):
    # Triángulo sin círculo: deja pasar la señal sin cambiarla
    return a


def compuerta_implica(a, b):
    # A -> B  equivale a  (no A) o B
    return compuerta_or(compuerta_not(a), b)


# ------------------------------------------------------------------
# LECTOR DE COMPUERTAS: dibujo y submenú
# ------------------------------------------------------------------
def dibujar_compuerta_una_entrada(nombre, etiqueta, valor, salida):
    print()
    print(" " + etiqueta + "=" + str(valor) + " ---[ " + nombre + " ]---> " + str(salida))


def dibujar_compuerta_dos_entradas(nombre, etiqueta1, valor1, etiqueta2, valor2, salida):
    print()
    print(" " + etiqueta1 + "=" + str(valor1) + " ---+")
    print("        +--[ " + nombre + " ]--> " + str(salida))
    print(" " + etiqueta2 + "=" + str(valor2) + " ---+")


def ejecutar_compuerta(opcion, variables):
    if opcion == "1":
        indice = pedir_indice_variable("Elija la entrada para NOT (A, B, C o D): ")
        entrada = variables[indice]
        salida = compuerta_not(entrada)
        dibujar_compuerta_una_entrada("NOT", NOMBRES_VARIABLES[indice], entrada, salida)
        print("\nNOT", NOMBRES_VARIABLES[indice], "=", salida)
    elif opcion == "8":
        indice1 = pedir_indice_variable("Elija la primera entrada de la suma (A, B, C o D): ")
        indice2 = pedir_indice_variable("Elija la segunda entrada de la suma (A, B, C o D): ")
        suma = variables[indice1] + variables[indice2]
        salida = compuerta_if(suma)
        etiqueta = NOMBRES_VARIABLES[indice1] + "+" + NOMBRES_VARIABLES[indice2]
        dibujar_compuerta_una_entrada("IF", etiqueta, suma, salida)
        print("\nLa suma entera es", suma, "y la compuerta IF la reconfigura a", salida)
    else:
        indice1 = pedir_indice_variable("Elija la primera entrada (A, B, C o D): ")
        indice2 = pedir_indice_variable("Elija la segunda entrada (A, B, C o D): ")
        a = variables[indice1]
        b = variables[indice2]
        if opcion == "2":
            nombre = "AND"
            salida = compuerta_and(a, b)
        elif opcion == "3":
            nombre = "OR"
            salida = compuerta_or(a, b)
        elif opcion == "4":
            nombre = "XOR"
            salida = compuerta_xor(a, b)
        elif opcion == "5":
            nombre = "NAND"
            salida = compuerta_nand(a, b)
        elif opcion == "6":
            nombre = "NOR"
            salida = compuerta_nor(a, b)
        elif opcion == "7":
            nombre = "XNOR"
            salida = compuerta_xnor(a, b)
        else:
            nombre = "IMPLICA"
            salida = compuerta_implica(a, b)
        dibujar_compuerta_dos_entradas(nombre, NOMBRES_VARIABLES[indice1], a, NOMBRES_VARIABLES[indice2], b, salida)
        print("\n" + NOMBRES_VARIABLES[indice1], nombre, NOMBRES_VARIABLES[indice2], "=", salida)


def es_opcion_compuerta(opcion):
    # True si la opción es un único carácter entre "1" y "9"
    return len(opcion) == 1 and opcion >= "1" and opcion <= "9"


def submenu_compuertas(variables):
    while True:
        mostrar_variables(variables)
        print("LECTOR DE COMPUERTAS")
        print(" 1. Compuerta NOT")
        print(" 2. Compuerta AND")
        print(" 3. Compuerta OR")
        print(" 4. Compuerta XOR")
        print(" 5. Compuerta NAND")
        print(" 6. Compuerta NOR")
        print(" 7. Compuerta XNOR")
        print(" 8. Compuerta IF (reconfigura a 1 si la suma es mayor a 1)")
        print(" 9. Implicación (A -> B)")
        print("10. Limpiar pantalla")
        print("0. Regresar al menú principal")
        opcion = input("Elija una opción: ")
        if opcion == "0":
            break
        elif opcion == "10":
            limpiar_pantalla()
        elif es_opcion_compuerta(opcion):
            ejecutar_compuerta(opcion, variables)
        else:
            print("Opción no válida.")


# ------------------------------------------------------------------
# CIRCUITOS LÓGICOS: cálculo
# Correspondencia con el enunciado: w = A, x = B, y = C, z = D
# ------------------------------------------------------------------
def calcular_circuito_1(a, b, c, d):
    # Figura 1: F = NOR( XOR( BUF( OR( AND(A,B), B ) ), NAND(B,C) ), NOT(D) )
    ab = compuerta_and(a, b)                       # 0
    union = compuerta_or(ab, b)                    # 1
    salida_buffer = compuerta_buffer(union)        # 2
    nand_bc = compuerta_nand(b, c)                 # 3
    xor_1 = compuerta_xor(salida_buffer, nand_bc)  # 4
    no_d = compuerta_not(d)                        # 5
    f = compuerta_nor(xor_1, no_d)                 # 6
    return (ab, union, salida_buffer, nand_bc, xor_1, no_d, f)


def calcular_circuito_2(a, b, c):
    # Figura 2: Z = OR( AND(A,B), AND(A,C) )
    d_cable = compuerta_and(a, b)
    e_cable = compuerta_and(a, c)
    z = compuerta_or(d_cable, e_cable)
    return (d_cable, e_cable, z)


def calcular_circuito_3(a, b, c, d):
    # Ecuación: F = [A -> (B <-> C)] xor (B and D)
    bicondicional = compuerta_xnor(b, c)
    implicacion = compuerta_implica(a, bicondicional)
    b_y_d = compuerta_and(b, d)
    f = compuerta_xor(implicacion, b_y_d)
    return (bicondicional, implicacion, b_y_d, f)


def salida_circuito_1(a, b, c, d):
    resultado = calcular_circuito_1(a, b, c, d)
    return resultado[6]


def salida_circuito_2(a, b, c):
    resultado = calcular_circuito_2(a, b, c)
    return resultado[2]


def salida_circuito_3(a, b, c, d):
    resultado = calcular_circuito_3(a, b, c, d)
    return resultado[3]


# Formas simplificadas con las leyes del álgebra booleana
def circuito_1_simplificado(a, b, c, d):
    # F = B . C' . D
    return compuerta_and(compuerta_and(b, compuerta_not(c)), d)


def circuito_2_simplificado(a, b, c):
    # Z = A . (B + C)
    return compuerta_and(a, compuerta_or(b, c))


def circuito_3_simplificado(a, b, c, d):
    # F = A'B' + A'D' + B'C' + B.C.D' + A.C'.D   (mapa de Karnaugh)
    termino_1 = compuerta_and(compuerta_not(a), compuerta_not(b))
    termino_2 = compuerta_and(compuerta_not(a), compuerta_not(d))
    termino_3 = compuerta_and(compuerta_not(b), compuerta_not(c))
    termino_4 = compuerta_and(compuerta_and(b, c), compuerta_not(d))
    termino_5 = compuerta_and(compuerta_and(a, compuerta_not(c)), d)
    suma = termino_1 + termino_2 + termino_3 + termino_4 + termino_5
    return compuerta_if(suma)


# ------------------------------------------------------------------
# CIRCUITOS LÓGICOS: dibujo (ASCII). Cada (n) es el valor de ese cable.
# ------------------------------------------------------------------
def dibujar_circuito_1(a, b, c, d):
    r = calcular_circuito_1(a, b, c, d)
    sa = str(a)
    sb = str(b)
    sc = str(c)
    sd = str(d)
    print()
    print(" FIGURA 1  (cada (n) es el valor del cable en ese punto)")
    print()
    print(" A=" + sa + " ---+")
    print(espacios(8) + "+-[AND]-(" + str(r[0]) + ")--+")
    print(" B=" + sb + " ---+" + espacios(12) + "+-[OR]-(" + str(r[1]) + ")-[BUF]-(" + str(r[2]) + ")--+")
    print(" B=" + sb + " " + guiones(16) + "+" + espacios(21) + "+-[XOR]-(" + str(r[4]) + ")--+")
    print(" B=" + sb + " ---+" + espacios(34) + "|" + espacios(12) + "+-[NOR]--> F=" + str(r[6]))
    print(espacios(8) + "+-[NAND]-(" + str(r[3]) + ")" + guiones(23) + "+" + espacios(12) + "|")
    print(" C=" + sc + " ---+" + espacios(47) + "|")
    print(" D=" + sd + " -[NOT]-(" + str(r[5]) + ")" + guiones(41) + "+")
    print()
    print(" (B se conecta a tres compuertas: AND, OR y NAND)")


def dibujar_circuito_2(a, b, c):
    r = calcular_circuito_2(a, b, c)
    sa = str(a)
    print()
    print(" FIGURA 2  (D y E son cables internos, no la variable D)")
    print()
    print(" A=" + sa + " ---+")
    print(espacios(8) + "+-[AND]-(D=" + str(r[0]) + ")--+")
    print(" B=" + str(b) + " ---+" + espacios(14) + "|")
    print(espacios(23) + "+-[OR]-(Z=" + str(r[2]) + ")")
    print(" A=" + sa + " ---+" + espacios(14) + "|")
    print(espacios(8) + "+-[AND]-(E=" + str(r[1]) + ")--+")
    print(" C=" + str(c) + " ---+")
    print()
    print(" (A se conecta a las dos compuertas AND)")


def dibujar_circuito_3(a, b, c, d):
    r = calcular_circuito_3(a, b, c, d)
    print()
    print(" ECUACIÓN:  F = [A -> (B <-> C)] xor (B and D)")
    print()
    print(" A=" + str(a) + " " + guiones(19) + "+")
    print(" B=" + str(b) + " ---+" + espacios(15) + "+-[IMP]-(" + str(r[1]) + ")--+")
    print(espacios(8) + "+-[XNOR]-(" + str(r[0]) + ")" + guiones(4) + "+" + espacios(12) + "|")
    print(" C=" + str(c) + " ---+" + espacios(28) + "+-[XOR]-(F=" + str(r[3]) + ")")
    print(" B=" + str(b) + " ---+" + espacios(28) + "|")
    print(espacios(8) + "+-[AND]-(" + str(r[2]) + ")" + guiones(18) + "+")
    print(" D=" + str(d) + " ---+")
    print()
    print(" (IMP = implicación, XNOR = bicondicional)")


# ------------------------------------------------------------------
# CIRCUITOS LÓGICOS: simplificación y tabla de verdad
# ------------------------------------------------------------------
def mostrar_simplificaciones():
    print()
    print(" CIRCUITO 1  F = NOR( XOR( BUF( OR(A.B, B) ), NAND(B,C) ), NOT D )")
    print("  1) Absorción:  (A.B) + B = B   -> la rama de arriba queda solo B")
    print("  2) El BUF no cambia la señal")
    print("  3) De Morgan:  NAND(B,C) = B' + C'")
    print("  4) B xor (B' + C'):  si B=0 da 1, si B=1 da C   ->  B' + C")
    print("  5) De Morgan:  NOR(X, D') = X' . D   con X = B' + C  ->  X' = B . C'")
    print("  RESULTADO:  F = B . C' . D   (no depende de A)")
    print()
    print(" CIRCUITO 2  Z = (A.B) + (A.C)")
    print("  1) Factor común (distributiva):  A.B + A.C = A.(B + C)")
    print("  RESULTADO:  Z = A . (B + C)")
    print()
    print(" ECUACIÓN  F = [A -> (B <-> C)] xor (B.D)")
    print("  1) A -> X  =  A' + X        y       B <-> C  =  B.C + B'.C'")
    print("  2) P xor Q  =  P'.Q + P.Q'  (definición de XOR)")
    print("  3) Se desarrolla y se agrupa con un mapa de Karnaugh (cinco grupos)")
    print("  RESULTADO:  F = A'B' + A'D' + B'C' + B.C.D' + A.C'.D")
    print()
    print(" Compruebe todo con la opción de la tabla de verdad.")


def mostrar_tabla_verdad():
    print()
    print(" w x y z | F1 F1s | Z Zs | F3 F3s | Coincide")
    print(" --------+--------+------+--------+---------")
    todo_correcto = True
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f1 = salida_circuito_1(w, x, y, z)
                    f1s = circuito_1_simplificado(w, x, y, z)
                    zz = salida_circuito_2(w, x, y)
                    zzs = circuito_2_simplificado(w, x, y)
                    f3 = salida_circuito_3(w, x, y, z)
                    f3s = circuito_3_simplificado(w, x, y, z)
                    if f1 == f1s and zz == zzs and f3 == f3s:
                        veredicto = "OK"
                    else:
                        veredicto = "ERROR"
                        todo_correcto = False
                    print(" ", w, x, y, z, "|", f1, " ", f1s, " |", zz, " ", zzs, "|", f3, " ", f3s, " |", veredicto)
    print()
    print(" F1, Z y F3 = circuito original;  F1s, Zs y F3s = forma simplificada")
    if todo_correcto:
        print(" Las simplificaciones coinciden con los circuitos en las 16 filas.")
    else:
        print(" Hay filas que no coinciden: revise las simplificaciones.")


def mostrar_salidas(variables):
    a = variables[0]
    b = variables[1]
    c = variables[2]
    d = variables[3]
    f1 = salida_circuito_1(a, b, c, d)
    z = salida_circuito_2(a, b, c)
    f3 = salida_circuito_3(a, b, c, d)
    print(" Salidas ->  F1 (fig. 1) =", f1, "  Z (fig. 2) =", z, "  F (ecuación) =", f3)
    print(" (w = A, x = B, y = C, z = D)")
    print("=" * 56)


def submenu_circuitos(variables):
    while True:
        mostrar_variables(variables)
        mostrar_salidas(variables)
        print("CIRCUITOS LÓGICOS")
        print(" 1. Dibujar y evaluar el circuito de la figura 1")
        print(" 2. Dibujar y evaluar el circuito de la figura 2")
        print(" 3. Dibujar y evaluar F = [A -> (B <-> C)] xor (B and D)")
        print(" 4. Ver simplificaciones con leyes del álgebra booleana")
        print(" 5. Ver tabla de verdad comparativa (16 filas)")
        print(" 6. Limpiar pantalla")
        print(" 0. Regresar al menú principal")
        opcion = input("Elija una opción: ")
        a = variables[0]
        b = variables[1]
        c = variables[2]
        d = variables[3]
        if opcion == "0":
            break
        elif opcion == "1":
            dibujar_circuito_1(a, b, c, d)
        elif opcion == "2":
            dibujar_circuito_2(a, b, c)
        elif opcion == "3":
            dibujar_circuito_3(a, b, c, d)
        elif opcion == "4":
            mostrar_simplificaciones()
        elif opcion == "5":
            mostrar_tabla_verdad()
        elif opcion == "6":
            limpiar_pantalla()
        else:
            print("Opción no válida.")


# ------------------------------------------------------------------
# PUNTO OPCIONAL A: CONVERSOR DE BASES NUMÉRICAS
# ------------------------------------------------------------------
def valor_digito(caracter):
    # Devuelve el valor (0 a 15) de un dígito, o -1 si no es un dígito válido
    for i in range(16):
        if caracter == DIGITOS_MAYUSCULAS[i] or caracter == DIGITOS_MINUSCULAS[i]:
            return i
    return -1


def es_numero_valido(texto, base):
    if len(texto) == 0:
        return False
    for caracter in texto:
        valor = valor_digito(caracter)
        if valor == -1 or valor >= base:
            return False
    return True


def a_decimal(texto, base):
    # Método de Horner: se recorre de izquierda a derecha
    resultado = 0
    for caracter in texto:
        resultado = resultado * base + valor_digito(caracter)
    return resultado


def de_decimal(numero, base):
    # Divisiones sucesivas: los residuos, leídos al revés, forman el número
    if numero == 0:
        return "0"
    texto = ""
    while True:
        if numero == 0:
            break
        residuo = numero % base
        texto = DIGITOS_MAYUSCULAS[residuo] + texto
        numero = numero // base
    return texto


def pedir_base(mensaje):
    while True:
        texto = input(mensaje)
        if texto == "2" or texto == "8" or texto == "10" or texto == "16":
            base = int(texto)
            break
        print("Base no válida. Use 2, 8, 10 o 16.")
    return base


def pedir_numero_en_base(base):
    while True:
        texto = input("Ingrese el número (entero >= 0) en base " + str(base) + ": ")
        if es_numero_valido(texto, base):
            break
        print("Número no válido para la base", base, "(sin signos, ni espacios, ni decimales).")
    return texto


def rellenar_ceros(texto, largo):
    while True:
        if len(texto) >= largo:
            break
        texto = "0" + texto
    return texto


def quitar_ceros(texto):
    resultado = ""
    empezo = False
    for caracter in texto:
        if caracter == "1":
            empezo = True
        if empezo:
            resultado = resultado + caracter
    if empezo == False:
        return "0"
    return resultado


def comparar_binarios(x, y):
    # 1 si x > y, -1 si x < y, 0 si son iguales
    x = quitar_ceros(x)
    y = quitar_ceros(y)
    if len(x) > len(y):
        return 1
    if len(x) < len(y):
        return -1
    for i in range(len(x)):
        if x[i] > y[i]:
            return 1
        if x[i] < y[i]:
            return -1
    return 0


def sumar_binarios(x, y):
    # Sumador completo: usa las compuertas del punto 2
    largo = len(x)
    if len(y) > largo:
        largo = len(y)
    x = rellenar_ceros(x, largo)
    y = rellenar_ceros(y, largo)
    resultado = ""
    acarreo = 0
    for i in range(largo - 1, -1, -1):
        bit_x = int(x[i])
        bit_y = int(y[i])
        diferentes = compuerta_xor(bit_x, bit_y)
        bit_suma = compuerta_xor(diferentes, acarreo)
        acarreo = compuerta_or(compuerta_and(bit_x, bit_y), compuerta_and(diferentes, acarreo))
        resultado = str(bit_suma) + resultado
    if acarreo == 1:
        resultado = "1" + resultado
    return quitar_ceros(resultado)


def restar_binarios(x, y):
    # Resta con préstamo (x debe ser >= y; el signo se maneja afuera)
    largo = len(x)
    if len(y) > largo:
        largo = len(y)
    x = rellenar_ceros(x, largo)
    y = rellenar_ceros(y, largo)
    resultado = ""
    prestamo = 0
    for i in range(largo - 1, -1, -1):
        bit_x = int(x[i])
        bit_y = int(y[i])
        diferentes = compuerta_xor(bit_x, bit_y)
        bit_resta = compuerta_xor(diferentes, prestamo)
        pide_1 = compuerta_and(compuerta_not(bit_x), bit_y)
        pide_2 = compuerta_and(compuerta_not(diferentes), prestamo)
        prestamo = compuerta_or(pide_1, pide_2)
        resultado = str(bit_resta) + resultado
    return quitar_ceros(resultado)


def multiplicar_binarios(x, y):
    # Suma y desplazamiento: por cada bit 1 del multiplicador se suma x corrido
    resultado = "0"
    desplazamiento = ""
    for i in range(len(y) - 1, -1, -1):
        if y[i] == "1":
            resultado = sumar_binarios(resultado, x + desplazamiento)
        desplazamiento = desplazamiento + "0"
    return resultado


def convertir_bases():
    base_origen = pedir_base("Base del número que va a ingresar (2, 8, 10 o 16): ")
    numero = pedir_numero_en_base(base_origen)
    base_destino = pedir_base("Base a la que desea convertirlo (2, 8, 10 o 16): ")
    valor_decimal = a_decimal(numero, base_origen)
    resultado = de_decimal(valor_decimal, base_destino)
    print()
    print(numero, "(base", base_origen, ") = ", resultado, "(base", base_destino, ")")
    print("Paso intermedio: el valor decimal es", valor_decimal)


def operar_binarios(opcion):
    print("Ingrese dos números binarios.")
    x = pedir_numero_en_base(2)
    y = pedir_numero_en_base(2)
    x = quitar_ceros(x)
    y = quitar_ceros(y)
    print()
    if opcion == "2":
        print(x, "+", y, "=", sumar_binarios(x, y), " (en decimal:", a_decimal(x, 2), "+", a_decimal(y, 2), ")")
    elif opcion == "3":
        if comparar_binarios(x, y) >= 0:
            print(x, "-", y, "=", restar_binarios(x, y), " (en decimal:", a_decimal(x, 2), "-", a_decimal(y, 2), ")")
        else:
            print(x, "-", y, "= -" + restar_binarios(y, x), " (el resultado es negativo)")
    else:
        print(x, "x", y, "=", multiplicar_binarios(x, y), " (en decimal:", a_decimal(x, 2), "x", a_decimal(y, 2), ")")


def submenu_bases(variables):
    while True:
        mostrar_variables(variables)
        print("CONVERSOR DE BASES NUMÉRICAS")
        print(" 1. Convertir un número entre bases (2, 8, 10, 16)")
        print(" 2. Sumar números binarios")
        print(" 3. Restar números binarios")
        print(" 4. Multiplicar números binarios")
        print(" 5. Limpiar pantalla")
        print(" 0. Regresar al menú principal")
        opcion = input("Elija una opción: ")
        if opcion == "0":
            break
        elif opcion == "1":
            convertir_bases()
        elif opcion == "2" or opcion == "3" or opcion == "4":
            operar_binarios(opcion)
        elif opcion == "5":
            limpiar_pantalla()
        else:
            print("Opción no válida.")


# ------------------------------------------------------------------
# PUNTO OPCIONAL B: CALCULADORA DE CONJUNTOS
# Un conjunto se representa con una lista sin elementos repetidos.
# ------------------------------------------------------------------
def pertenece(elemento, conjunto):
    for x in conjunto:
        if x == elemento:
            return True
    return False


def union(a, b):
    resultado = []
    for x in a:
        if pertenece(x, resultado) == False:
            resultado.append(x)
    for x in b:
        if pertenece(x, resultado) == False:
            resultado.append(x)
    return resultado


def interseccion(a, b):
    resultado = []
    for x in a:
        if pertenece(x, b):
            resultado.append(x)
    return resultado


def diferencia(a, b):
    # Elementos de a que NO están en b
    resultado = []
    for x in a:
        if pertenece(x, b) == False:
            resultado.append(x)
    return resultado


def complemento(a, universal):
    return diferencia(universal, a)


def diferencia_simetrica(a, b):
    return union(diferencia(a, b), diferencia(b, a))


def producto_cartesiano(a, b):
    resultado = []
    for x in a:
        for y in b:
            resultado.append((x, y))
    return resultado


def conjuntos_iguales(a, b):
    if len(a) != len(b):
        return False
    for x in a:
        if pertenece(x, b) == False:
            return False
    return True


def texto_conjunto(conjunto):
    if len(conjunto) == 0:
        return "{ }  (conjunto vacío)"
    texto = "{"
    primero = True
    for x in conjunto:
        if primero:
            texto = texto + x
            primero = False
        else:
            texto = texto + ", " + x
    return texto + "}"


def texto_producto(pares):
    if len(pares) == 0:
        return "{ }  (conjunto vacío)"
    texto = "{"
    primero = True
    for par in pares:
        par_texto = "(" + par[0] + ", " + par[1] + ")"
        if primero:
            texto = texto + par_texto
            primero = False
        else:
            texto = texto + ", " + par_texto
    return texto + "}"


def ingresar_conjunto(nombre, universal, es_universal):
    conjunto = []
    print("Conjunto", nombre, "- escriba un elemento por vez (ENTER vacío para terminar).")
    while True:
        elemento = input("  Elemento: ")
        if elemento == "":
            break
        if es_universal == False and pertenece(elemento, universal) == False:
            print("  Ese elemento no está en el universal U. No se agregó.")
        elif pertenece(elemento, conjunto):
            print("  Elemento repetido: un conjunto no repite elementos.")
        else:
            conjunto.append(elemento)
    return conjunto


def ingresar_todos_los_conjuntos(conjuntos):
    while True:
        universal = ingresar_conjunto("U (universal)", CONJUNTO_VACIO, True)
        if len(universal) > 0:
            break
        print("El universal no puede estar vacío. Intente de nuevo.")
    conjuntos[0] = universal
    conjuntos[1] = ingresar_conjunto("A", universal, False)
    conjuntos[2] = ingresar_conjunto("B", universal, False)
    conjuntos[3] = ingresar_conjunto("C", universal, False)


def mostrar_conjuntos(conjuntos):
    print()
    print(" U =", texto_conjunto(conjuntos[0]))
    print(" A =", texto_conjunto(conjuntos[1]))
    print(" B =", texto_conjunto(conjuntos[2]))
    print(" C =", texto_conjunto(conjuntos[3]))


def pedir_conjunto(conjuntos, mensaje):
    # Pide U, A, B o C y devuelve el conjunto correspondiente
    while True:
        texto = input(mensaje)
        if texto == "U" or texto == "u":
            elegido = conjuntos[0]
            break
        elif texto == "A" or texto == "a":
            elegido = conjuntos[1]
            break
        elif texto == "B" or texto == "b":
            elegido = conjuntos[2]
            break
        elif texto == "C" or texto == "c":
            elegido = conjuntos[3]
            break
        print("Conjunto no válido. Escriba U, A, B o C.")
    return elegido


def operar_conjuntos(opcion, conjuntos):
    universal = conjuntos[0]
    if opcion == "6":
        a = pedir_conjunto(conjuntos, "Conjunto del que quiere el complemento (U, A, B o C): ")
        print("Complemento =", texto_conjunto(complemento(a, universal)))
    else:
        a = pedir_conjunto(conjuntos, "Primer conjunto (U, A, B o C): ")
        b = pedir_conjunto(conjuntos, "Segundo conjunto (U, A, B o C): ")
        if opcion == "3":
            print("Unión =", texto_conjunto(union(a, b)))
        elif opcion == "4":
            print("Intersección =", texto_conjunto(interseccion(a, b)))
        elif opcion == "5":
            print("Diferencia (primero - segundo) =", texto_conjunto(diferencia(a, b)))
        elif opcion == "7":
            print("Diferencia simétrica =", texto_conjunto(diferencia_simetrica(a, b)))
        else:
            print("Producto cartesiano =", texto_producto(producto_cartesiano(a, b)))


def calcular_expresiones(conjuntos):
    universal = conjuntos[0]
    a = conjuntos[1]
    b = conjuntos[2]
    c = conjuntos[3]
    print()
    # i. (A U C) U (B ∩ C)
    r1 = union(union(a, c), interseccion(b, c))
    print(" i.   (A U C) U (B ∩ C) =", texto_conjunto(r1))
    if conjuntos_iguales(r1, union(a, c)):
        print("      Verificación: coincide con A U C (B ∩ C ya está dentro de C)")
    # ii. (A U B U C)'
    r2 = complemento(union(union(a, b), c), universal)
    print(" ii.  (A U B U C)' =", texto_conjunto(r2))
    simplificado = interseccion(interseccion(complemento(a, universal), complemento(b, universal)),
                                complemento(c, universal))
    if conjuntos_iguales(r2, simplificado):
        print("      Verificación: coincide con A' ∩ B' ∩ C' (De Morgan)")
    # iii. (A ∩ C) U (B - C)
    r3 = union(interseccion(a, c), diferencia(b, c))
    print(" iii. (A ∩ C) U (B - C) =", texto_conjunto(r3))
    # iv. (A U B) ∩ (A U B')
    r4 = interseccion(union(a, b), union(a, complemento(b, universal)))
    print(" iv.  (A U B) ∩ (A U B') =", texto_conjunto(r4))
    if conjuntos_iguales(r4, a):
        print("      Verificación: coincide con A (A U (B ∩ B') = A U vacío)")
    # v. C ∩ [(A Δ B)' - (C' Δ A')]
    izquierda = complemento(diferencia_simetrica(a, b), universal)
    derecha = diferencia_simetrica(complemento(c, universal), complemento(a, universal))
    r5 = interseccion(c, diferencia(izquierda, derecha))
    print(" v.   C ∩ [(A Δ B)' - (C' Δ A')] =", texto_conjunto(r5))
    if conjuntos_iguales(r5, interseccion(interseccion(a, b), c)):
        print("      Verificación: coincide con A ∩ B ∩ C")


def submenu_conjuntos(variables, conjuntos):
    while True:
        mostrar_variables(variables)
        print("CALCULADORA DE CONJUNTOS")
        print(" 1. Ingresar U, A, B y C")
        print(" 2. Mostrar los conjuntos")
        print(" 3. Unión")
        print(" 4. Intersección")
        print(" 5. Diferencia")
        print(" 6. Complemento")
        print(" 7. Diferencia simétrica")
        print(" 8. Producto cartesiano")
        print(" 9. Calcular las cinco expresiones del enunciado (i a v)")
        print("10. Limpiar pantalla")
        print(" 0. Regresar al menú principal")
        opcion = input("Elija una opción: ")
        conjuntos_listos = len(conjuntos[0]) > 0
        if opcion == "0":
            break
        elif opcion == "1":
            ingresar_todos_los_conjuntos(conjuntos)
        elif opcion == "10":
            limpiar_pantalla()
        elif opcion >= "2" and opcion <= "9" and len(opcion) == 1:
            if conjuntos_listos == False:
                print("Primero ingrese los conjuntos (opción 1).")
            elif opcion == "2":
                mostrar_conjuntos(conjuntos)
            elif opcion == "9":
                calcular_expresiones(conjuntos)
            else:
                operar_conjuntos(opcion, conjuntos)
        else:
            print("Opción no válida.")


# ------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------
def mostrar_menu_principal(variables):
    mostrar_variables(variables)
    print("MENÚ PRINCIPAL")
    print(" 1. Ingresar las variables booleanas A, B, C, D")
    print(" 2. Mostrar el valor actual de A, B, C, D")
    print(" 3. Lector de compuertas")
    print(" 4. Circuitos lógicos")
    print(" 5. Conversor de bases numéricas")
    print(" 6. Calculadora de conjuntos")
    print(" 7. Limpiar pantalla")
    print(" 0. Salir del programa")


def main():
    variables = [VALOR_SIN_ASIGNAR, VALOR_SIN_ASIGNAR, VALOR_SIN_ASIGNAR, VALOR_SIN_ASIGNAR]
    conjuntos = [CONJUNTO_VACIO, CONJUNTO_VACIO, CONJUNTO_VACIO, CONJUNTO_VACIO]
    while True:
        mostrar_menu_principal(variables)
        opcion = input("Elija una opción: ")
        if opcion == "0":
            print("Hasta luego.")
            break
        elif opcion == "1":
            ingresar_variables(variables)
        elif opcion == "2":
            if variables_ingresadas(variables):
                print("Valores actuales: A =", variables[0], " B =", variables[1],
                      " C =", variables[2], " D =", variables[3])
            else:
                print("Aún no se han ingresado las variables (opción 1).")
        elif opcion == "7":
            limpiar_pantalla()
        elif opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":
            if variables_ingresadas(variables) == False:
                print("Primero debe ingresar las variables A, B, C y D (opción 1).")
            elif opcion == "3":
                submenu_compuertas(variables)
            elif opcion == "4":
                submenu_circuitos(variables)
            elif opcion == "5":
                submenu_bases(variables)
            else:
                submenu_conjuntos(variables, conjuntos)
        else:
            print("Opción no válida.")
main()