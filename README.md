# Validação de Senha em python

Este projeto é um programa simples que valida senhas de acordo com regras de segurança básicas

- Mínimo de 8 caracteres
- Pelo menos um número
- Pelo menos uma letra maiúscula

---

## Como usar

1. Clone esse repositório
```bash
git clone https://github.com/israeloscar/valida-o-senhas.git
```

2. Entre na pasta do projeto
```bash
cd valida-o-senhas
```

3. Execute o arquivo python
```bash
python senha.py
```

4. Siga as instruções para digitar sua senha

## Estrutura do código

- `tem_numero(senha)`: verifica se a senha contém pelo menos um número  
- `tem_letra_maiuscula(senha)`: verifica se a senha contém pelo menos uma letra maiúscula  
- `validar_senha(senha)`: valida a senha e retorna uma mensagem de erro ou None  
- Loop principal: solicita a senha ao usuário e exibe mensagens de validação

## Autor

Israel Oscar