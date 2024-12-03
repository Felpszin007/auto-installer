from helpers.path_operations import create_directories
from helpers.path_operations import remove_directories

from helpers.file_operations import move_zip_files
from project_scripts.exe_runner import  install_uipath
from helpers.file_operations import move_uipath_files
from project_scripts.uipath_config_script import configure_uipath

def install_robot():
    create_directories()
    move_zip_files()
    install_uipath()
    move_uipath_files()
    # configure_uipath()

def uninstall_robot():
    print('Desinstalando robô...')
    remove_directories()    

def set_process():
   
        a = input("""
            Selecione o processo do robô:
            1 - Instalar robô
            2 - Desinstalar o robô
            
            """)
        if a == "1":
            install_robot()
        elif a == "2":
            uninstall_robot()
        
        


def main():
    set_process()

if __name__ == "__main__":
    main()
    
