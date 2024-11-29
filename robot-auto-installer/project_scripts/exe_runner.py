import os
import subprocess
import time
import pygetwindow as gw

base_path = "C:\\RPA"
arquivos_path = os.path.join(base_path, "Arquivos")
projetos_path = os.path.join(base_path, "Projetos")

def install_uipath():
    # Caminho do instalador do UiPath
    ui_path_installer = os.path.join(arquivos_path, "UiPathStudioSetup.exe")

    # Verifica se o instalador existe
    if not os.path.exists(ui_path_installer):
        print(f"Erro: O instalador não foi encontrado no caminho: {ui_path_installer}")
        return  # Adiciona um retorno para evitar continuar se o instalador não existir

    try:
        # Muda o diretório de trabalho para a pasta "Arquivos" e executa o instalador do UiPath
        print(f"Executando o instalador: {ui_path_installer}")
        process = subprocess.Popen(ui_path_installer, cwd=arquivos_path, shell=True)

        # Aguarda a conclusão do processo do instalador
        process.wait()  # Isso bloqueia até que o processo termine

        # Após o processo terminar, verifique se a janela "UiPath Studio" está aberta
        time.sleep(2)  # Aguarda um pouco para garantir que a janela tenha tempo de abrir
        success_window = gw.getWindowsWithTitle("UiPath Studio")

        if success_window:
            print("A instalação do UiPath foi concluída e a janela 'UiPath Studio' está aberta.")
        else:
            print("A instalação do UiPath foi concluída, mas a janela 'UiPath Studio' não foi encontrada.")

    except Exception as e:
        print(f"Ocorreu um erro ao tentar executar o instalador: {e}")