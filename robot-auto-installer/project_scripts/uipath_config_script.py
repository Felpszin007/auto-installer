import pyautogui
import pygetwindow as gw

def find_and_click_by_image(image_path):
    # Espera um pouco para que você possa mudar para a janela desejada
    pyautogui.moveTo(x=10, y=10)
    pyautogui.sleep(3)
    
    # Tenta localizar a imagem na tela
    local = pyautogui.locateOnScreen(image_path,)  # Ajuste a confiança conforme necessário

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
    """
    Ativa uma window pelo nome.

    :param window_name: O nome da window que você deseja ativar.
    """
    # Encontrar a window
    windows = gw.getWindowsWithTitle(window_name)

    if windows:
        # Se a window foi encontrada, trazê-la para o primeiro plano
        window = windows[0]  # Pega a primeira window encontrada
        window.activate()  # Ativa a window
        print(f"A window '{window_name}' foi ativada.")
    else:
        print(f"Nenhuma window com o nome '{window_name}' foi encontrada.")

def configure_uipath():
    
    turn_to_the_window("UiPath Studio")
    find_and_click_by_image("C:\\RPA\\Imagens\\mais_opcoes_button.png")
    find_and_click_by_image("C:\\RPA\\Imagens\\opcoes_autonomas_button.png")
    find_and_click_by_image("C:\\RPA\\Imagens\\community_offline_button.png")
configure_uipath()        