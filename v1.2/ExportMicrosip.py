import os
import shutil

# Obtenha o caminho completo para o arquivo Contacts.xml
arquivo_a_copiar = os.path.expanduser(
    r'~\AppData\Roaming\MicroSIP\Contacts.xml')
caminho_destino = r'L:\Contacts.xml'

# Verifique se o arquivo a ser copiado existe antes de copiá-lo
if os.path.exists(arquivo_a_copiar):
    shutil.copy(arquivo_a_copiar, caminho_destino)
    print(
        f"O arquivo {arquivo_a_copiar} foi copiado com sucesso para {caminho_destino}.")

else:
    print(f"O arquivo {arquivo_a_copiar} não existe.")
