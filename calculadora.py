print ("Calculadora Simples")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 -  Divisão")

opcao = input ("Escolha uma operação: ")

if opcao == "1":
   print("Resultado: ", n1 + n2)
elif opcao == "2":
   print("Resultado: ", n1 - n2)
elif opcao == "3":
   print("Resultado: ", n1 * n2)
elif opcao == "4":
   if n2 == 0:
       print("Erro: Divisão por zero.")
   else:
       print("Resultado: ", n1 / n2)
else:
    print("Opção inválida.")
