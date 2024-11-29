import pyautogui


def configure_uipath():
    botao = pyautogui.locateOnScreen("uipath_logo.png")

    if botao is not None:
    # Obtém o centro do botão
        centro_botao = pyautogui.center(botao)

        # Move o mouse para o centro do botão e clica
        pyautogui.moveTo(centro_botao)
        pyautogui.click()
        print("Botão clicado!")
    else:
        print("Botão não encontrado na tela.")