def verificar_cadastro(nome,email,senha,confSenha):
    if not nome or not email or not senha or not confSenha:
        return "Preencha todos os campos"
    
    if len(nome.strip()) < 3:
        return "O seu nome precisa ter pelo menos 3 caracteres"
    
    if "@" not in email or "." not in email:
        return "Email inválido."
    
    if len(senha) < 8:
        return "A senha precisa ter pelo menos 8 caracteres."

    return "Cadastro válido."