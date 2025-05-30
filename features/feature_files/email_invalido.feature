Funcionalidade: Validação de e-mail do formulário Rede de Transformação Digital
    @email_invalido
	  Cenário: Usuário insere e-mail com formato inválido
	    Quando o usuário está no formulário
	    Quando ele preenche o campo e-mail com "cers.rodrigues"
	    E clica em "Enviar"
	    Então o sistema deve exibir uma mensagem de "E-mail inválido"
