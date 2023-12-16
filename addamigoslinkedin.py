from navegador.browser import browser
from selenium.webdriver.common.by import By
import time
from dados.linkedin_dados import info_login_teste, urls

instance = browser()  

def faca_login_linkedin():
    url = urls.get('urlbaselinkedin')
    instance.open_window_maximized(url)
    
    input_email = '//*[@id="session_key"]'
    elemento_email = instance.driver.find_element(By.XPATH, input_email)
    elemento_email.send_keys(info_login_teste['user'])
    
    input_senha = '//*[@id="session_password"]'
    elemento_senha = instance.driver.find_element(By.XPATH, input_senha)
    elemento_senha.send_keys(info_login_teste['senha'])

    botao = '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button'
    botao_login = instance.driver.find_element(By.XPATH, botao)
    botao_login.click()
    time.sleep(10)
    
def add_amigos():
    print('Adicionando amigos')
    urlfriends = urls.get('urlfriends')
    instance.driver.get(urlfriends)
    
    contador = 0
    time.sleep(10)
    
    try:
        while(contador < 100):
            contador = +1
            
            # Selecionando todos os botões de seguir amigos
            buttons = instance.driver.find_elements(By.XPATH, '//button[contains(@aria-label, "connect")]')
            
            if len(buttons) == 0:
                buttons = instance.driver.find_elements(By.XPATH, '//button[contains(@aria-label, "conectar")]')
            
            print(f'buttons: {buttons}')
                
            # Iterando sobre os botões encontrados
            for button in buttons:
                # Fazendo alguma ação com cada botão, como clicar nele
                button.click() 
                time.sleep(4)
            
            print('Terminou os contatos da página!')
            print('Aguardando próximos comandos...')
            
            instance.driver.refresh()
            
            print('página atualizada, seguindo novos amigos...')
            time.sleep(10)
                
    except Exception as e:
        print(f'Erro {e}')

try:
    faca_login_linkedin()
    
    add_amigos()
    
except Exception as e:
    print(f"Erro: {e}")

finally:
    # Fechar o navegador
    instance.driver.quit()
