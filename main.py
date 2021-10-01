import ply.lex as lex
import ply.yacc as yacc

# colocar todas as palavras reservadas da linguagem aqui! 
reserved = {'PRIMARY': 'PRIMARY', 'KEY' : 'KEY', 'INT':'INT','SELECT':'SELECT', 'INSERT':'INSERT','INTO':'INTO', 'UPDATE':'UPDATE','DELETE':'DELETE', 'WHERE':'WHERE','ORDER':'ORDER','BY':'BY', 'GROUP':'GROUP', 'HAVING':'HAVING','FROM':'FROM', 'VALUES':'VALUES', 'SET':'SET', 'CREATE':'CREATE', 'TABLE':'TABLE',  'ALTER':'ALTER', 'DECLARE':'DECLARE', 'PROCEDURE':'PROCEDURE', 'AS':'AS', 'OR':'OR', 'BEGIN':'BEGIN', 'IF':'IF', 'SET':'SET', 'END':'END', 'OUTPUT':'OUTPUT', 'PRINT':'PRINT','EXEC':'EXEC', 'ISNULL':'ISNULL', 'FOR':'FOR', 'LEFT':'LEFT', 'JOIN':'JOIN', 'ON':'ON','OPEN':'OPEN', 'FETCH':'FETCH','WHILE':'WHILE','ELSE':'ELSE', 'DEALLOCATE':'DEALLOCATE', 'DO':'DO', 'CLOSE':'CLOSE', 'NOT':'NOT', 'NULL':'NULL', 'INNER':'INNER','RIGHT':'RIGHT','DISTINCT':'DISTINCT','DATEPART':'DATEPART','ISNULL':'ISNULL','VARCHAR':'VARCHAR','DATETIME':'DATETIME','NUMBER':'NUMBER'}

tokens = ['ID', 'NUMERO', 'MUL', 'DIV', 'SOMA', 'SUB', 'PERCE','MENORQ','MAIORQ', 'IGUAL', 'MAIORIGUAL', 'MENORIGUAL','ABREPARENTESES','FECHAPARENTESES','VIRGULA','NUMFLOAT','NUMINTEIRO', 'STRING']+list(reserved.values())

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
t_ABREPARENTESES =r'\('
t_FECHAPARENTESES =r'\)'
t_VIRGULA =r','

t_ignore=" \t\n"
#reconhcer identificador, inicio de nomes e simbolos da linguagem
def t_NUMFLOAT(t):
  r'([1-9][0-9]*(\.[0-9]+)([eE][0-9]+)?)|(0(\.[0-9]+)([eE][0-9]+)?)'
  t.value = float(t.value)
  return t
  
def t_NUMINTEIRO(t):
  r'[1-9][0-9]*'
  t.value = int(t.value)
  return t

def t_ID(t):
	  r'[a-zA-Z@_0-9][a-zA-Z_0-9]*(\.[a-zA-Z_0-9]+)?'
	  t.type = reserved.get(t.value.upper(), 'ID')
	  return t

def t_STRING(t):
  r'\'[^\n\']|"[^\n"]"'
  return t

def t_COMENTARIO_LINHA(t):
   r'--[^\n]*'
   pass
     
def t_COMENTARIO_MULTINHAS(t):
   r'/\*[^(\*/)]*\*/'
   pass
    

def p_inicio (p):
	'''inicio : criartabela 
              | inserirdados
              | criartabela inicio
              | inserirdados inicio
  '''
	print("Inicio")

def p_literal (p):
  '''literal : NUMFLOAT 
               | NUMINTEIRO
               | STRING 
  '''

def p_criartabela(p):
	'''criartabela : CREATE TABLE ID ABREPARENTESES tabelacolunas FECHAPARENTESES'''
	print("Criar Tabela")

def p_inserirdados(p):
  '''inserirdados : INSERT INTO ID VALUES ABREPARENTESES dadosinseridos FECHAPARENTESES'''
  print("inserirdados")

def p_dadosinseridos(p):
  '''dadosinseridos : literal 
				              | literal VIRGULA                dadosinseridos'''

def p_tipo(p):
  '''tipo : INT
            | VARCHAR ABREPARENTESES NUMINTEIRO FECHAPARENTESES
            | NUMBER
            | DATETIME
            | NUMFLOAT'''
  print("tipo")

def p_sufixotable(p):
  '''sufixotable : NOT NULL
    | NULL
    | NOT NULL PRIMARY KEY'''
  print("Sufixo: ", p[1])
   

def p_tabelacolunas(p):
  '''tabelacolunas : ID tipo sufixotable
         | ID tipo            
         | ID tipo sufixotable VIRGULA tabelacolunas
         | ID tipo VIRGULA tabelacolunas'''





lexer = lex.lex()
teste = """ CREATE TABLE TB_CLIENTE (
             CD_CLIENTE INT NOT NULL PRIMARY KEY,
             NM_CLIENTE INT NOT NULL,
             CPF INT NULL,
             DT_INCLUSAO INT NOT NULL )
             INSERT INTO TB_CLIENTE VALUES(1)"""
#teste = "Select VALOR TABLE.LINHA @ SET 25 * / - + % < > = >= <="

#lexer.input(teste)
passer = yacc.yacc(debug=True)
passer.parse(teste)