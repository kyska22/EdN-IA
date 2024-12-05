"""
Escreva um programa que leia o número de um funcionário, seu númeo de horas trabalhadas, o valor que recebe por hora 
e calcule o salário desse funcionário. 
A seguir mostre o número e o salário do funcionário, com duas casas decimais
"""

def calcula_salario():
    codigo_funcionario = int(input("escreva o código do funcionario: "))
    horas_trabalhadas = int(input("Diguite a quantidde de horas trabalhadas: "))
    valor_hora = float(input("Digite o valor hora: "))

    salario = horas_trabalhadas * valor_hora

    print(f"NUMBER = {codigo_funcionario}")
    print(f"SALARIO = UR$ {salario:.2f}")

calcula_salario()
