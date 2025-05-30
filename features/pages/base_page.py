from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_element(locator):
    return get_driver().find_element(By.CSS_SELECTOR, locator) #Localiza um elemento na página usando um seletor CSS (locator).

# def find_element(locator, by=By.CSS_SELECTOR):
#     return get_driver().find_element(by, locator)

def get_element_text(locator):
    return find_element(locator).get_attribute("value") #Pega o texto (ou valor) do elemento localizado por um seletor CSS (locator).

def wait_for_element(locator, timeout):
    element = find_element(locator)
    return WebDriverWait(get_driver(), timeout).until(
        EC.presence_of_all_elements_located(element) #Espera até que todos os elementos correspondentes ao seletor CSS (locator) estejam presentes.
    )