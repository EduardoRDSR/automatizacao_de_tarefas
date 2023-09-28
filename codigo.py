import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

# entrar no navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# abrir o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# espera de carregamento
time.sleep(2)

# fazer login
pyautogui.press("tab")
pyautogui.write("eduardo@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

# espera de carregamento
time.sleep(2)

# importar base de dados
tabela = pandas.read_csv("produtos.csv")

# repetição de cadastro de produto
for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]

    # cadastrar produto
    pyautogui.click(x=819, y=273)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")


pyautogui.scroll(50000)