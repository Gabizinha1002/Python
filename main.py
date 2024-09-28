#o "def" cria uma função chamada menu e ali estão as opções que a pessoa pode escolher
def menu():
    print("Escolha uma opção:")
    print("1 Dizer olá")
    print("2 Somar dois números")
    print("3 Sair")

#Cria um loop
while True:

    menu() #Chama a função menu que foi criada
    user_opc = input("Digite o número da opção desejada: ") #Cria uma variável em que a pessoa pdoe fazer a sua escolha

#Cria para cada escolha, a resposta
    if user_opc == '1': # Se, a pessoa escolher a opção 1
        print("Olá, seja bem-vindo!")  
        # Exibe a mensagem de boas vindas a pessoa

    elif user_opc == '2':   #Senão, se a pessoa escolher a opção 2
        #Cria duas variáveis para guardar dois números para serem somados
        num1 = float(input("Digite o primeiro número: ")) #float serve para números decimais
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2   #Cria uma variável que some os dois números escolhidos
        print(f"A soma é: {soma}") #Exibe o resultado

    elif user_opc == '3':    #Senão, se a pessoa escolher a opção 3
        print("Saindo... Até mais!")#Exibe a mensagem de saída
        break #Termina

    else:#Caso a pessoa digite qualquer outra coisa que não seja 1, 2 ou 3
        print("Essa opção não existe")#Exibe a mensagem que a opção não existe
