# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor
n = int(input('Digite um número: '))
a = n-1
s = n+1
print('O número antecessor de {} é {}. \nO sucessor é {}' .format(n, a, s))

# Ou pode ser realizado dessa forma

#n = int(input('Digite um número: '))
#print('O número antecessor de {} é {}. \nO sucessor é {}' .format(n, (n-1), (n+1)))

#Quanto menos variaveis, mais memória é economizada no dispositivo