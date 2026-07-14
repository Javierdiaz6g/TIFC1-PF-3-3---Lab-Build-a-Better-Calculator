def addmultiplenumbers(numbers):
    total = sum(numbers)
    return total

def multiplymultiplenumbers(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

def isiteven(num):
    if isinstance(num, int):
        return num % 2 == 0
    elif isinstance(num, float):
        return num.is_integer() and num % 2 == 0
    return False

def isitaninteger(num):
    if isinstance(num, int):
        return True
    elif isinstance(num, float):
        return num.is_integer()
    return False

def main():
    # Mensaje inicial requerido por las instrucciones
    print("¡Hola, aprendices!")
    mi_lista = [1, 2, 3, 4]
    print(addmultiplenumbers(mi_lista))
    print(multiplymultiplenumbers(mi_lista))
    print(isiteven(3))
    print(isitaninteger(3.5))



if __name__ == "__main__":
    main()

