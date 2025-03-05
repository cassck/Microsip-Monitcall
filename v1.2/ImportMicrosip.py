import os
import shutil

# Caminho de origem do arquivo Contacts.xml em L:\
caminho_origem = r'L:\\Contacts.xml'

# Caminho de destino para onde você deseja importar o arquivo
caminho_destino = os.path.expanduser(
    r'~\\AppData\\Roaming\\MicroSIP\\Contacts.xml')

# Verifique se o arquivo de origem em L:\ existe antes de importá-lo
if os.path.exists(caminho_origem):
    shutil.copy(caminho_origem, caminho_destino)
    print(
        f"O arquivo {caminho_origem} foi importado com sucesso para {caminho_destino}.")
else:
    print(f"O arquivo {caminho_origem} não existe em L:\\.")
