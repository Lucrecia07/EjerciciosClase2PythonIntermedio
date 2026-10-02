import json

# Ejercicio 1.
# Escribe un programa que intente dividir dos números. 
# Si el segundo número es cero, captura la excepción ZeroDivisionError
# y muestra un mensaje de error al usuario.

print("\n* Ejercicio 1. *")
print("** Este programa divide dos números ingresados por el usuario. ")
print("Si el segundo número es cero, captura la excepción")
print("y muestra un mensaje al usuario. **\n")

# Definición de la función para dividir dos números enteros.
def dividir(dividendo : int | float, divisor : int | float) -> int|float: 
    """
    Esta función divide dos números.
    Tiene 2 parámetros de tipo entero o flotante.
    Retorna el resultado de la división, de tipo entero o flotante.
    """
    return round((dividendo/divisor),2)

# Definición de la función para solicitar al usuario un número entero o flotante.
def solicitar_numero(mensaje : str) -> float:
    """
    Esta función solicita al usuario un número a través de un mensaje.
    Tiene un parámetro de tipo string.
    Retorna el número ingresado por el usuario, casteando a tipo flotante.
    """
    while True:
        try:
            numero_ingresado = float(input(mensaje))
        except ValueError:
            print("El valor ingresado debe ser numérico.")
        else:
            return numero_ingresado

while True:
    try:
        # Solicitar al usuario que ingrese el dividendo.
        primer_numero = solicitar_numero("Ingrese el primer número y presione enter: ")
        while True:
            try:
                # Solicitar al usuario que ingrese el divisor.
                segundo_numero = solicitar_numero("Ingrese el segundo número y presione enter: ")
                # Llamar a la función para que realice la división.
                resultado = dividir(primer_numero, segundo_numero)
            except ZeroDivisionError:
                print("No se puede dividir por cero. ")
            else:
                # Mostrar el resultado de la división de los números ingresados por el usuario.
                print(f"El resultado de dividir: {primer_numero} / {segundo_numero} es: {resultado}")
                break
    except Exception as e:
        print("Ocurrió un error inesperado.")
    else:
        break
    finally:
        print("* Fin del programa. *\n")



print("* Otra manera de resolver el ejercicio 1. *")
# Definición de la función para dividir dos números enteros.
def dividir(dividendo : int | float, divisor : int | float) -> int|float: 
    """
    Esta función divide dos números.
    Tiene 2 parámetros de tipo entero o flotante.
    Retorna el resultado de la división, de tipo entero o flotante.
    """
    return round((dividendo/divisor),2)

try:
    # Forzar la excepción.
    dividendo = 20
    divisor = 0
    print(f"Intento de dividir: {dividendo} / {divisor}")
    dividir(dividendo, divisor)
except ZeroDivisionError:
    print("No se puede dividir por cero.")

print("---------------------------------------------------------------")

# Ejercicio 2.
# Escribe un programa que intente sumar un número y una cadena.
# Si se produce un error de tipo, captura la excepción TypeError
# y muestra un mensaje de error al usuario.

print("\n* Ejercicio 2. *")
print("** Este programa intenta sumar un número y una cadena ingresados por el usuario. ")
print("Captura la excepción y muestra un mensaje al usuario. **")

# Definición de la función para sumar dos números enteros.
def sumar(primer_numero : int | float, segundo_numero : int | float) -> int|float: 
    """
    Esta función suma dos números.
    Tiene 2 parámetros de tipo entero o flotante.
    Retorna el resultado de la suma, de tipo entero o flotante.
    """
    return (primer_numero + segundo_numero)

# Definición de la función para solicitar al usuario un número entero o flotante.
def solicitar_numero(mensaje : str) -> float:
    """
    Esta función solicita al usuario un número a través de un mensaje.
    Tiene un parámetro de tipo string.
    Retorna el número ingresado por el usuario, casteando a tipo flotante.
    """
    while True:
        try:
            numero_ingresado = float(input(mensaje))
        except ValueError:
            print("El valor ingresado debe ser numérico.")
        else:
            return numero_ingresado

# Definición de la función para solicitar al usuario una cadena de texto.
def solicitar_cadena(mensaje : str) -> str:
    """
    Esta función solicita al usuario una cadena.
    Tiene un parámetro de tipo string.
    Retorna la cadena ingresada por el usuario.
    """
    while True:
        cadena_ingresada = input(mensaje).strip()
        if cadena_ingresada.isalpha():
            return cadena_ingresada
        else:
            print("Debe ingresar una palabra.")


try:
    # Solicitar al usuario que ingrese un numero.
    numero = solicitar_numero("Ingrese un número y presione enter: ")
    # Solicitar al usuario que ingrese una cadena.
    # Para forzar el error de tipo.
    cadena_de_texto = solicitar_cadena("Ingrese una palabra presione enter: ")
    # Llamar a la función para que realice la suma.
    resultado = sumar(numero, cadena_de_texto)
except TypeError:
    # Capturar la excepción y muestra un mensaje de error al usuario.
    print("El tipo de dato es inapropiado para sumar. ")
    print("No se puede sumar un número y una cadena de texto.")
except Exception as e:
    # Capturar la excepción y muestra un mensaje de error al usuario.
    print("Ocurrió un error inesperado.")
else:
    # Mostrar el resultado de la suma de los números ingresados por el usuario.
    print(f"El resultado de sumar: {numero} + {cadena_de_texto} es: {resultado}")
finally:
    print("* Fin del programa. *\n")






print("* Otra manera de resolver el ejercicio 2. *")
print("\n* Ejercicio 2. *")
print("** Este programa intenta sumar un número y una cadena ingresados por el usuario. ")
print("Captura la excepción y muestra un mensaje al usuario. **")

# Definición de la función para sumar dos números enteros.
def sumar_numeros(primer_numero : int | float, segundo_numero : int | float) -> int|float: 
    """
    Esta función suma dos números.
    Tiene 2 parámetros de tipo entero o flotante.
    Retorna el resultado de la suma, de tipo entero o flotante.
    """
    return (primer_numero + segundo_numero)

# Definición de la función para solicitar al usuario un número entero o flotante.
def solicitar_numeros(mensaje : str) -> float:
    """
    Esta función solicita al usuario un número a través de un mensaje.
    Tiene un parámetro de tipo string.
    Retorna el número ingresado por el usuario, casteando a tipo flotante.
    Sino puede castear, retorna un string, para forzar el error de tipo.
    """
    numero_ingresado = input(mensaje).strip()
    try:
        numero_ingresado = float(numero_ingresado)
    except ValueError:
        return numero_ingresado
    else:
        return numero_ingresado

try:
    # Solicitar al usuario que ingrese un numero.
    numero1 = solicitar_numeros("Ingrese el primer número y presione enter: ")
    # Solicitar al usuario que ingrese una cadena.
    # Para forzar el error de tipo.
    numero2 = solicitar_numeros("Ingrese el segundo número y presione enter: ")
    # Llamar a la función para que realice la suma.
    resultado1 = sumar_numeros(numero1, numero2)
except TypeError:
    # Capturar la excepción y muestra un mensaje de error al usuario.
    print("El tipo de dato es inapropiado para sumar. ")
    print("No se puede sumar un número y una cadena de texto.")
except Exception as e:
    # Capturar la excepción y muestra un mensaje de error al usuario.
    print("Ocurrió un error inesperado.")
else:
    # Mostrar el resultado de la suma de los números ingresados por el usuario.
    print(f"El resultado de sumar: {numero1} + {numero2} es: {resultado1}")
finally:
    print("* Fin del programa. *\n")








print("* Otra manera de resolver el ejercicio 2. *")
print("\n* Ejercicio 2. *")
print("** Este programa intenta sumar un número y una cadena. **")

# Definición de la función para sumar dos números de tipo entero o flotante.
def sumar(primer_numero : int | float, segundo_numero : int | float)-> int | float: 
    """
    Esta función suma dos números.
    Tiene 2 parámetroso de tipo entero o flotante.
    Retorna el resultado de la suma, de tipo entero o flotante.
    """
    return primer_numero + segundo_numero

try:
    numero = 15
    cadena = "palabra"
    print(f"Intento de sumar, {numero} + {cadena}")
    # Forzar el error de tipo.
    sumar(numero, cadena)
except TypeError:
    print("Argumento/s inapropiado/s, no se puede sumar un número y una cadena.")
finally:
    print("* Fin del programa. *\n")


print("---------------------------------------------------------------")

# Ejercicio 3.
# Escribe un programa que intente acceder a una clave que no existe 
# en un diccionario. Si se produce una excepción KeyError,
# captura la excepción y muestra un mensaje de error al usuario.

print("\n* Ejercicio 3. *")
print("** Este programa, si intenta acceder a una clave que no existe en un diccionario,  ")
print("captura la excepción y muestra un mensaje de error al usuario. \n ")


# Definición de la función para mostrar clave-valor de un diccionario.
def mostrar_diccionario(nombre_diccionario):
    """
    Esta función muestra clave-valor de un diccionario.
    """
    for i,x in nombre_diccionario.items():
        print(i,x)

# Definición de la función para mostar el valor de un diccionario, dada la clave.
def mostrar_valor_diccionario(nombre_diccionario, clave_diccionario):
    """
    Esta función el valor de un diccionario, dada la clave.
    """
    return nombre_diccionario[clave_diccionario]

# Creación de un diccionario.
datos_personales = {
    "nombre": "Juan", 
    "apellido": "Gomez", 
    "dni": "37.452.365"
}

# Mostrar el diccionario.
print("El diccionario contiene la siguiente información: ")
mostrar_diccionario(datos_personales)

while True:
    try:
        # Solicitar la clave del diccionario al usuario.
        clave_ingresada = input("Por favor, ingrese la clave del valor que desea acceder y presione enter: ").strip().lower()
        # Obtener el valor de la clave.
        valor_obtenido = mostrar_valor_diccionario(datos_personales, clave_ingresada)
    except KeyError:
        # Capturar la excepción.
        print(f"La clave ingresada: {clave_ingresada}, no existe.")
    else:
        # Mostrar el valor de la clave ingresada.
        print(f"El valor de la clave {clave_ingresada}, es: {valor_obtenido}")
        break

print("* Fin del programa. *")

print("---------------------------------------------------------------")

# Ejercicio 4.
# Escribe un programa que intente abrir un archivo que no existe.
# Si se produce una excepción FileNotFoundError, captura la excepción
# y muestra un mensaje de error al usuario. 
# Sin embargo, también intenta crear el archivo si no existe.


print("\n * Ejercicio 4. * ")
print("\n** Este programa, si se intenta abrir un archivo que no existe, ")
print("captura la excepción mostrando un mensaje de error al usuario, ")
print("y crea el archivo si no existe. **\n")

# Lista de caracteres no permitidos para nombre de un archivo.
caracteres_no_permitidos = ["<", ">", ":", '"', "/", "\\", "|", "¿", "?", "*", "¡", "!"]

# Definición de la función para comprobación de nombre de archivo.
def comprobar_nombre_archivo(nombre):
    """
    Esta función comprueba el nombre de un archivo.
    Tiene un parámetro.
    Retorna si el nombre del archivo es o no un nombre permitido.
    """
    if nombre == "":
        print("El nombre del archivo no puede estar vacío.")
        return False
    for caracter in nombre:
        if caracter in caracteres_no_permitidos:
            print("El nombre del archivo no puede contener caracteres especiales.")
            return False
    return True

# Definición de la función para comprobación de extensión del archivo.
def comprobar_extension(extension):
    """
    Esta función comprueba la extensión del archivo.
    Tiene un parámetro.
    Retorna si la extensión del archivo es correcta o no.
    """ 
    if extension == "txt" or extension == "py" or extension == "json":
        return True
    else:
        print("La extensión del archivo ingresada es incorrecta.")
        return False

# Definición de la función para abrir un archivo.        
def abrir_archivo(archivo_nombre, extension):
    """
    Esta función abre un archivo de acuerdo al tipo.
    Tiene dos parámetros que corresponden al nombre y extensión del archivo que se desea abrir.
    Abre el archivo correspondiente.
    """
    match extension:
        case "txt":
            with open(f'{archivo_nombre}.{extension}', 'r', encoding='UTF-8') as f:
                return f.read()
        case "py":
            with open(f'{archivo_nombre}.{extension}', 'r', encoding='UTF-8') as f:
                return f.read()
        case "json":
            with open(f'{archivo_nombre}.{extension}', 'r', encoding='UTF-8') as f:
                return json.load(f)

# Definición de la función para crear un archivo.
def crear_archivo(archivo_nombre, extension):
    """
    Esta función crea un archivo con un contenido inicial, de acuerdo a su extensión.
    Tiene dos parámetros que corresponden al nombre y extensión del archivo a crear.
    Crea el archivo correspondiente.
    """
    match extension:
        case "txt":
            with open(f'{archivo_nombre}.{extension}', 'w', encoding='UTF-8') as f:
                f.write(f'¡Hola!. Soy el archivo: {archivo_nombre}.{extension}')
        case "py":
            with open(f'{archivo_nombre}.{extension}', 'w', encoding='UTF-8') as f:
                f.write(f'# ¡Hola!. Soy el archivo: {archivo_nombre}.{extension}')
        case "json":
            diccionario = {
                "nombre_archivo": f"{archivo_nombre}",
                "extension": f"{extension}"
            }
            with open(f'{archivo_nombre}.{extension}', 'w', encoding='UTF-8') as f:
                json.dump(diccionario,f,indent=4)



extension_correcta = False
nombre_correcto = False
try:
    # Comprobación del nombre del archivo.
    while nombre_correcto == False:
        nombre_archivo = input("Por favor, ingrese el nombre del archivo que desea abrir y presione enter: ").strip()
        nombre_correcto = comprobar_nombre_archivo(nombre_archivo)
    # Comprobación de la extensión del archivo.
    while extension_correcta == False:
        extension_archivo = input("Por favor, ingrese la extensión del archivo que desea abrir (txt/py/json) y presione enter: ").strip().lower()
        extension_correcta = comprobar_extension(extension_archivo)
    # Intenta abrir el archivo.
    contenido_del_archivo = abrir_archivo(nombre_archivo, extension_archivo)
    # print("El contenido del archivo es: ")
    # print(contenido_del_archivo)
except FileNotFoundError:
    # Captura la excepción.
    print(f"El archivo de nombre: {nombre_archivo} y extensión: {extension_archivo}, no existe.")
    crear_archivo(nombre_archivo, extension_archivo)
    print(f"Como dicho archivo no existe, fue creado como: {nombre_archivo}.{extension_archivo}")
except ValueError:
    # Captura la excepción.
    print("Por favor, debe ingresar un nombre para el archivo.")
else:
    print("El contenido del archivo es: ")
    print(contenido_del_archivo)
finally:
    print("* Fin del programa. *")


print("---------------------------------------------------------------")

# Ejercicio 5.
# Escribe un programa que intente dividir dos números. 
# Si el segundo número es cero, captura la excepción ZeroDivisionError.
# Si el primer número es un número no válido, captura la excepción
# ValueError. En cualquier caso, muestra un mensaje de error al usuario.

print("\n* Ejercicio 5. *")
print("** Este programa divide dos números ingresados por el usuario. **")

# Definición de la función para dividir dos números enteros.
def dividir(dividendo : int | float, divisor : int | float) -> int|float: 
    """
    Esta función divide dos números.
    Tiene 2 parámetros de tipo entero o flotante.
    Retorna el resultado de la división, de tipo entero o flotante.
    """
    return round((dividendo/divisor),2)

# Definición de la función para solicitar al usuario un número entero o flotante.
def solicitar_numero(mensaje : str) -> float:
    """
    Esta función solicita al usuario un número a través de un mensaje.
    Tiene un parámetro de tipo string.
    Retorna el número ingresado por el usuario, casteando a tipo flotante.
    """
    while True:
        try:
            numero_ingresado = float(input(mensaje))
        except ValueError:
            print("El valor ingresado debe ser numérico.")
        else:
            return numero_ingresado

while True:
    try:
        # Solicitar al usuario que ingrese el dividendo.
        primer_numero = solicitar_numero("Ingrese el primer número y presione enter: ")
        while True:
            try:
                # Solicitar al usuario que ingrese el divisor.
                segundo_numero = solicitar_numero("Ingrese el segundo número y presione enter: ")
                # Llamar a la función para que realice la división.
                resultado = dividir(primer_numero, segundo_numero)
            except ZeroDivisionError:
                print("No se puede dividir por cero. ")
            else:
                # Mostrar el resultado de la división de los números ingresados por el usuario.
                print(f"El resultado de dividir: {primer_numero} / {segundo_numero} es: {resultado}")
                break
    except Exception as e:
        print("Ocurrió un error inesperado.")
    else:
        break
    finally:
        print("* Fin del programa. *\n")