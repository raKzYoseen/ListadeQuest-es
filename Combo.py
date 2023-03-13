#Q.1

# Foi feita uma função para receber um parametro de uma lista de inteiros e dentro foi declarado uma nova lista chamada pares.
def somadepares(inteiros):
    pares = []
    
# Foi feito um laço de repetição em que percorreu a lista de inteiros e dividiu todos por 2 e somente os resultados de resto 0 foram
# adicionados na lista de pares.
# Foi realizada uma verificação na lista para que caso a lista de pares não contenha nenhum número após o laço de repetição seja 
# informado ao usuario que a lista não contém números pares.   
    for i in inteiros:
        if i%2==0:
            pares.append(i)
    if pares == []:
        print('A lista não contém nenhum número par!')

# Foi criada uma nova variavel para que fosse feita a soma de todos os termos da lista de pares e então foi utilizado o return com 
# o valor da soma.
    soma_dos_pares = sum(pares)
    return soma_dos_pares

# Foi feita uma nova variavel em que foi utilizado um laço de repetição para que o usuario delegue uma lista de números inteiros.
listainteiros = []

# Opcional: Abaixo criei uma variavel para receber do usuario a quantidade de termos que ele deseja que a lista de inteiros tenha.
rangedalista = int(input('Digite a quantidade de termos da sua lista: '))

# Original: No range do laço de repetição poderia ser apenas colocado um valor que gostariamos que a ista tivesse. (exp. 10)
for i in range(rangedalista):
    listainteiros.append(int(input('Digite uma lista de números inteiros: ')))

# Foi realizado o print chamando a função utilizado a variavel que o usuario inseriu a sua lista de números inteiros.
#print(somadepares(listainteiros))

#Q.2

def palindromo(palavra):
    invertida = palavra[::-1]

    if palavra == invertida:
        print('Esta palavra é um Palíndromo!')
    else:
        print('Esta palavra não é um Palíndromo!')


while True:
    pala = str(input('Digite uma palavra(0 para sair): '))
    if pala == '0':
        break
    palindromo(pala)

#Q.3

def listastring(lista):
    contador = 0

    for i in lista:
        if len(i) > 5:
            contador += 1
    return contador

lista2 = ['ovo','victor','casa']


while True:
    print('Você gostaria de adicionar mais palavras a lista? [s ou n]')
    if input('> ') == 's':
        novalista = str(input('Digite a lista de novas palavras(0 para sair): '))
        lista2.append(novalista)
    else:
        break
    
print(listastring(lista2))



