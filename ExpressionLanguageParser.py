import ply.yacc as yacc
from SintaxeAbstrata import *
from VisitorPrinter import *
from ExpressionLanguageLex import tokens



def p_inicioCriarTabelaSimple(p):
  '''inicio : criartabela'''
  p[0] = ComposicaoCriarTabela (p[1], None)

def p_inicioComposicaoCriarTabela(p):
  '''inicio : criartabela inicio'''  
  p[0] = ComposicaoCriarTabela(p[1], p[2])
 
def p_inicioInserirDadosSimple(p):
  '''inicio : inserirdados'''
  p[0] = ComposicaoInserirDados (p[1], None)

def p_inicioComposicaoInserirDados(p):
  '''inicio : inserirdados inicio'''
  p[0] = ComposicaoInserirDados (p[1], p[2])

def p_literalNumFloat(p):
  '''literal : NUMFLOAT '''
  p[0] = NumFloat(p[1])

def p_literalNumInteiro(p):
  '''literal : NUMINTEIRO '''
  p[0] = NumInteiro(p[1])

def p_literalString(p):
  '''literal : STRING '''
  p[0] = String(p[1])

def p_criartabela(p):
  '''criartabela : CREATE TABLE ID ABREPARENTESES tabelacolunas FECHAPARENTESES'''
  p[0] = CriaTabela(p[3], p[5])
 
def p_inserirdados(p):
  '''inserirdados : INSERT INTO ID VALUES ABREPARENTESES dadosinseridos FECHAPARENTESES'''
  p[0] = InserirDados(p[3], p[6])
  


def p_dadosInseridosSimple(p):
  '''dadosinseridos : literal '''
  p[0] = ComposicaoDadosInseridos(p[1], None)
  
def p_dadosInseridos(p):
  '''dadosinseridos : literal VIRGULA dadosinseridos'''
  p[0] = ComposicaoDadosInseridos(p[1], p[3])

def p_tipoInt(p):
  '''tipo : INT'''
  p[0] = TipoInt()

def p_tipoVarChar(p):
  '''tipo : VARCHAR ABREPARENTESES NUMINTEIRO FECHAPARENTESES'''
  p[0] = TipoVarChar(p[3])

def p_tipoNumeric(p):
  '''tipo : NUMERIC'''
  p[0] = TipoNumeric()

def p_tipoDateTime(p):
  '''tipo : DATETIME'''
  p[0] = TipoDateTime()

def p_tipoNumFloat(p):
  '''tipo : NUMFLOAT'''
  p[0] = TipoNumFloat()

def p_sufixoNotNull(p):
  '''sufixotable : NOT NULL'''
  p[0] = SufixoNotNull()

def p_sufixoNull(p):
  '''sufixotable : NULL'''
  p[0] = SufixoNull()

def p_sufixoNotNullPrimaryKey(p):
  '''sufixotable : NOT NULL PRIMARY KEY'''
  p[0] = SufixoNotNullPrimaryKey()

def p_tabelacolunas(p):
  '''tabelacolunas : ID tipo sufixotable
                     | ID tipo            
                     | ID tipo sufixotable VIRGULA tabelacolunas
                     | ID tipo VIRGULA tabelacolunas'''

def p_tabelacolunasimplessufixo(p):
  '''tabelacolunas : ID tipo sufixotable'''
  p[0] = TabelaColunasSimples(p[1], p[2], p[3])

def p_tabelacolunassimples(p):
  '''tabelacolunas : ID tipo'''
  p[0] = TabelaColunasSimples(p[1], p[2], None)

def p_tabelacolunassufixo(p):
  '''tabelacolunas : ID tipo sufixotable VIRGULA tabelacolunas'''
  p[0] = TabelaColunasComposta(p[1], p[2], p[3], p[5])

def p_tabelacolunas(p):
  '''tabelacolunas : tipo VIRGULA tabelacolunas'''
  p[0] = TabelaColunasComposta(p[1], p[2], None, p[4])

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
             | if
		         | listtypedid'''
  p[0] = p[1]

def p_declarevar(p):
  '''declarevar : DECLARE listtypedid'''
  p[0] = Declarevar(p[2])
      
def p_comandosimples(p):
  '''comandos : comando'''
  p[0] = Comandos(p[1])

def p_comandos(p):
  '''comandos : comando comandos'''
  p[0] = ComandosComando(p[1], p[2])

def p_selectlisttyped(p):
  '''select : SELECT listtypedid FROM ID'''
  p[0] = SelectTypedId(p[2], p[4])

def p_selectMul(p):
  '''select : SELECT MUL FROM ID'''
  p[0] = SelectMul(p[4])

def p_SelectSum(p):
  '''select : SELECT SUM ABREPARENTESES ID FECHAPARENTESES FROM ID WHERE ID IGUAL ID'''
  p[0] = SelectSum(p[4], p[7], p[9], p[11])

def p_deallocate(p):
  '''deallocate : DEALLOCATE ID'''
  p[0] = Deallocate(p[2])

def p_listtypeidsimples(p):
  '''listtypedid : ID tipo'''
  p[0] = ListTypeIdSimples(p[1], p[2])

def p_listtypeidcomposto(p):
  '''listtypedid : ID tipo VIRGULA listtypedid'''
  p[0] = ListTypeIdComposto(p[1], p[2], p[4])
  
def p_dadossemtipoSimples(p):
  '''dadossemtipo : ID'''
  p[0] = ComposicaoDadosSemTipo(p[1], None)

def p_dadossemtipo(p):
  '''dadossemtipo : ID VIRGULA dadossemtipo'''
  p[0] = ComposicaoDadosSemTipo(p[1], p[3])

def p_while(p):
  '''while : WHILE ABREPARENTESES ID IGUAL ZERO FECHAPARENTESES comandos'''
  p[0] = While(p[3],p[7])

def p_begin(p):
  '''begin : BEGIN comandos END'''
  p[0] = Begin(p[2])

def p_beginSet(p):
  '''begin : BEGIN set comandos END '''
  p[0] = BeginSet(p[2],p[3])

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

def p_set(p):
  '''set : SET ID IGUAL ABREPARENTESES select FECHAPARENTESES'''
  p[0] = Set(p[2], p[3])

# 1 - IF ID IGUAL literal begin ELSE begin
# 2 - IF ID IGUAL literal comando ELSE comando
# 3 - IF ID IGUAL literal comando ELSE begin
# 4 - IF ID IGUAL literal begin ELSE comando

# 5 - IF ID IGUAL literal comando 
# 6 - IF ID IGUAL literal begin

# 7 - IF ID IGUAL literal begin ELIF ID IGUAL literal begin 
# 8 - IF ID IGUAL literal comando ELIF ID IGUAL literal comando
# 9 - IF ID IGUAL literal comando ELIF ID IGUAL literal begin
# 10 -IF ID IGUAL literal begin ELIF ID IGUAL literal comando

def p_if1(p):
  '''if : IF ID IGUAL literal begin ELSE begin'''
  p[0] = IfElse(p[2], p[4], p[5], None, p[7], None)

def p_if2(p):
  '''if : IF ID IGUAL literal comando ELSE comando'''
  p[0] = IfElse(p[2], p[4], None, p[5], None, p[7])

def p_if3(p):
  '''if : IF ID IGUAL literal comando ELSE begin'''
  p[0] = IfElse(p[2], p[4], None, p[5], p[6], None)

def p_if4(p):
  '''if : IF ID IGUAL literal begin ELSE comando'''
  p[0] = IfElse(p[2], p[4], p[5], None, None, p[7])

def p_if5(p):
  '''if : IF ID IGUAL literal comando'''
  p[0] = IfElse(p[2], p[4], None, p[5])

#ID, literal, begin, comando
#(self, IDIf, literalIf, beginIf, comandoIf, beginElse, comandoElse):

def p_if6(p):
  '''if : IF ID IGUAL literal begin'''
  p[0] = If(p[2], p[4], p[5], None)

def p_if7(p):
  '''if : IF ID IGUAL literal begin ELIF ID IGUAL literal begin'''
  p[0] = IfElif(p[2], p[4], p[5], p[6], None, p[7], p[9], p[10], None)

def p_if8(p):
  '''if : IF ID IGUAL literal comando ELIF ID IGUAL literal comando'''
  p[0] = IfElif(p[2], p[4], None, p[5], p[7], p[9] , None, p[10])

def p_if9(p):
  '''if : IF ID IGUAL literal comando ELIF ID IGUAL literal begin'''
  p[0] = IfElif(p[2], p[4], None, p[5], p[7], p[9], p[10], None)

def p_if10(p):
  '''if : IF ID IGUAL literal begin ELIF ID IGUAL literal comando'''
  p[0] = IfElif(p[2],p[4],p[5],None,p[7], p[9], None,p[10])

# def __init__(self, IDIf, literalIf, beginIf, comandoIf, IDElif, literalElif, beginElif, comandoElif):  
  
def p_exec(p):
  '''exec : EXEC ID dadossemtipo OUTPUT'''
  p[0] = Exec(p[2], p[3])


def p_error(p):
  print('Error')

parser = yacc.yacc()

visitor = VisitorPrinter()

s = """DECLARE C_CLIENTE CURSOR FOR   SELECT CD_CLIENTE, NM_CLIENTE, CPF, DT_INCLUSAO FROM TB_CLIENTE OPEN C_CLIENTE FETCH C_CLIENTE INTO @CD_CLIENTE, @NM_CLIENTE, @CPF, @DT_INCLUSAO WHILE (@@FETCH_STATUS = 0) BEGIN SET @QTD_PRODUTOS = (SELECT SUM(QUANTIDADE) FROM TB_VENDAS WHERE CD_CLIENTE = @CD_CLIENTE) EXEC SP_CLASSIFICA_CLIENTE @DT_INCLUSAO, @QTD_PRODUTOS,@CLASSIFICACAO OUTPUT IF @CLASSIFICACAO = 'PARCEIRO' INSERT INTO TB_CLIENTE_PARCEIRO VALUES(@CD_CLIENTE,@NM_CLIENTE, @CPF, @DT_INCLUSAO) ELSE INSERT INTO TB_CLIENTE_ALVO VALUES(@CD_CLIENTE, @NM_CLIENTE, @CPF,@DT_INCLUSAO) FETCH C_CLIENTE INTO @CD_CLIENTE,@NM_CLIENTE, @CPF, @DT_INCLUSAO, @QTD_PRODUTOS END CLOSE C_CLIENTE DEALLOCATE C_CLIENTE END"""

#s = """INSERT INTO TB_CLIENTE VALUES(1,'JOAO',5444,'20180301')"""

#s = """ CREATE TABLE TB_CLIENTE (CD_CLIENTE INT NOT NULL PRIMARY KEY,
 # NM_CLIENTE VARCHAR(60) NOT NULL,CPF INT NULL,
  #DT_INCLUSAO DATETIME NOT NULL
#)"""

result = parser.parse(s)
#print(type(result))
result.accept(visitor)


# while True:
#  try:
#      s = input('Funcionando > ')
#  except EOFError:
#      break
#  if not s: continue
#  result = parser.parse(s)
#  print(result)
#  result.accept(Visitor)

#lexer.input(teste)
#passer = yacc.yacc(debug=True)
#passer.parse(teste)