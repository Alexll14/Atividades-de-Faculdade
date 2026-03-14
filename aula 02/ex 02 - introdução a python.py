"""
1. Escreva um algoritmo que calcule a área de um triângulo cuja fórmula é base x altura / 2.
"""

base = float(input("digite a base : "))
altura = float(input("digite a altura : "))

area = base * altura / 2

print("A area é de : ", area)


"""
2. Escreva um algoritmo que leia horas, minutos e segundos do teclado e apresente o tempo total em segundos.
"""

segundos = float(input("Informe os segundos: "))
minutos = float(input("Informe os minutos: "))
horas = float(input("Informe os horas: "))

totalSegundos = horas * 3600 + minutos * 60 + segundos;

print("O tempo total em segundos é de :" , totalSegundos , " segundos.")

"""
3. Escreva um algoritmo que leia um número inteiro e apresente o seu antecessor e o seu sucessor.
"""

numero = float(input("Escrevas um número : "))

print("sucessor: ", numero + 1)
print("antecessor: ", numero - 1)

"""
4. Escreva um algoritmo que leia a nota de três provas de um aluno, calcule e escreva a média final deste aluno. Considere que a média é ponderada e que o peso das provas é 2 para a primeira prova, 3 para a segunda prova e 5 para a terceira prova.
"""

nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

print("Média do aluno: ", media)

"""
5. Escreva um algoritmo que leia uma temperatura em graus Celsius e a apresente convertida em graus Fahrenheit.
"""

celsius = float(input("Informe a temperatura em celsius: "))

fahrenheit = (celsius * 9)/5 + 32

print("A temperatura é de : " , fahrenheit , " fahrenheits")

"""
6. Escreva um algoritmo que apresente a conversão de um valor em reais para dólar, de acordo com a taxa de câmbio informada pelo usuário.
"""

reais = float(input("Informe o valor a ser convertido: "))
taxa = float(input("Informe a taxa de câmbio do dólar : "))

valorConvertido = reais / taxa

print("O valor convertido é de : ", valorConvertido)

"""
7. Escreva um algoritmo que calcule e mostre o consumo médio e a autonomia que um veículo ainda teria antes de um abastecimento de combustível. Considere que o veículo sempre seja abastecido até encher o tanque e que são fornecidas apenas a capacidade do tanque, a quantidade de litros abastecidos e a quilometragem percorrida desde o último abastecimento.
"""

capacidadeTanque = float(input("Informe quantos litros o tanque comporta: "))
litrosAbastecidos = float(input("Informe o valor em litros que foi abastecido: "))
quilometragemPercorrida = float(input("Informe a quilometragem que foi percorrida: "))

consumoMedio = quilometragemPercorrida / litrosAbastecidos
litrosRestantes = capacidadeTanque - litrosAbastecidos

autonomia = consumoMedio * litrosRestantes

print("O consumo médio foi de : ", consumoMedio)
print("O carro ainda pode percorrer : ", autonomia)

"""
8. Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o garçom. Escreva um algoritmo que leia o valor gasto pelo cliente em um restaurante e mostre o valor da gorjeta e o valor total a ser pago.
"""

conta = float(input("Informe o valor a ser pago: "))

taxa = conta * 0.10
total = conta + taxa

print("A gorjeta é de : ", taxa)
print("o preço total é de :", total)

"""
9. Escreva um algoritmo que leia o número de votos brancos, o número de votos nulos e o número de votos válidos em um município. Em seguida, calcule e escreva o percentual de votos brancos, nulos e válidos em relação ao total de eleitores do município.
"""

brancos = float(input("Informe o total de votos brancos: "))
nulos = float(input("Informe o total de votos nulos: "))
validos = float(input("Informe o total de votos validos: "))

eleitores = brancos + nulos + validos

brancos = brancos * 100 / eleitores
nulos = nulos * 100 / eleitores
validos = validos * 100 / eleitores

print(f"Porcentagem de Votos brancos: {brancos:.2f}%")
print(f"Porcentagem de Votos nulos: {nulos:.2f}%")
print(f"Porcentagem de Votos validos: {validos:.2f}%")

"""
10. Escreva um algoritmo que leia dois números inteiros e faça a troca de valores entre eles, apresentando as variáveis com seus valores trocados.
"""

valor1 = input("Informe o primeiro valor(ou texto): ")
valor2 = input("Informe o segundo valor(ou texto): ")

print(valor1, " : ", valor2)

temp = valor1
valor1 = valor2
valor2 = temp

print(valor1, " : ", valor2)