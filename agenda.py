#Solicitação de dados da pessoa 
nome = input("Insira seu nome: ")
telefone = int(input("Telefone: "))
email = input("Email: ")
favorito = ''

#Lista de contatos
contatos = []

#Função para salvar o contato que ela acabou de digitar 
def salvarContato():
    contato = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": favorito}
    contatos.append(contato)
    print("Contato salvo com sucesso!")

def editarContato():
    nome_editar = input("Digite o contato que deseja editar:")
    for contato in contatos:
        if(nome_editar == contato["Nome"]):
            opcao = int(input("Digite o que você deseja editar do contato:(1 - Nome, 2 - Telefone, 3 - Email, 4 - Favoritar/Desfavoritar Contato)"))
            while True:
                if opcao == 1:
                    novo_nome = input("Digite o novo nome para esse contato:")
                    contato["Nome"] = novo_nome
                    opcao_edicao = input("Deseja editar outro campo do mesmo contato? (S/N): ").upper()
                    if opcao_edicao == 'S':
                        editarContato()
                    elif opcao_edicao == 'N':    
                        break
                    else:
                        print("Opção de editar inválida")
                        break
                elif opcao == 2:
                    novo_telefone = input("Digite o novo telefone para esse contato:")
                    contato["Telefone"] = novo_telefone
                    opcao_edicao = input("Deseja editar outro campo do mesmo contato? (S/N): ").upper()
                    if opcao_edicao == 'S':
                        editarContato()
                    elif opcao_edicao == 'N':    
                        break
                    else:
                        print("Opção de editar inválida")
                        break
                elif opcao == 3:
                    novo_email = input("Digite o novo email para esse contato:")
                    contato["Email"] = novo_email
                    opcao_edicao = input("Deseja editar outro campo do mesmo contato? (S/N): ").upper()
                    if opcao_edicao == 'S':
                        editarContato()
                    elif opcao_edicao == 'N':    
                        break
                    else:
                        print("Opção de editar inválida")
                        break
                elif opcao == 4:
                        novo_favorito = input("Você deseja favoritar esse contato? (S/N): ").upper()
                        if novo_favorito == 'S':
                            contato["Favorito"] = '⭐'
                        elif novo_favorito == 'N':
                            pass
                        else:
                            print("Opção inválida. Pulando para o próximo contato.")
                            continue  # Pule para a próxima iteração se a entrada for inválida

                        if contato["Favorito"] == '⭐':
                            novo_desfavorito = input("Você deseja desfavoritar esse contato? (S/N): ").upper()
                            if novo_desfavorito == 'S':
                                contato["Favorito"] = None
                                print(contato)
                            elif novo_desfavorito == 'N':
                                pass
                                print(contato)  # Não faz nada, mantém o valor atual
                            else:
                                print("Opção inválida. Pulando para o próximo contato.")
                            opcao_edicao = input("Deseja editar outro campo do mesmo contato? (S/N): ").upper()
                            if opcao_edicao == 'S':
                                editarContato()
                            elif opcao_edicao == 'N':    
                                break
                            else:
                                print("Opção de editar inválida")
                                break
                       
        

                
                else:
                    print("Opção Inválida")
                    
        else:
            print("Contato inválido")




#função de deletar contato
def deletarContato():
    nome_aexcluir = input("Escreva o contato que você deseja excluir: ")
    for contato in contatos:
        if(contato["Nome"] == nome_aexcluir):
            contatos.remove(contato)
            print("Usuário excluido")
            break


#função de favoritar contato
def favoritarContato():
    solicitação_favorito = input("Certeza que deseja favoritar esse contato? 'S' ou 'N': ")
    
    # Colocando a resposta do usuário tudo em maiúsculo
    favorito = solicitação_favorito.upper()
    
    # Verificando se o usuário colocou sim ou não
    if(favorito == 'S'and len(contatos) > 0):
        contatos[-1]["Favorito"] = '⭐'  # Marca o último contato como favorito
        print(contatos)
    elif(favorito == 'N' and len(contatos) > 0):
        print(contatos)
    else:
        print("Ou você é um pateta que esqueceu de salvar ou digitou errado")

#Função pra imprimir contatos adicionados
def visualizarListadeContatos():
    print(contatos)

#Função pra imprimir contatos favoritados
def visualizarListadeContatosFavoritados():
    for contato in contatos:
        if(contato["Favorito"] == '⭐'):
            print(contato)
        elif(contato["Favorito"] != '⭐'):
            pass
        else:
            ("Não existe essa opção!")
            break
#Função para adicionar novo contato
def adicionarNovoContato():
    nome_novocontato = input("Insira o nome: ")
    telefone_novocontato = input("Telefone: ")
    email_novocontato = input("Email: ") 
    contato = {"Nome": nome_novocontato, "Telefone": telefone_novocontato, "Email": email_novocontato}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

def dicionarioFuncoes(opcao):
    opcoes = {
        1: visualizarListadeContatos,
        2: visualizarListadeContatosFavoritados,
        3: adicionarNovoContato,
        4: salvarContato,
        5: editarContato,
        6: favoritarContato,
        7: deletarContato
    }
    # puxar número selecionado no input opcao
    opcoes[opcao]() #??

while True:
    opcao = int(input("\nEscolha uma opção (1 - Visualizar Lista de Contatos, 2 - Visualizar Lista de Contatos Favoritados, 3 - Adicionar Novo Contato,  4 - Salvar Contato, 5 - Editar Contato, 6 - Favoritar Contato, 7 - Deletar Contato, 8 - Encerrar Agenda): " ))
    if opcao == 1:
        print("1 - Visualizar Lista de Contatos")
        dicionarioFuncoes(opcao)
    elif opcao == 2:
        print("2 - Visualizar Lista de Contatos Favoritados")
        dicionarioFuncoes(opcao)
    elif opcao == 3:
        print("3 - Adicionar Novo Contato")
        dicionarioFuncoes(opcao)    
    elif opcao == 4:
        print("4 - Salvar Contato")
        dicionarioFuncoes(opcao)
    elif opcao == 5:
        print("5 - Editar Contato")
        dicionarioFuncoes(opcao)
    elif opcao == 6:
        print("6 - Favoritar Contato")
        dicionarioFuncoes(opcao)
    elif opcao == 7:
        print("7 - Deletar Contato")
        dicionarioFuncoes(opcao)
    elif opcao == 8:
        print("8 - Encerrar Agenda")
        break
    else:
        print("Opção inválida. Por favor, insira um número válido.")



