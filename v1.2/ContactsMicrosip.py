import os
import pandas as pd


def main():
    # Obter o diretório de downloads padrão independente do nome de usuário
    downloads_dir = os.path.expanduser("~/Downloads")

    # Caminho completo para o arquivo desejado
    caminho_arquivo = os.path.join(downloads_dir, "Listas de Ramais.csv")

    if not os.path.exists(caminho_arquivo):
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return  # Encerre o programa se o arquivo não for encontrado

    # Continua com o processamento se o arquivo foi encontrado
    tabela = pd.read_csv(caminho_arquivo)

    # Mapear as colunas para os nomes desejados
    coluna_mapping = {
        'Nome': 'Name',          # Renomeia a coluna 'Nome' para 'Name'
        'Ramal': 'Number',      # Renomeia a coluna 'Ramal' para 'Number'
        'Departamento': 'Info'  # Renomeia a coluna 'Departamento' para 'Info'
    }
    tabela.rename(columns=coluna_mapping, inplace=True)

    # Excluir colunas irrelevantes
    colunas_irrelevantes = [
        "#", "Tipo", "LOF", "LOC", "DDF", "DDC", "DDI",
        "SRV", "Endereço", "NAT", "Gerenciar", "Último Uso", "Latência (ms)"
    ]
    tabela = tabela.drop(columns=colunas_irrelevantes)

    # Reorganizar as colunas
    ordem_colunas = ['Name', 'Number', 'Info']
    tabela = tabela.reindex(columns=ordem_colunas)

    caminho_destino_csv = r'L:\Contacts.csv'
    tabela.to_csv(caminho_destino_csv, index=False)

    print(f"O arquivo foi exportado com sucesso para {caminho_destino_csv}.")


if __name__ == "__main__":
    main()
