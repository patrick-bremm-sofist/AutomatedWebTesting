from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura o ChromeDriver Manager
service = Service(ChromeDriverManager().install())

# Inicia uma nova sessão do navegador
driver = webdriver.Chrome(service=service)

try:
    # Abre o Google
    driver.get("https://www.google.com")

    # Encontra o campo de busca
    search_box = driver.find_element("name", "q")

    # Digita a consulta de busca e envia
    search_query = "Python Selenium example"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Aguarda os resultados carregarem
    time.sleep(2)

    # Captura os resultados da busca
    results = driver.find_elements("css selector", "h3")
    for index, result in enumerate(results):
        print(f"{index + 1}. {result.text}")

finally:
    # Fecha o navegador
    driver.quit()
