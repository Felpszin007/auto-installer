import shutil
import os
import subprocess


base_path = "C:\\RPA"
arquivos_path = os.path.join(base_path, "Arquivos")
projetos_path = os.path.join(base_path, "Projetos")
imagens_path = os.path.join(base_path, "Imagens")


def move_zip_files():
    print('Os diretórios foram criados!')

    # Lista de arquivos a serem movidos
    files_to_move = {
        "C:\\app.exe": projetos_path,
        "C:\\atualiza bat e versao.exe":  projetos_path,
        "C:\\close_button.png":imagens_path,
        "C:\\community_offline_button.png":imagens_path,
        "C:\\definicoes_sidebar_button.png":imagens_path,
        "C:\\ferramentas_sidebar_button.png":imagens_path,
        "C:\\gerir_origens_button.png":imagens_path,
        "C:\\install_chrome_extension_button.png":imagens_path,
        "C:\\mais_opcoes_button.png":imagens_path,
        "C:\\nugget_box.png":imagens_path,
        "C:\\ok_button.png":imagens_path,
        "C:\\opcoes_autonomas_button.png":imagens_path,
        "C:\\uipath_studio_option_button.png":imagens_path,
        "C:\\UiPathStudioSetup.exe":arquivos_path,
        "C:\\Whatsapp.2.2.144.nupkg":projetos_path,

    }

    for src, dst in files_to_move.items():
        try:
            # Verifica se o arquivo existe antes de tentar mover
            if os.path.exists(src):
                shutil.move(src, dst)
                print(f"Arquivo movido: {src} -> {dst}")
            else:
                print(f"Arquivo não encontrado: {src}")
        except PermissionError as e:
            print(f"Erro de permissão ao mover o arquivo {src}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {src}: {e}")

import os
import shutil
import subprocess

def move_uipath_files():
    # Cria o caminho completo para o executável
    package_dir = "C:\\ProgramData\\UiPath\\Packages"
    files_mover_path = os.path.join(projetos_path, 'atualiza bat e versao.exe')
    
    try:
        # Executa o arquivo .exe
        subprocess.run([files_mover_path], check=True)
        print('Movendo os arquivos do robô..')
        print('Abrindo arquivo secundário')
        print('Arquivos movidos!')
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o executável: {e}")
    except FileNotFoundError:
        print("O arquivo executável não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # # Mover arquivos .nupkg
    # for file in os.listdir(projetos_path):
    #     if file.endswith(".nupkg"):
    #         full_file_path = os.path.join(projetos_path, file)
    #         if os.path.exists(full_file_path):
    #             shutil.move(full_file_path, package_dir)
    #             print(f"Arquivo {file} movido com sucesso.")
    #         else:
    #             print(f"O arquivo {full_file_path} não foi encontrado.")