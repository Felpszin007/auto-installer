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
#     "C:\\Whatsapp.bat",
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



import pygetwindow as gw
import os
import subprocess
import time
import shutil
# Define o caminho base
base_path = "C:\\RPA"
arquivos_path = os.path.join(base_path, "Arquivos")
def move_files():
    projetos_path = os.path.join(base_path, "Projetos")

    # Cria as pastas "RPA", "Arquivos" e "Projetos"
    os.makedirs(arquivos_path, exist_ok=True)
    os.makedirs(projetos_path, exist_ok=True)

    print('Os diretórios foram criados!')
    # Move os arquivos para as pastas corretas
    shutil.move("C:\\UiPathStudioSetup.exe", arquivos_path)
    shutil.move("C:\\atualiza bat e versao.exe", projetos_path)
    shutil.move("C:\\WhatsApp.2.2.144.nupkg", projetos_path)
    shutil.move("C:\\Whatsapp.bat", projetos_path)
    shutil.move("C:\\app.exe", projetos_path)

def install_ui_path():
    # Caminho do instalador do UiPath
    ui_path_installer = os.path.join(arquivos_path, "UiPathStudioSetup.exe")

    # Verifica se o instalador existe
    # Verifica se o instalador existe
    if not os.path.exists(ui_path_installer):
        print(f"Erro: O instalador não foi encontrado no caminho: {ui_path_installer}")
    else:
        try:
            # Muda o diretório de trabalho para a pasta "Arquivos" e executa o instalador do UiPath
            print(f"Executando o instalador: {ui_path_installer}")
            subprocess.Popen(ui_path_installer, cwd=arquivos_path, shell=True)

            # Aguarda a janela "UiPath Studio" ou "UiPathStudioSetup.exe" aparecer
            
            while True:
                time.sleep(1)  # Aguarda 1 segundo antes de verificar novamente
                success_window = gw.getWindowsWithTitle("UiPath Studio")
                error_window = gw.getWindowsWithTitle("UiPathStudioSetup.exe")
                installing_window = gw.getWindowsWithTitle("Installing...")
                if success_window:
                    print("A instalação do UiPath foi concluída e a janela 'UiPath Studio' está aberta.")
                    break
                elif error_window:
                    print("A instalação do UiPath falhou e a janela 'UiPathStudioSetup.exe' está aberta.")
                    break
                elif installing_window:
                    print("Installing...")

        except Exception as e:
            print(f"Ocorreu um erro ao tentar executar o instalador: {e}")

            