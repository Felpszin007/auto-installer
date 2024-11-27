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




import os
import subprocess
import time
import shutil
# Define o caminho base
base_path = "C:\\RPA"
arquivos_path = os.path.join(base_path, "Arquivos")
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



# Caminho do instalador do UiPath
ui_path_installer = os.path.join(arquivos_path, "UiPathStudioSetup.exe")

# Verifica se o instalador existe
if not os.path.exists(ui_path_installer):
    print(f"Erro: O instalador não foi encontrado no caminho: {ui_path_installer}")
else:
    # Executa o instalador do UiPath
    process = subprocess.Popen(ui_path_installer)

    # Monitora a instalação
    while True:
        retcode = process.poll()  # Verifica se o processo ainda está em execução
        if retcode is not None:  # Se o retorno não for None, o processo terminou
            print("O instalador do UiPath foi executado. Agora verificando a conclusão da instalação...")
            break
        time.sleep(1)  # Aguarda um segundo antes de verificar novamente
        
    # Verifica se o arquivo app.exe foi instalado com sucesso
    ui_path_app_exe = os.path.join(os.getenv('LOCALAPPDATA'), "UiPath", "app.exe")
    if os.path.exists(ui_path_app_exe):
        print("A instalação do UiPath foi concluída com sucesso.")
    else:
        print("A instalação do UiPath não foi concluída ou falhou.")
