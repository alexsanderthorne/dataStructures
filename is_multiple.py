a = int(input("Digite o valor para o 1º nº : "))
b = int(input("Digite o valor para o 2º nº : "))

mi = False


def is_multiple(a, b, mi):
    if (a % b == 0):
        mi = True

        return mi


print(is_multiple(a, b, mi))
