import os
import shutil

def main():
    # Caminho de origem do arquivo Contacts.xml em L:\
    caminho_origem = r'L:\\MicroSip\\Contacts.xml'

    # Caminho de destino para onde você deseja importar o arquivo
    caminho_destino = os.path.expanduser(
        r'~\\AppData\\Roaming\\MicroSIP\\Contacts.xml')

    # Verifica se o arquivo de origem em L:\ existe antes de importá-lo
    if os.path.exists(caminho_origem):
        try:
            shutil.copy(caminho_origem, caminho_destino)
            print(
                f"O arquivo {caminho_origem} foi importado com sucesso para {caminho_destino}.")
        except Exception as e:
            print(f"Erro ao copiar o arquivo: {e}")
    else:
        print(f"O arquivo {caminho_origem} não existe em L:\\.")

if __name__ == "__main__":
    main()
