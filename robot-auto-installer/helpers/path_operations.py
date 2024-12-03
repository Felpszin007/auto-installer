import os
import shutil



def create_directories():
    base_path = "C:\\RPA"
    arquivos_path = os.path.join(base_path, "Arquivos")
    projetos_path = os.path.join(base_path, "Projetos")
    imagens_path = os.path.join(base_path, "Imagens")
    # Cria as pastas "RPA", "Arquivos" e "Projetos"
    os.makedirs(arquivos_path, exist_ok=True)
    os.makedirs(projetos_path, exist_ok=True)
    os.makedirs(imagens_path, exist_ok=True)

def remove_directories():
    """Remove os diretórios especificados do sistema."""
    # Lista de diretórios a serem removidos
    directories_to_remove = [
        os.path.join(os.getenv('LOCALAPPDATA'), 'UiPath'),  # AppData\Local\UiPath
        os.path.join(os.getenv('APPDATA'), 'UiPath'),       # AppData\Roaming\UiPath
        os.path.join(os.getenv('PROGRAMDATA'), 'UiPath'),    # ProgramData\UiPath
        os.path.join(os.getenv('APPDATA'), 'NuGet'),    # ProgramData\UiPath
        os.path.join(os.getenv('LOCALAPPDATA'), 'NuGet'),    # ProgramData\UiPath

        r'C:\RPA'                                            # C:\RPA
    ]

    for directory in directories_to_remove:
        try:
            # Verifica se o diretório existe
            if os.path.exists(directory):
                shutil.rmtree(directory)  # Remove o diretório e todo o seu conteúdo
                print(f"Diretório '{directory}' e todo o seu conteúdo removidos com sucesso.")
            else:
                print(f"Diretório '{directory}' não encontrado.")
        except Exception as e:
            print(f"Erro ao remover diretório '{directory}': {e}")


    