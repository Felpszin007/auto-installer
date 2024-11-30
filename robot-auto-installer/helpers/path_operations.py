import os




def create_directories():
    base_path = "C:\\RPA"
    arquivos_path = os.path.join(base_path, "Arquivos")
    projetos_path = os.path.join(base_path, "Projetos")
    imagens_path = os.path.join(base_path, "Imagens")
    # Cria as pastas "RPA", "Arquivos" e "Projetos"
    os.makedirs(arquivos_path, exist_ok=True)
    os.makedirs(projetos_path, exist_ok=True)
    os.makedirs(imagens_path, exist_ok=True)