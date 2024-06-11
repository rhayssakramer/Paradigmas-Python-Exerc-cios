# Funções Matemáticas
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: A divisão por zero não é permitida!"
    return x / y

# Menu de Operações
def menu():
    print("\nEscolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisaão")
    print("5. Encerrar")

# Menu de Entradas e Saídas
def main():
    while True:
        menu()
        
        try:
            escolha = int(input("Digite uma operação: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número de 1 a 5.")
            continue
        
        if escolha == 5:
            print("Obrigada por usar a calculadora Digital!")
            break
        
        if escolha in [1, 2, 3, 4]:
            # Captura os números e trata possíveis erros de entrada
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, digite números válidos.")
                continue

            if escolha == 1:
                print(f"Resultado: {soma(num1, num2)}")
            elif escolha == 2:
                print(f"Resultado: {subtracao(num1, num2)}")
            elif escolha == 3:
                print(f"Resultado: {multiplicacao(num1, num2)}")
            elif escolha == 4:
                resultado = divisao(num1, num2)
                print(f"Resultado: {resultado}")
        else:
            print("Escolha inválida! Por favor, selecione uma opção de 1 a 5.")

if __name__ == "__main__":
    main()