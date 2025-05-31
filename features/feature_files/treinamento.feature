Funcionalidade: Teste automação - Lab Figital LP


    @Smoke @test1
    Cenário: Cadastro no formulário
        Dado que a página de formulário de 1º Escalão seja acessada
        Quando o valor "Luiz" for inserido no campo nome
        E o valor "Saúde" for inserido no campo secretaria
        E o valor "Subchefe" for inserido no campo cargo
        E o valor "luizviniciusprimo@gmail.com" for inserido no campo email
        E o valor "8199865043" for inserido no campo whatsapp 
        E o valor "Falta de leitos" for inserido no campo problema
        E o botão click me for pressionado
        Então  o sistema confirma o envio com sucesso


    @test2
        Cenário: Login com credenciais inválidas
            Dado que a página de login seja acessada
            Quando o valor "Luiz@gmail.com" for inserido no campo email de login
            E o valor "luiz011" for inserido no campo senha
            E o botão entrar for pressionado
            Então o sistema deve exibir uma mensagem de "E-mail ou senha inválidos."

    @test3
        Cenário: Login com credenciais válidas
            Dado que a página de login seja acessada novamente
            Quando o valor válido "luizviniciusprimo@gmail.com" for inserido no campo email de login
            E o valor válido "#luiz123456" for inserido no campo senha
            E o botão entrar for pressionado novamente
            Então o sistema deve exibir uma mensagem de "Bem-vindo, Luiz ao Laboratório de Estratégias Figital!"