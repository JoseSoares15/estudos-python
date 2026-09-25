# Quando você utiliza o comando `input()` para ler algo digitado pelo usuário no teclado, o Python trata a entrada nativamente como uma string (str), ou seja, como um texto.

# Se você tentar somar dois valores lidos direto com o input() (como n1 + n2), o operador + atuará realizando uma concatenação (juntando os textos) em vez de uma adição matemática. Por exemplo, se o usuário digitar 3 e 2, o resultado impresso será 32 em vez de 5.

# Para permitir cálculos e manipular dados corretamente, o Python utiliza quatro tipos primitivos principais:

# 1. int (Inteiros): Números inteiros, positivos, negativos ou nulos, sem parte fracionária (ex.: 7, -4, 0, 9875).

# 2. float (Ponto Flutuante / Reais): Números decimais ou reais, usando o ponto (.) como separador (ex.: 4.5, 0.076, -15.23, 7.0).

# 3. bool (Booleanos / Lógicos): Aceita apenas dois valores: True (Verdadeiro) e False (Falso), ambos escritos obrigatoriamente com a primeira letra maiúscula. Quando convertido em booleano, um dado com conteúdo avalia como True, enquanto um dado vazio avalia como False.

# 4. str (Strings / Caracteres): Textos delimitados por aspas simples ('Olá') ou aspas duplas ("Olá"), incluindo palavras, símbolos ou até uma string vazia ('').

# Para resolver o problema do input(), envolve-se o comando na função do tipo desejado. Ao usar int(input('...')), o texto digitado é convertido para um número inteiro na memória, permitindo realizar operações matemáticas normalmente.

# Em vez de concatenar várias vírgulas e aspas no comando print(), o Python permite usar chaves ({}) no texto como "máscaras" de substituição combinadas com o método .format().

#Exemplo: print('A soma entre {} e {} vale {}'.format(n1, n2, s)). As chaves serão substituídas pelas variáveis passadas dentro do .format() na exata ordem em que aparecem.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} é {}' .format(n1, n2, s))