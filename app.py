import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário
pyautogui.click(968,541, duration=0.5)
pyautogui.write('jhonathan')
# 2 - Clicar e digitar minha senha
pyautogui.click(976,574, duration=0.5)
pyautogui.write('123456')
# 3 - Clicar em "Entrar"
pyautogui.click(845,605, duration=0.5)
# 4 - Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0].strip()
        quantidade = linha.split(',')[1].strip()
        preco = linha.split(',')[2].strip()
        # 1 - clicar e digitar produto
        pyautogui.click(627,525, duration=0.5)
        pyautogui.write(produto)
        # 2 - clicar e digitar quantidade
        pyautogui.click(635,560, duration=0.5)
        pyautogui.write(quantidade)
        # 3 - clicar e digitar preço
        pyautogui.click(637,595, duration=0.5)
        pyautogui.write(preco)
        # 4 - Clicar em "Registrar"
        pyautogui.click(500,784, duration=0.5)
        sleep(0.75)  # Esperar o registro ser processado
