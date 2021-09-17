import ply.lex as lex

tokens = ['SELECAO', 'INSERIR','INTO', 'ATUALIZAR','APAGAR', 'WHERE', 'ORDER','BY', 'GROUP', 'HAVING','FROM']
t_ignore = ' \t'
t_SELECAO = r'SELECT'
t_INSERIR = r'INSERT'
t_ATUALIZAR = r'UPDATE'
t_APAGAR = r'DELETE'


analisador = lex.lex()
teste = "SELECT"
teste2 = "INSERT"
teste3 = "UPDATE"
teste4 = "DELETE"

analisador.input(teste)
for token in analisador:
  print(token.type, token.value)

analisador.input(teste2)
for token in analisador:
  print(token.type, token.value)

analisador.input(teste3)
for token in analisador:
  print(token.type, token.value)

analisador.input(teste4)
for token in analisador:
  print(token.type, token.value)