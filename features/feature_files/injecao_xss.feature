Funcionalidade: Segurança na tela de login
	@xss
	Cenário: Injeção de script malicioso no campo de usuário
		Dado o usuário acessa a tela de login
		Quando ele preenche o campo de usuário com "<script>alert('XSS')</script>"
		E insere uma senha qualquer
		E clica em "Entrar"
		Então o sistema não deve executar nenhum script malicioso
