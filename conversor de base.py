#Conversão de Bases
print("Conversor para Decimal")
base = int(input("Qual a base do valor que será convertida? "))

def verificarBase(b): 
    n = input("Qual o valor que será convertido? ")
    for key in n:     
        value = int(key)
        if(value > b-1 or value < 0):
            print("Erro! A base não condiz com o valor, digite novamente! ")
            verificarBase(b)
    else:
        return n


valor = verificarBase(base)

def converterBase(n, b):
    numeroConvertido = 0
    for i in range(len(n)):
        value = int(n[i])
        print(f'{value}*{b}^({len(n)-i-1}) ')
        numeroConvertido += value*b**(len(n)-i-1)
    return numeroConvertido

print(converterBase(valor, base))
