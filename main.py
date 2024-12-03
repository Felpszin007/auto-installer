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
    
