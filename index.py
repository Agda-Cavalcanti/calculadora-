#Faça uma função calculadora de dois números com três parâmetros: 
# os dois primeiros serão os números da operação e o terceiro será 
# a entrada que definirá a operação a ser executada. Considera a seguinte definição:

#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
import time 
continuar = True
def calculadora (a,b, operador):
    if (operador == "1"):
        return a + b
    elif (operador == "2"):
        return a - b
    elif (operador == "3"):
        return a * b
    elif (operador == "4"):
        return a / b
    else:
       return 0
    
    


while continuar == True :
    print("\n||||  CALCULADORA  |||\n\n")
    time.sleep(1)
    operador = str(input('''Lista de operações:\n
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

'''))
    time.sleep(1)

    if (operador == "1") or (operador == "2") or (operador == "3") or (operador == "4"):
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))

        resultado = calculadora(a,b,operador)
        print("\nResultado: ", resultado)

    elif (operador == "0"):
        print("----------------------")
        print("Fim da calculadora")
        print("----------------------")
        continuar = False
    else:
        print("----------------------")
        time.sleep(1)
        print("Essa opção não existe ")
        time.sleep(1)
        print("----------------------")
        time.sleep(1)
        
        

    



