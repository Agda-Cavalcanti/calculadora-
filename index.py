#Faça uma função calculadora de dois números com três parâmetros: 
# os dois primeiros serão os números da operação e o terceiro será 
# a entrada que definirá a operação a ser executada. Considera a seguinte definição:

#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


def calculadora (a,b, operador):
    if operador == 1:
        resultado = a + b
    elif operador == 2:
        resultado = a - b
    elif operador == 3:
        resultado = a * b
    elif operador == 4:
        resultado = a / b
    else:
        resultado = 0
    
    return resultado


print("\n|  CALCULADORA  |\n\n")
a = int(input("Digite um valor: "))
b = int(input("Digite um outro valor: "))
operador = int(input("\nEscolha um número para as seguintes operações:\n\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n\n"))


resultado = calculadora(a,b,operador)
print("\nResultado: ", resultado)



