from selenium.webdriver.support.ui import Select

def preenche_selects(elementos_select):
    
    try:
        # Iterar sobre os elementos <select>
        for select_element in elementos_select:
            # Criar um objeto Select para manipular as opções
            print(select_element)
            select = Select(select_element)
            time.sleep(2)
            # Selecionar a opção "Yes" para cada <select>
            select.select_by_visible_text('Yes')
              
    except Exception as e:
        print(f"Erro ao preencher selects: {e}")
 