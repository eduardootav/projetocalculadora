print("=== CALCULADORA ===")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\nEscolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("\nOpção: ")

if opcao == "1":
    print(f"\nResultado: {n1 + n2}")

elif opcao == "2":
    print(f"\nResultado: {n1 - n2}")

elif opcao == "3":
    print(f"\nResultado: {n1 * n2}")

elif opcao == "4":
    if n2 == 0:
        print("\nErro: divisão por zero não é permitida.")
    else:
        print(f"\nResultado: {n1 / n2}")

else:
    print("\nOpção inválida.")
