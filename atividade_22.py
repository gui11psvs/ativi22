# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
def somar_numeros():
    total = 0
    while True:
        numero = float(input("Digite um número (0 para parar): "))
        if numero == 0:
            break
        total += numero
    print(f"A soma total é: {total}")

somar_numeros()
