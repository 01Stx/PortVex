def calcular(numero1, operador, numero2):
    if operador == "+":
        return numero1 + numero2
    elif operador == "-":
        return numero1 - numero2
    elif operador == "*":
        return numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
            raise ZeroDivisionError("Divisão por zero não permitida.")
        return numero1 / numero2
    else:
        raise ValueError("Operador inválido.")
