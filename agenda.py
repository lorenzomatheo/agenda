#Solicitação de dados da pessoa 
nome = input("Insira seu nome: ")
telefone = input("Telefone: ")
email = input("Email: ")

#Lista de contatos
contatos = []

#Função pra imprimir contatos adicionados
def visualizarListadeContatos():
    print(contatos)

#Função para salvar o contato que ela acabou de digitar 
def salvarContato():
    contatos.append(nome)
    contatos.append(telefone)
    contatos.append(email)

#função de favoritar contato
def favoritarContato():
    solicitação_favorito = input("Certeza que deseja favoritar esse contato? 'S' ou 'N': ") 
    #Colocando a resposta do usuario tudo em minúsculo
    favorito = solicitação_favorito.upper() 
    #Verificando se o usuário colocou sim ou não
    if(favorito == 'S'):
        print('S')
    elif(favorito == 'N'):
        print("\nNome: " + nome)
        print("Telefone: " + telefone)
        print("Email: " + email)  
    else:
        print("\nNome: " + nome)
        print("Telefone: " + telefone)
        print("Email: " + email)

#função para encerrar o ciclo
def encerrarAgenda():
    break






def dicionarioFuncoes(opcao):
    opcoes = {
        1: visualizarListadeContatos,
        2: salvarContato,
        3: favoritarContato,
        4: encerrarAgenda
    }
    opcoes[opcao]()

while True:
    opcao = int(input("\nEscolha uma opção (1 - Visualizar Lista de Contatos, 2 - Salvar Contato, 3 - Favoritar Contato, 4 - Encerrar Agenda): " ))
    if opcao == 1:
        print("1 - Visualizar Lista de Contatos")
        dicionarioFuncoes(opcao)
    elif opcao == 2:
        print("2 - Salvar Contato")
        dicionarioFuncoes(opcao)
    elif opcao == 3:
        print("3 - Favoritar Contato")
        dicionarioFuncoes(opcao)
    elif opcao == 4:
        print("4 - Encerrar Agenda")
        dicionarioFuncoes(opcao)
        break
    else:
        print("Opção inválida. Por favor, insira um número válido.")



