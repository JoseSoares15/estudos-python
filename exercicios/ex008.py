# escreva um programa que leia um valor em metros e o exiba converido em centimetros e milimetros (e mais)

m = float(input('Digite o metro: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print('A unidade de medida {}m equivale a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm' .format(m,km, hm, dam, dm, cm, mm))