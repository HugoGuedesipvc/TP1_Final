import xmlrpc.client
import time
if __name__ == "__main__":

    time.sleep(3)

    try:
        print("Conectando ao servidor...")
        server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

        csv_path = 'cars.csv'

        try:
            result = server.list_xml()
            if result:
                print("Lista de arquivos XML:")
                for item in result:
                    print(item)
            else:
                print("Nenhum arquivo XML encontrado.")
        except Exception as e:
            print(f"Erro ao listar arquivos XML: {e}")

        result=server.routinas_query(1)
        print(result)

        while True:
            print("\nMenu:")
            print("1. Enviar arquivo CSV")
            print("2. Eliminar arquivo XML")
            print("3. Executar consultas")
            print("4. Sair")

            choice = input("Escolha uma opção (1-8): ")

            if choice == '1':
                csv_name = input("Digite o nome do arquivo CSV: ")
                print("Ficheiro scv a ser processado...")
                with open(csv_path, 'rb') as csv_file:
                    csv_data = xmlrpc.client.Binary(csv_file.read())
                    server.save_csv_file(csv_name, csv_data)
                print("Ficheiro scv finalizado")

            elif choice == '2':
                try:
                    result = server.list_xml()
                    if result:
                        print("Lista de arquivos XML:")
                        for item in result:
                            print(item)
                    else:
                        print("Nenhum arquivo XML encontrado.")
                except Exception as e:
                    print(f"Erro ao listar arquivos XML: {e}")
                id_to_remove = input("Digite o ID do arquivo XML para remover: ")
                server.eliminar_xml(id_to_remove)

            elif choice == '3':

                print("1. Filtrar por país")
                print("2. Filtrar por ano")
                print("3. Pesquisar carros")
                print("4. Listar pessoas ordenadas por nome")
                print("5. Filtrar carros por marca")

                choice = input("Escolha uma opção (1-5): ")

                if '1' <= choice <= '5':
                    result=server.routinas_query(int(choice))
                    print(result)

            elif choice == '4':
                print("Saindo do programa.")
                break

            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Erro durante a execução do cliente: {e}")
