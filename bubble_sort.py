#lista de dicionários
lista_contatos = []

#função para deixar telefone no padrão (XX) XXXXX-XXXX
def formatar_numero(telefone):
    telefone = str(telefone) #transformar em string pra modificar
    telefone = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "") #tirar itens indesejados
    
    if len(telefone) == 11:
        telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}" #formatar no padrão
        return telefone_formatado
    else:
        return None

#função para adicionar contato a lista_contatos
def adicionar_contato(nome, telefone):
    telefone_formatado = formatar_numero(telefone)
    if telefone_formatado:
        lista_contatos.append({"nome": nome, "telefone": telefone_formatado})
        print(f"Contato de {nome} adicionado à lista com telefone {telefone_formatado}.")
    else:
        print("Número de telefone inválido. Certifique-se de inserir um número com 11 dígitos.")

#bubble sort para ordenar lista de contatos em ordem alfabética
def bubble_sort_contatos(contatos):
    n = len(contatos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if contatos[j]['nome'].lower() > contatos[j + 1]['nome'].lower():
                contatos[j], contatos[j + 1] = contatos[j + 1], contatos[j]

#exibe contatos em ordem
def exibir_contatos(contatos):
    if contatos:
        bubble_sort_contatos(contatos)
        print("Lista de contatos:")
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
    else:
        print("Nenhum contato salvo.")


#remove contato pelo nome
def remover_contato(nome):
    for contato in lista_contatos: #percorre cada item da lista e o adiciona na variável contato
        if contato['nome'].lower() == nome.lower(): #verifica se o contato é igual ao nome passado (.lower para ser case-sensitive)
            lista_contatos.remove(contato) #remove contato da lista
            print(f"Contato de {nome} removido da lista.")
            return
    print(f"Contato com nome {nome} não encontrado.")

#menu de interação com o usuário
def menu():
    while True:
        print('Menu de contatos:')
        print("1 - Adicionar contato")
        print("2 - Exibir lista de contatos")
        print("3 - Excluir contato")
        print("4 - Sair do sistema")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do contato: ")
            telefone = input("Telefone (somente números): ")
            adicionar_contato(nome, telefone)
        elif opcao == '2':
            exibir_contatos(lista_contatos)
        elif opcao == '3':
            nome = input("Nome do contato a ser removido: ")
            remover_contato(nome)
        elif opcao == '4':
            print("Encerrando")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
