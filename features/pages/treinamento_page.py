from features.helpers.driver import get_driver
from features.pages.base_page import find_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page import *

##################### MAPEANDO CAMPOS NA TELA #####################################

#BOTAO_1_ESCALAO = ".btn-primary"
BOTAO_REDE_TRANSFORMACAO = ".btn-success"  #xpath = //a[text()='Rede de Transformação Digital']
BOTAO_VOLTAR = ".btn-secondary"
CAMPO_NOME = "#id_nome"
CAMPO_SECRETARIA = "#id_secretaria"
CAMPO_CARGO = "#id_cargo"
CAMPO_EMAIL = "#id_email"
CAMPO_LOGIN_EMAIL = "#email"
BOTAO_ENVIAR = "form button[type='submit']" #"body > div > div > div > div > form > button" #"button.btn.btn-primary" OU "form button[type='submit']"
#BOTAO_VOLTAR_ESCALAO = ".btn btn-secondary"
BOTAO_AREA_RESTRITA = ".btn-warning"
BOTAO_ENTRAR = "button.btn.btn-warning"
CAMPO_SENHA = "#password"

CAMPO_WHATSAPP = "#id_telefone"
CAMPO_PROBLEMA = "#id_problema_urgente"
BOTAO_CLICK_ME = "button.btn-primary.w-100"
MENSAGEM_SUCESSO_FORM = "div.alert.alert-success"
CAMPO_EMAILLOGIN = "#email"
BUTTON_LOG = "button.btn.btn-warning.w-100"
MENSAGEM_ERRO_LOGIN = "div.alert.alert-danger.text-center"
MENSAGEM_BOAS_VINDAS_CSS = "span.navbar-text"

################## VARIAVEIS PARA AJUDAR O TESTE #####################################################
texto_email = "cers"
texto_nome = "carlos"
texto_secretaria = "Seplag"
texto_cargo = "Desenvolvedor"
login = "xss"
#texto_senha = "123456"

################# METODOS do 1-cenário:Redirecionamento para a tela inicial ao clicar em "Voltar" - Formulário Rede de Transformação Digita ######################
def acessar_pagina_inicial_aplicacao():
    get_driver().get("https://laboratoriofigital.recife.pe.gov.br/")

def acessar_pagina_formulario_rede_transformacao():
    find_element(BOTAO_REDE_TRANSFORMACAO).click()

def clicar_no_botao_voltar_do_formulario_rede_transformacao():
    find_element(BOTAO_VOLTAR).click()

################# METODOS do 2- cenário: Validação no formato de e-mail invalido ######################
def preencher_campos():
    preencher_campo_nome()
    preencher_campo_secretaria()
    preencher_campo_cargo()
    preencher_campo_email()
# def clicar_no_botao_voltar_do_formulario_escalao():
#     find_element(BOTAO_VOLTAR_ESCALAO).click()

def preencher_campo_nome():
    find_element(CAMPO_NOME).send_keys(texto_nome)

def preencher_campo_secretaria():
    find_element(CAMPO_SECRETARIA).send_keys(texto_secretaria)

def preencher_campo_cargo():
    find_element(CAMPO_CARGO).send_keys(texto_cargo)

def preencher_campo_email():
    find_element(CAMPO_EMAIL).send_keys(texto_email)

def clicar_no_botao_enviar_do_formulario_rede_transformacao():
    find_element(BOTAO_ENVIAR).click()

def obter_mensagem_erro_email():
    driver = get_driver()
    input_email = driver.find_element(By.CSS_SELECTOR, CAMPO_EMAIL)  
    return driver.execute_script("return arguments[0].validationMessage;", input_email)

################# METODOS do 3- Verificar se há proteção contra ataques XSS. ######################
def acessar_tela_login():
    find_element(BOTAO_AREA_RESTRITA).click()

def preencher_campo_login_com_xss():
    campo_email = find_element(CAMPO_LOGIN_EMAIL)
    campo_email.clear()
    campo_email.send_keys("<script>alert('XSS')</script>")


def preencher_campo_senha(texto_senha):
    campo_senha = find_element(CAMPO_SENHA) 
    campo_senha.clear()
    campo_senha.send_keys(texto_senha)


def clicar_no_botao_entrar():
    botao_entrar = find_element(BOTAO_ENVIAR)
    botao_entrar.click()
############################
    ##########LUIZ
###########################
def get_campo_nome():
    return find_element(CAMPO_NOME)

def get_campo_secretaria():
    return find_element(CAMPO_SECRETARIA)

def get_campo_cargo():
    return find_element(CAMPO_CARGO)

def get_campo_email():
    return find_element(CAMPO_EMAIL)

def get_campo_whatsap():
    return find_element(CAMPO_WHATSAPP)

def get_campo_problema():
    return find_element(CAMPO_PROBLEMA)

def get_botao_click_me():
    return find_element(BOTAO_CLICK_ME)

def obter_mensagem_sucesso_formulario():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)
    mensagem_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, MENSAGEM_SUCESSO_FORM))
    )
    return mensagem_element.text.strip()

# ____________________________________________________________________________________
def get_campo_emaillogin():
    return find_element(CAMPO_EMAILLOGIN)

def get_campo_senha():
    return find_element(CAMPO_SENHA)

def get_button_login():
    find_element(BUTTON_LOG).click()

def obter_mensagem_erro_login_invalido():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)
    mensagem_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, MENSAGEM_ERRO_LOGIN))
    )
    return mensagem_element.text.strip()

#___________________________________________________________________________
def obter_texto_mensagem_boas_vindas():
    driver = get_driver()
    wait = WebDriverWait(driver, 10) # Espera até 10 segundos
    mensagem_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, MENSAGEM_BOAS_VINDAS_CSS))
    )
    return mensagem_element.text.strip() # .strip() remove espaços em branco extras


