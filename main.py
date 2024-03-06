#1) Observe o trecho de código abaixo: Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0
k = 0

while k < indice:
    k = k+1
    soma = soma + k

print(soma)
# RESPOSTA: no final do processamento soma = 91

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

numero = int(input("Digite um número inteiro: "))
anterior = 0
atual = 1

while atual <= numero:
    if atual == numero:
        print(f"O número {numero} está na sequência de Fibonacci.")
        break
    proximo = anterior + atual
    anterior = atual
    atual = proximo
if atual > numero:
    print(f"O número {numero} não está na sequência de Fibonacci.")



#5) Escreva um programa que inverta os caracteres de um string.
palavra = input("Digite uma palavra: ")
invertida = ''

for i in range(len(palavra) - 1, -1, -1):
    invertida += palavra[i]
print("A palavra invertida é:", invertida)