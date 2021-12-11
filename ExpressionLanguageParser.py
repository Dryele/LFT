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
				              | literal VIRGULA dadosinseridos'''

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
            
def p_comandos(p):
  '''comandos : comando
                | comando comandos'''

def p_select(p):
  '''select : SELECT listtypedid FROM ID 
              | SELECT MUL FROM ID 
              | SELECT SUM ABREPARENTESES ID FECHAPARENTESES FROM ID WHERE ID IGUAL ID'''

def p_deallocate(p):
  '''deallocate : DEALLOCATE ID'''

def p_listtypeid(p):
  '''listtypedid : ID tipo 
			             | ID tipo VIRGULA listtypedid'''

def p_dadossemtipo(p):
  '''dadossemtipo : ID
			              | ID VIRGULA dadossemtipo'''

def p_while(p):
  '''while : WHILE ABREPARENTESES ID IGUAL ZERO FECHAPARENTESES comandos'''

def p_procedure(p):
  '''procedure : CREATE OR ALTER PROCEDURE ID AS begin   comandos close deallocate END '''

def p_open(p):
  '''open : OPEN ID'''

def p_close(p):
  '''close : CLOSE ID''' 

def p_fetch(p):
  '''fetch : FETCH ID INTO dadossemtipo'''

def p_begin(p):
  '''begin : BEGIN comandos END
             | BEGIN set comandos END '''

def p_set(p):
  '''set : SET ID IGUAL ABREPARENTESES select FECHAPARENTESES'''

def p_if(p):
  '''if : ID IGUAL STRING
	        | ID IGUAL NUMINTEIRO
	        | ID IGUAL NUMFLOAT'''

def p_exec(p):
  '''exec : EXEC ID dadossemtipo OUTPUT'''




#lexer.input(teste)
passer = yacc.yacc(debug=True)
passer.parse(teste)