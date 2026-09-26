n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
sub = n1-n2
print('A soma vale {}' .format(s), end=' ')
print('A subtração vale {}' .format(sub))
print('A multiplicação vale {}' .format(m))
print('A divisão vale {:.2f}' .format(d))
print('A divisão inteira vale: {}' .format(di))
print('A exponenciação vale {}' .format(e))