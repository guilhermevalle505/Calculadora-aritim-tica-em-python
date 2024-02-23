#calculadora aritimética
print('-------------------------------------------------------------------')
print('|                        calculadora ARITIMÉTICA                  |')
print('-------------------------------------------------------------------')

escolha = str(input("escolha seu operador aritimético: +,  -,  *, ou /"))
if escolha == "+":
  n1 = float(input("escolha um número "))
  n2 = float(input("escolha outro número "))
  soma = n1 + n2
  print("o resultado da sua soma é:{}".format(soma))
elif escolha == "-":
  n1 = float(input("escolha um número"))
  n2 = float(input("escolha outro número"))
  subtracao = n1 - n2
  print("o resultado a sua subtração é:{}".format(subtracao))
elif escolha == "*":
  n1 = float(input("escolha um número"))
  n2 = float(input("escolha outro número"))
  multiplicacao = n1 * n2
  print("o resultado da sua multiplicação é:{}".format(multiplicacao))
else:
  n1 = float(input("escolha um número"))
  n2 = float(input("escolha outro número"))
  divisao = n1 / n2
  print("o resultado da sua divisão é:{}".format(divisao))
  if n1 == 0 and n2 == 0:
    print(" ERRO! REINICIE O PROGRAMA!")