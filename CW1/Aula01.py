# Aula01 - Testes de acesso.

# Solicitamos os dados de Usuário e senha

login = input('Digite o seu login: ')
senha = input('Digite sua senha:  ')

# Aqui conferimos se os dados estão corretos

if login == 'user-teste' and senha == 'teste@1':
    print('Bem-Vindo', login)
else:
    print('Acesso negado, Usuário ou Senha invalidos! ')