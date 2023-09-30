import xml.etree.ElementTree as ET


class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        return {"Nome": self.nome, "Telefone": self.telefone, "Email": self.email}


def inserir_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o endereço de e-mail: ")
    return Contato(nome, telefone, email)


def salvar_contatos_xml(contatos, arquivo_path):
    root = ET.Element("Contatos")
    for contato in contatos:
        contato_elem = ET.SubElement(root, "Contato")
        nome_elem = ET.SubElement(contato_elem, "Nome")
        nome_elem.text = contato.nome
        telefone_elem = ET.SubElement(contato_elem, "Telefone")
        telefone_elem.text = contato.telefone
        email_elem = ET.SubElement(contato_elem, "Email")
        email_elem.text = contato.email

    tree = ET.ElementTree(root)
    tree.write(arquivo_path)
    print(f"Contato(s) salvo(s) em XML com sucesso no arquivo {arquivo_path}!")


def ler_contatos_xml(arquivo_path):
    try:
        tree = ET.parse(arquivo_path)
        root = tree.getroot()
        contatos = []
        for contato_elem in root.findall("Contato"):
            nome = contato_elem.find("Nome").text
            telefone = contato_elem.find("Telefone").text
            email = contato_elem.find("Email").text
            contato = Contato(nome, telefone, email)
            contatos.append(contato)
        return contatos
    except FileNotFoundError:
        return []


def listar_contatos(contatos):
    for i, contato in enumerate(contatos, start=1):
        print(f"Contato {i}:")
        print(f"Nome: {contato.nome}")
        print(f"Telefone: {contato.telefone}")
        print(f"E-mail: {contato.email}")


def main():
    arquivo_path = "contatos.xml"
    contatos = ler_contatos_xml(arquivo_path)

    while True:
        opcao = input(
            "1 - Inserir um contato\n2 - listar contatos\n3 - para sair\n")

        if opcao == '1':
            contato = inserir_contato()
            contatos.append(contato)

        elif opcao == '2':
            listar_contatos(contatos)

        elif opcao == '3':
            salvar_contatos_xml(contatos, arquivo_path)
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
