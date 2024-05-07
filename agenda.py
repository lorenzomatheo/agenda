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
    contato = {"Nome ": nome, "Telefone ": telefone, "Email ": email}
    contatos.append(contato)
    #é uma bidimensional??

#função de favoritar contato
def favoritarContato():
    solicitação_favorito = input("Certeza que deseja favoritar esse contato? 'S' ou 'N': ") 
    # Colocando a resposta do usuário tudo em maiúsculo
    favorito = solicitação_favorito.upper() 
    # Verificando se o usuário colocou sim ou não
    if(favorito == 'S' and len(contatos) > 0):
        estrela = '⭐'
        contatos.append(estrela)
        print(contatos)
    elif(favorito == 'N' and len(contatos) > 0):
        print(contatos)
    else:
        print("Ou você é um pateta que esqueceu de salvar ou digitou errado")

def deletarContato():




def dicionarioFuncoes(opcao):
    opcoes = {
        1: visualizarListadeContatos,
        2: salvarContato,
        3: favoritarContato,
        4: deletarContato

    }
    opcoes[opcao]()

while True:
    opcao = int(input("\nEscolha uma opção (1 - Visualizar Lista de Contatos, 2 - Salvar Contato, 3 - Favoritar Contato, 4 - Deletar Contato, 5 - Encerrar Agenda): " ))
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
        print("4 - Deletar Contato")
        dicionarioFuncoes(opcao)
    elif opcao == 5:
        print("5 - Encerrar Agenda")
        break
    else:
        print("Opção inválida. Por favor, insira um número válido.")



