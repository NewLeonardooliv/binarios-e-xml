import pickle


class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def salvar_contatos(self):
        with open("./contatos.bin", "wb") as arquivo:
            pickle.dump(self.contatos, arquivo)
        print("Contato(s) salvo(s) com sucesso!")


def main():
    agenda = Agenda()

    while True:
        opcao = input("1 - Inserir um contato\n2 - sair\n")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o número de telefone: ")
            email = input("Digite o endereço de e-mail: ")

            contato = Contato(nome, telefone, email)
            agenda.adicionar_contato(contato)
            agenda.salvar_contatos()

        elif opcao == '2':
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
