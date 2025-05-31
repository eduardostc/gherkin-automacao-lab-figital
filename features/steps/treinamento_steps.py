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
    #assert False
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
    #assert False
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
    #assert False
    assert "login" in get_driver().current_url or get_driver().title.lower().find("login") != -1 # Verificar se estar na página de login

    valor_campo = get_driver().find_element(By.CSS_SELECTOR, CAMPO_LOGIN_EMAIL).get_attribute("value") # Verificar que o campo de usuário contém o texto injetado
    assert "<script>alert('XSS')</script>" in valor_campo


############################
    ##########LUIZ
###########################
from features.helpers.driver import get_driver

@given(u'que a página de formulário de 1º Escalão seja acessada')
def acessar_site(context):
    get_driver().get("https://laboratoriofigital.recife.pe.gov.br/primeiro-escalao/")

@when(u'o valor "{nome}" for inserido no campo nome')
def inserir_valor_campo(context, nome):
    get_campo_nome().send_keys(nome)
    time.sleep(1)

@when(u'o valor "{secretaria}" for inserido no campo secretaria')
def inserir_valor_campo(context, secretaria):
    get_campo_secretaria().send_keys(secretaria)
    time.sleep(1)

@when(u'o valor "{cargo}" for inserido no campo cargo')
def inserir_valor_campo(context, cargo):
    get_campo_cargo().send_keys(cargo)
    time.sleep(1)

@when(u'o valor "{email}" for inserido no campo email')
def inserir_valor_campo(context, email):
    get_campo_email().send_keys(email)
    time.sleep(1)

@when(u'o valor "{whatsapp}" for inserido no campo whatsapp') 
def inserir_valor_campo(context, whatsapp):
    get_campo_whatsap().send_keys(whatsapp)
    time.sleep(3)

@when(u'o valor "{problema}" for inserido no campo problema')
def inserir_valor_campo(context, problema):
    get_campo_problema().send_keys(problema)
    time.sleep(3)

@when(u'o botão click me for pressionado')
def pressionar_botao_click_me(context):
    get_botao_click_me().click()
    time.sleep(2) 

@then(u'o sistema confirma o envio com sucesso')
def sistema_confirma_envio_sucesso(context):
    mensagem_sucesso = obter_mensagem_sucesso_formulario()
    assert "Formulário enviado com sucesso!" in mensagem_sucesso, \
        f"Mensagem de sucesso não encontrada ou incorreta. Esperado: 'Formulário enviado com sucesso!', Obtido: '{mensagem_sucesso}'"

# ________________________________________________________________________________

@given(u'que a página de login seja acessada')
def acessar_site_login(context):
    get_driver().get("https://laboratoriofigital.recife.pe.gov.br/login/")

@when(u'o valor "{emaillogin}" for inserido no campo email de login')
def inserir_valor_campo(context, emaillogin):
    get_campo_emaillogin().send_keys(emaillogin)
    time.sleep(2)

@when(u'o valor "{senha}" for inserido no campo senha')
def inserir_valor_campo(context, senha):
    get_campo_senha().send_keys(senha)
    time.sleep(2)

@when(u'o botão entrar for pressionado')
def clicar_botao_login(context):
    get_button_login()
    time.sleep(2)

@then(u'o sistema deve exibir uma mensagem de "E-mail ou senha inválidos."')
def validar_mensagem_emailsenha_invalido(context):
    mensagem_erro = obter_mensagem_erro_login_invalido()
    assert "E-mail ou senha inválidos." in mensagem_erro, \
        f"Mensagem de erro não encontrada ou incorreta. Esperado: 'E-mail ou senha inválidos.', Obtido: '{mensagem_erro}'"

#____________________________________________________________________________________________________________________________________


@given(u'que a página de login seja acessada novamente')
def acessar_site_login(context):
    get_driver().get("https://laboratoriofigital.recife.pe.gov.br/login/")

@when(u'o valor válido "{emailloginv}" for inserido no campo email de login')
def inserir_valor_campo(context, emailloginv):
    get_campo_emaillogin().send_keys(emailloginv)
    time.sleep(2)

@when(u'o valor válido "{senhav}" for inserido no campo senha')
def inserir_valor_campo(context, senhav):
    get_campo_senha().send_keys(senhav)
    time.sleep(2)

@when(u'o botão entrar for pressionado novamente')
def clicar_botao_login(context):
    get_button_login()
    time.sleep(2)

@then(u'o sistema deve exibir uma mensagem de "Bem-vindo, Luiz ao Laboratório de Estratégias Figital!"')
def validar_mensagem_boas_vindas(context):
    mensagem_exibida = obter_texto_mensagem_boas_vindas()
    assert "Bem-vindo, Luiz ao Laboratório de Estratégias Figital!" in mensagem_exibida, \
        f"Mensagem correta. Obtido: '{mensagem_exibida}'"