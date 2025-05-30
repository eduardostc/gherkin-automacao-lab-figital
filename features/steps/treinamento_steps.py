from behave import given, when, then
from features.pages.treinamento_page import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

########################## 1- Cenário: Redirecionamento para a tela inicial ao clicar em "Voltar" - Formulário Rede de Transformação Digital######################################
@given(u'o usuário está na tela do formulário da Rede de Transformação Digital')
def acessar_tela_formulario_rede_transformacao(context):
    acessar_pagina_inicial_aplicacao()
    acessar_pagina_formulario_rede_transformacao()
    time.sleep(3)


@when(u'ele clica no botão "Voltar"')
def clicar_botao_voltar_formulario(context):
    clicar_no_botao_voltar_do_formulario_rede_transformacao()
    time.sleep(3)


@then(u'o sistema deve redirecionar para a página inicial')
def validar_redirecionamento_pagina_inicial(context):
    wait = WebDriverWait(get_driver(), 10)
    wait.until(EC.url_to_be("https://laboratoriofigital.recife.pe.gov.br/"))
    assert get_driver().current_url == "https://laboratoriofigital.recife.pe.gov.br/"

########################## 2- Cenário: Validação no formato de e-mail invalido ######################################
@when(u'o usuário está no formulário')
def step_acessar_tela_formulario_rede_transformacao(context):
    acessar_pagina_inicial_aplicacao()
    acessar_pagina_formulario_rede_transformacao()
    time.sleep(3)


@when(u'ele preenche o campo e-mail com "cers.rodrigues"')
def preencher_email_invalido(context):
    preencher_campos()
    time.sleep(3)
    

@when(u'clica em "Enviar"')
def clicar_em_enviar(context):
    clicar_no_botao_enviar_do_formulario_rede_transformacao()
    time.sleep(3)


@then(u'o sistema deve exibir uma mensagem de "E-mail inválido"')
def validar_mensagem_email_invalido(context):
    mensagem_erro = obter_mensagem_erro_email()
    assert "Inclua um \"@\"" in mensagem_erro or "@" in mensagem_erro, f"Mensagem de erro não encontrada: {mensagem_erro}"

########################## 3- Cenário: Verificar se há proteção contra ataques XSS.######################################

@given(u'o usuário acessa a tela de login')
def acessar_tela_de_login(context):
    acessar_pagina_inicial_aplicacao()
    acessar_tela_login()

@when(u'ele preenche o campo de usuário com "<script>alert(\'XSS\')</script>"')
def preencher_usuario_com_script_xss(context):
    preencher_campo_login_com_xss()
    time.sleep(3)

@when(u'insere uma senha qualquer')
def preencher_senha_qualquer(context):
    preencher_campo_senha("senha_teste")
    time.sleep(3)

@when(u'clica em "Entrar"')
def clicar_botao_entrar(context):
    clicar_no_botao_entrar()
    time.sleep(3)

@then(u'o sistema não deve executar nenhum script malicioso')
def validar_ausencia_execucao_script_malicioso(context):
    assert "login" in get_driver().current_url or get_driver().title.lower().find("login") != -1 # Verificar se estar na página de login

    valor_campo = get_driver().find_element(By.CSS_SELECTOR, CAMPO_LOGIN_EMAIL).get_attribute("value") # Verificar que o campo de usuário contém o texto injetado
    assert "<script>alert('XSS')</script>" in valor_campo
    