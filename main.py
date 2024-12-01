"""
Exigências: 
    
    - O .zip deve estar localizado no disco "C:\"
    - O .zip com o script conterá os seguintes arquivos:

        1. "UiPathStudio.exe" (instalador do UiPath)
        2. "atualiza bat e versao"
        3. Última atualização do robô disponível  (No momento em que escrevo isso é a "WhatsApp.2.2.144.nupkg")
        4. "Whatsapp.bat" 
        5. "app.exe" (Última versão disponível do curupira)

        

Passo-a-passo(o que ele vai fazer)

      - criar a pasta "RPA" dentro do disco "C:\" 

      Já dentro da pasta "RPA", ele deve criar as pastas "Arquivos" e "Projetos"

      Dentro da pasta "Projetos", ele colocará os arquivos:

        - "app.exe", "Whatsapp.bat", "WhatsApp.2.2.XXX", "atualiza bat e versao.exe"
      
      Dentro da pasta "Arquivos", ele colocará o arquivo:
        
        - "UiPathStudio.exe" 

        Com tudo isso já feito, ele irá rodar o arquivo  "UiPathStudio.exe",
      e de alguma forma monitorar a instalação pra saber quando ela terminou
              






"""

# import os
# import shutil
# import subprocess
# import time

# # Define o caminho base
# base_path = "C:\\RPA"
# arquivos_path = os.path.join(base_path, "Arquivos")
# projetos_path = os.path.join(base_path, "Projetos")

# # Cria as pastas "RPA", "Arquivos" e "Projetos"
# os.makedirs(arquivos_path, exist_ok=True)
# os.makedirs(projetos_path, exist_ok=True)

# # Define os arquivos que devem ser movidos
# files_to_move = [
#     "C:\\UiPathStudioSetup.exe",
#     "C:\\atualiza bat e versao.exe",
#     "C:\\WhatsApp.2.2.144.nupkg",
#     "C:\\app.exe"
# ]



# # Executa o instalador do UiPath
# ui_path_installer = os.path.join(arquivos_path, "UiPathStudioSetup.exe")
# process = subprocess.Popen(ui_path_installer)

# # Monitora a instalação
# while True:
#     retcode = process.poll()  # Verifica se o processo ainda está em execução
#     if retcode is not None:  # Se o retorno não for None, o processo terminou
#         print("A instalação do UiPath foi concluída.")
#         break
#     time.sleep(1)  # Aguarda um segundo antes de verificar novamente


# import os
# import subprocess
# import time
import pygetwindow as gw
from helpers.path_operations import create_directories
from helpers.file_operations import move_zip_files
from project_scripts.exe_runner import  install_uipath
from helpers.file_operations import move_uipath_files
from project_scripts.uipath_config_script import configure_uipath


def main():
    create_directories()
    move_zip_files()
    install_uipath()
    move_uipath_files()
    configure_uipath()

if __name__ == "__main__":
    main()
    
