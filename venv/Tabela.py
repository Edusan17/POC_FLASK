from selenium import webdriver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
        # chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        prefs = {"profile.default_content_settings.popups": 0,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True
    }
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(
            service=Service(r"caminhodowebdriver"),
            options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(5)

driver = webdriver.Chrome()
driver.get("https://www.vriconsulting.com.br/guias/guiasIndex.php?idGuia=22")

xpath_da_tabela = '//*[@id="corpoGuia"]/table[1]'
tabela = driver.find_element("xpath", xpath_da_tabela)

linhas = tabela.find_elements("tag name", "tr")
dados = []
for linha in linhas:
    colunas = linha.find_elements("tag name", "td")
    dados.append([coluna.text for coluna in colunas])

driver.quit()

print(dados)

df = pd.DataFrame(dados, columns=["N", "Campo", "Descrição", "Tipo", "Tam", "Dec", "Obrig"])
print(df)

df.to_sql("dados_da_tabela.sql", index=False)