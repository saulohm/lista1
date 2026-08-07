"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""
print("Média das notas do ano")
#cada n com número é a variável nota de cada bimestre. Teremos da n1 até n4.
#entrada de dados
n1=float(input("Digite a nota do primeiro bimestre:"))
n2=float(input("Digite a nota do segundo bimestre:"))
n3=float(input("digite a nota do terceiro bimestre:"))
n4=float(input("digite a nota do quarto bimestre:"))
#processamento dos dados
media=(n1+n2+n3+n4)/4#este é o cálculo da media
#saída de dados
print("A média do ano é: ",media)