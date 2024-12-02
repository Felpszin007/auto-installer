import os
import subprocess
import time
import pygetwindow as gw

def install_uipath():
    base_path = "C:\\RPA"
    arquivos_path = os.path.join(base_path, "Arquivos")
    # Caminho do instalador do UiPath
    ui_path_installer = os.path.join(arquivos_path, "UiPathStudioSetup.exe")

    # Verifica se o instalador existe
    if not os.path.exists(ui_path_installer):
        print(f"Erro: O instalador não foi encontrado no caminho: {ui_path_installer}")
        return  # Adiciona um retorno para evitar continuar se o instalador não existir

    try:
        # Muda o diretório de trabalho para a pasta "Arquivos" e executa o instalador do UiPath
        print(f"Executando o instalador: {ui_path_installer}")
        result = subprocess.run([ui_path_installer], cwd=arquivos_path, shell=True)

        # Verifica o código de saída do instalador
        if result.returncode == 0:
            print("Instalação concluída com sucesso.")
        else:
            print(f"Instalação falhou com código de saída: {result.returncode}")
            return  # Se a instalação falhou, não continue

        # Aguarda um pouco para garantir que a janela tenha tempo de abrir
        time.sleep(5)

        # Verifica se a janela "UiPath Studio" está aberta
        for _ in range(10):  # Tenta verificar várias vezes
            success_window = gw.getWindowsWithTitle("UiPath Studio")
            if success_window:
                print("A instalação do UiPath foi concluída e a janela 'UiPath Studio' está aberta.")
                break
            time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente
        else:
            print("A instalação do UiPath foi concluída, mas a janela 'UiPath Studio' não foi encontrada.")

    except Exception as e:
        print(f"Ocorreu um erro ao tentar executar o instalador: {e}")

# Chame a função para testar
install_uipath()


        