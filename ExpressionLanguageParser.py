import ply.yacc as yacc
from ExpressionLanguageLex import tokens
from SintaxeAbstrata import *


def p_inicio(p):
	'''inicio : criartabela 
              | inserirdados
              | criartabela inicio
              | inserirdados inicio
  '''
	print("Inicio")

def p_literal(p):
  '''literal : NUMFLOAT 
               | NUMINTEIRO
               | STRING '''

def p_criartabela(p):
  '''criartabela : CREATE TABLE ID ABREPARENTESES tabelacolunas FECHAPARENTESES'''
  p[0] = CriaTabela(p[3], p[5])
  # print("Criar Tabela")

def p_inserirdados(p):
  '''inserirdados : INSERT INTO ID VALUES ABREPARENTESES dadosinseridos FECHAPARENTESES'''
  p[0] = InserirDados(p[3], p[6])
  #print("inserirdados")

def p_dadosinseridosum(p):
  '''dadosinseridos : literal '''
  p[0] = DadosInseridosUm(p[1])
  
def p_dadosinseridosdois(p):
  '''dadosinseridos : literal VIRGULA dadosinseridos'''
  p[0] = DadosInseridosUm(p[1], p[3])
  
def p_tipo(p):
  '''tipo : INT
            | VARCHAR ABREPARENTESES NUMINTEIRO FECHAPARENTESES
            | NUMERIC
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

def p_comando(p):
  '''comando : declarevar
             | select 
		         | open
             | inserirdados
		         | close
		         | dadossemtipo
		         | deallocate
		         | while
		         | begin
		         | listtypedid'''

def p_declarevar(p):
  '''declarevar : DECLARE listtypedid'''
  p[0] = Declarevar(p[2])
            
def p_comandos(p):
  '''comandos : comando
                | comando comandos'''

def p_select(p):
  '''select : SELECT listtypedid FROM ID 
              | SELECT MUL FROM ID 
              | SELECT SUM ABREPARENTESES ID FECHAPARENTESES FROM ID WHERE ID IGUAL ID'''

def p_deallocate(p):
  '''deallocate : DEALLOCATE ID'''
  p[0] = Deallocate(p[2])

def p_listtypeid(p):
  '''listtypedid : ID tipo 
			             | ID tipo VIRGULA listtypedid'''

def p_dadossemtipo(p):
  '''dadossemtipo : ID
			              | ID VIRGULA dadossemtipo'''

def p_while(p):
  '''while : WHILE ABREPARENTESES ID IGUAL ZERO FECHAPARENTESES comandos'''
  p[0] = While(p[3],p[7])

def p_procedure(p):
  '''procedure : CREATE OR ALTER PROCEDURE ID AS begin comandos close deallocate END '''
  p[0] = Procedure(p[5], p[7], p[8], p[9], p[10])

def p_open(p):
  '''open : OPEN ID'''
  p[0] = Open(p[3])

def p_close(p):
  '''close : CLOSE ID''' 
  p[0] = Close(p[3])

def p_fetch(p):
  '''fetch : FETCH ID INTO dadossemtipo'''
  p[0] = Open(p[2], p[4])

def p_begin(p):
  '''begin : BEGIN comandos END
             | BEGIN set comandos END '''

def p_set(p):
  '''set : SET ID IGUAL ABREPARENTESES select FECHAPARENTESES'''
  p[0] = Set(p[2], p[3])

def p_if(p):
  '''if : ID IGUAL STRING
	        | ID IGUAL NUMINTEIRO
	        | ID IGUAL NUMFLOAT'''

def p_exec(p):
  '''exec : EXEC ID dadossemtipo OUTPUT'''
  p[0] = Exec(p[2], p[3])


def p_error(p):
  print('Error')

parser = yacc.yacc()

while True:
 try:
     s = input('calc > ')
 except EOFError:
     break
 if not s: continue
 result = parser.parse(s)
 print(result)


#lexer.input(teste)
#passer = yacc.yacc(debug=True)
#passer.parse(teste)