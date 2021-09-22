import ply.lex as lex

# colocar todas as palavras reservadas da linguagem aqui! 
reserved = {'SELECT':'SELECT', 'INSERT':'INSERT','INTO':'INTO', 'UPDATE':'UPDATE','DELETE':'DELETE', 'WHERE':'WHERE','ORDER':'ORDER','BY':'BY', 'GROUP':'GROUP', 'HAVING':'HAVING','FROM':'FROM', 'VALUES':'VALUES', 'SET':'SET', 'CREATE':'CREATE', 'TABLE':'TABLE',  'ALTER':'ALTER', 'DECLARE':'DECLARE', 'PROCEDURE':'PROCEDURE', 'AS':'AS', 'OR':'OR', 'BEGIN':'BEGIN', 'IF':'IF', 'SET':'SET', 'END':'END', 'OUTPUT':'OUTPUT', 'PRINT':'PRINT','EXEC':'EXEC', 'ISNULL':'ISNULL', 'FOR':'FOR', 'LEFT':'LEFT', 'JOIN':'JOIN', 'ON':'ON','OPEN':'OPEN', 'FETCH':'FETCH','WHILE':'WHILE','ELSE':'ELSE', 'DEALLOCATE':'DEALLOCATE', 'DO':'DO', 'CLOSE':'CLOSE', 'NOT':'NOT', 'NULL':'NULL', 'INNER':'INNER','RIGHT':'RIGHT','DISTINCT':'DISTINCT','DATEPART':'DATEPART','ISNULL':'ISNULL'}
tokens = ['ID', 'NUMERO', 'MUL', 'DIV', 'SOMA', 'SUB', 'PERCE','MENORQ','MAIORQ', 'IGUAL', 'MAIORIGUAL', 'MENORIGUAL']+list(reserved.values())
t_ignore = ' \t'

#reconhcer identificador, inicio de nomes e simbolos da linguagem
def t_NUMERO(t):
  r'[1-9][0-9]*(\.[0-9]+)?([eE][0-9]+)?'
  return t

def t_ID(t):
  r'[a-zA-Z@_0-9][a-zA-Z_0-9]*(\.[a-zA-Z_0-9]+)?'
  t.type = reserved.get(t.value.upper(), 'ID')
  return t

def t_COMENTARIO(t):
  r'--'
  pass

t_MUL = r'\*'
t_DIV =r'/'
t_SUB = r'-'
t_SOMA =r'\+'
t_PERCE =r'%'
t_MENORQ =r'<'
t_MAIORQ =r'>'
t_IGUAL =r'='
t_MAIORIGUAL =r'>='
t_MENORIGUAL =r'<='



analisador = lex.lex()
teste = "Select VALOR TABLE.LINHA SET 25 * / - + % < > = >= <="

analisador.input(teste)
for token in analisador:
  print(token.type, token.value)


