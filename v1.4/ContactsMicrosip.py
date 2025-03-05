import os
import pandas as pd

def to_xml_no_indentation(df, root_name='root', row_name='row', attr_cols=None):
    xml = df.to_xml(index=False, root_name=root_name, row_name=row_name, attr_cols=attr_cols)
    xml_no_indentation = '\n'.join(line.strip() for line in xml.splitlines())
    return xml_no_indentation

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

    # Excluir colunas irrelevantes
    colunas_irrelevantes = [
        "#", "Tipo", "LOF", "LOC", "DDF", "DDC", "DDI",
        "SRV", "Endereço", "NAT", "Gerenciar", "Último REG", "Latência (ms)"
    ]
    tabela = tabela.drop(columns=colunas_irrelevantes)
    df = tabela

    # Rename columns to match the desired XML attributes
    df = df.rename(columns={'Nome': 'name', 'Ramal': 'number', 'Departamento': 'info'})

    # Add additional columns with empty strings for the attributes you need
    additional_columns = ['firstname', 'lastname', 'phone', 'mobile', 'email', 'address', 'city', 'state',
                           'zip', 'comment', 'id', 'presence', 'starred', 'directory']
    df = df.assign(**{col: '' for col in additional_columns})

    # Reorder columns to match the desired XML structure
    xml_columns_order = ['name', 'number'] + additional_columns + ['info']
    df = df[xml_columns_order]

    # Generate XML data
    xml_data_no_indentation = to_xml_no_indentation(df, root_name='contacts', row_name='contact', attr_cols=xml_columns_order)

    xml_save = r'L:\MicroSip\Contacts.xml'
    with open(xml_save, 'w', encoding='utf-8') as xml_save_file:
        xml_save_file.write(xml_data_no_indentation)

if __name__ == "__main__":
    main()
