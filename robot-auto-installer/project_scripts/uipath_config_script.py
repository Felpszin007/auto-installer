import pyautogui
import pygetwindow as gw
# import cv2

 

def find_and_click_by_image(image_path, confidence):
    # Espera um pouco para que você possa mudar para a janela desejada
    pyautogui.moveTo(x=10, y=10)
    pyautogui.sleep(5)
    

    # Tenta localizar a imagem na tela
    local = pyautogui.locateOnScreen(image_path, confidence=confidence)  # Ajuste a confiança conforme necessário
    
    if local is not None:
        # Se a imagem foi encontrada, obtém o center da imagem
        center_x, center_y = pyautogui.center(local)

        # Move o mouse para o center da imagem e clica
        pyautogui.moveTo(center_x, center_y, duration=0.5)  # Move suavemente para a posição
        pyautogui.click()  # Clica
        print(f"Clicou na imagem encontrada em ({center_x}, {center_y})")
    else:
        print("Imagem não encontrada na tela.")

def turn_to_the_window(window_name):
    
    # Encontrar a window
    windows = gw.getWindowsWithTitle(window_name)

    if windows:
        # Se a window foi encontrada, trazê-la para o primeiro plano
        window = windows[0]  # Pega a primeira window encontrada
        window.activate()  # Ativa a window
        print(f"A window '{window_name}' foi ativada.")
    else:
        print(f"Nenhuma window com o nome '{window_name}' foi encontrada.")
        pyautogui.hotkey('Win')
        pyautogui.typewrite('UiPath')
        pyautogui.sleep(3)
        pyautogui.hotkey('Enter')
        pyautogui.sleep(20)
        windows = gw.getWindowsWithTitle(window_name)
        if windows:
            # Se a window foi encontrada, trazê-la para o primeiro plano
            window = windows[0]  # Pega a primeira window encontrada
            window.activate()  # Ativa a window
            print(f"A window '{window_name}' foi ativada.")
def configure_uipath():
    
    main_confidence = 0.9
    pyautogui.sleep(20)
    turn_to_the_window("UiPath Studio")
    pyautogui.sleep(20)
    find_and_click_by_image("C:\\RPA\\Imagens\\mais_opcoes_button.png", main_confidence)
    find_and_click_by_image("C:\\RPA\\Imagens\\opcoes_autonomas_button.png", main_confidence)
    find_and_click_by_image("C:\\RPA\\Imagens\\community_offline_button.png", main_confidence)
    find_and_click_by_image("C:\\RPA\\Imagens\\uipath_studio_option_button.png", main_confidence)
    pyautogui.sleep(20) 
    find_and_click_by_image("C:\\RPA\\Imagens\\close_button.png",0.9)
    find_and_click_by_image("C:\\RPA\\Imagens\\definicoes_sidebar_button.png",main_confidence)
    find_and_click_by_image("C:\\RPA\\Imagens\\gerir_origens_button.png",main_confidence)
    find_and_click_by_image("C:\\RPA\\Imagens\\nugget_box.png",main_confidence)
    find_and_click_by_image("C:\\RPA\\Imagens\\ferramentas_sidebar_button.png",main_confidence)
    find_and_click_by_image("C:\\RPA\\Imagens\\install_chrome_extension_button.png",main_confidence)
    pyautogui.sleep(5)
    # find_and_click_by_image("C:\\RPA\\Imagens\\install_edge_extension_button.png",main_confidence)
    find_and_click_by_image("C:\\RPA\\Imagens\\ok_button.png",0.8)

configure_uipath()