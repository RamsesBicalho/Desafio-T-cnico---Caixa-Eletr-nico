#Cabeçalho
print('-'*30)
print('{:^30}'.format ('Caixa Eletronico'))
print('-'*30)
print(f"Cédulas Disponiveis: 100, 50, 20, 10, 5, 2 reais.")

#Obter Valor Inteiro
def obter_valor_inteiro_multiplo():
    while True:
        try:
            valor = int(input("Qual valor você deseja sacar? R$: "))
            if valor % 2 == 0:
                return valor
            elif valor % 5 == 0:
                return valor
            else:
                print("Valor inválido! O número não é múltiplo de 2 ou 5.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro válido.")
# Contando Cédulas
numero_inteiro = obter_valor_inteiro_multiplo()

if numero_inteiro % 2 == 0:
    total = numero_inteiro
    cedulas = 100
    total_cedulas = 0
    
    while True:
            if total >= cedulas:
                total -= cedulas
                total_cedulas += 1
            else:
                if total_cedulas > 0:
                    print (f'Total de {total_cedulas} células de {cedulas} R$')
                if cedulas == 100:
                    cedulas = 50
                elif cedulas == 50:
                    cedulas = 20
                elif cedulas == 20:
                    cedulas = 10
                elif cedulas == 10:
                    cedulas = 2
                total_cedulas = 0
                if total == 0:
                    break
else:
    total = numero_inteiro
    cedulas = 100
    total_cedulas = 0
    
    while True:
            if total >= cedulas:
                total -= cedulas
                total_cedulas += 1
            else:
                if total_cedulas > 0:
                    print (f'Total de {total_cedulas} células de {cedulas} R$')
                if cedulas == 100:
                    cedulas = 50
                elif cedulas == 50:
                    cedulas = 20
                elif cedulas == 20:
                    cedulas = 10
                elif cedulas == 10:
                    cedulas = 5
                total_cedulas = 0
                if total == 0:
                    break

    
#Fim
print(f"Você sacou o valor: {numero_inteiro},00 R$. Volte Sempre.")