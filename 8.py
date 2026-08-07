"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""
#entrada de dados
ganhahora=float(input("Digite quanto você ganha por hora:"))
horasmes=int(input("Digite quantas horas você trabalha no mês:"))
#processamento
ganha=ganhahora*horasmes
#saída dos dados
print("Você ganha ",ganha," por mês")