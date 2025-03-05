import pyautogui
import time
import pandas

# tabela vai importar o arquivo com base no local onde o arquivo está
tabela = pandas.read_csv(
    r"C:\Users\erick.pereira\Downloads\Listas de Ramais.csv")

# vai renomear as colunas que serão lidas pelo microsip
tabela.rename(
    columns={'Nome': 'Name', 'Ramal': 'Number', 'Departamento': 'Info'},
    inplace=True
)
# excluir as colunas irrelevantes
tabela = tabela.drop(columns=["#", "Tipo", "LOF", "LOC", "DDF", "DDC", "DDI",
                     "SRV", "Endereço", "NAT", "Gerenciar", "Último Uso", "Latência (ms)"])

# colocar as colunas em ordem
ordem_colunas = ['Name', 'Number', 'Info']
tabela = tabela.reindex(columns=ordem_colunas)

# exportar o arquivo para o diretorio listado
tabela.to_csv(
    r'\\192.168.1.36\Publico\Contacts.csv', index=False)
